#!/bin/python

import argparse
import csv
from datetime import datetime, timedelta
import subprocess
import sys

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--date", type=str,
                        help="Date in YYYY-MM-DD format to track. Defaults to today.")
    parser.add_argument("-t", "--time", type=str,
                        help="Time in HH:mm or HH:mm-HH:mm format. Defaults to 08:00.")
    args = parser.parse_args()

    date_arg = args.date or datetime.today().strftime("%Y-%m-%d")
    date = datetime.strptime(date_arg, "%Y-%m-%d")

    time_arg = args.time or "08:00"
    times = time_arg.split("-", 1)
    if len(times) == 1:
        elapsed_time = get_delta(times[0])
    elif len(times) == 2:
        start_time = get_delta(times[0])
        end_time = get_delta(times[1])
        if start_time >= end_time:
            raise ValueError("Start time must be before end time.")
        elapsed_time = end_time - start_time
    else:
        elapsed_time = timedelta(hours=8)

    return date, elapsed_time

def get_delta(s):
    hours, minutes = int(s[:-3]), int(s[-2:])
    if not (hours == 24 and minutes == 0) and (not (0 <= hours < 24) or not (0 <= minutes < 60)):
        raise ValueError("Time should be between 00:00 and 24:00.")
    return timedelta(hours=hours, minutes=minutes)

def sum_time(subtag, data):
    items = data.items()
    return sum((time for tag, time in items if subtag in tag), timedelta())

# Run command
date, elapsed_time = parse_arguments()
date_end = date + timedelta(days=1)
command = [
    "arbtt-stats",
    "--m=0",
    "--output-format=csv",
    f"--filter=$date>={date.date()} && $date < {date_end.date()}"
]
output = subprocess.run(command, capture_output=True, text=True)
data = output.stdout.strip()

# Process
tag_times = {}
total_time = timedelta()
reader = csv.DictReader(data.splitlines())
for row in reader:
    tag = row["Tag"]
    time_str = row["Time"]

    time_parts = time_str.split(":")
    time = timedelta(hours=int(time_parts[0]), minutes=int(time_parts[1]))

    tag_times[tag] = time
    total_time += time


down_time = sum_time("Recreation", tag_times)
elapsed_time += down_time

print(f"Time tracked for {date.date()}:")

unassigned_time = elapsed_time - total_time
if unassigned_time > timedelta():
    print(f"\033[1;33m{unassigned_time} Unassigned\033[0m")
    print("------------------")

core_time = timedelta()
project_time = timedelta()
misc_time = timedelta()
sorted_tag_times = sorted(tag_times.items(), key=lambda item: item[1], reverse=True)
total_tracked_time = timedelta()
for tag, time in sorted_tag_times:
    if "Project" in tag:
        color = "\033[1;32m"
        project_time += time
    elif "Core" in tag:
        color = "\033[1;36m"
        core_time += time
    elif "Recreation" in tag:
        color = "\033[1;30m"
    else:
        color = "\033[1;37m"
        misc_time += time
    total_tracked_time += time
    print(f"{color}{str(time)} {tag}\033[0m")

print(f"\n\033[1;32m{project_time} Project\033[0m")
print(f"\033[1;36m{core_time} Core\033[0m")
print(f"\033[1;37m{misc_time} Miscellaneous\033[0m")
print(f"\033[1;30m{down_time} Downtime\033[0m")
print(f"\033[1;37m{total_tracked_time} Total time tracked\033[0m")

productive_percentage = (project_time + core_time) / elapsed_time * 100

print(f"\nProductive: {productive_percentage:.2f}%")
