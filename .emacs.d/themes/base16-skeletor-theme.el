;; base16-skeletor-theme.el -- A base16 colorscheme

;;; Commentary:
;; Base16: (https://github.com/chriskempson/base16)

;;; Authors:
;; Scheme: Antti Joutsi (http://jarizleifr.github.io)
;; Template: Kaleb Elwert <belak@coded.io>

;;; Code:

(require 'base16-theme)

(defvar base16-skeletor-colors
  '(:base00 "#111122"
    :base01 "#291b36"
    :base02 "#313148"
    :base03 "#746e9f"
    :base04 "#8e7e9d"
    :base05 "#d6cdee"
    :base06 "#eeeeff"
    :base07 "#ffffff"
    :base08 "#ff7979"
    :base09 "#d8d4ab"
    :base0A "#f3ae7c"
    :base0B "#95d34c"
    :base0C "#f7a7ca"
    :base0D "#7eb1f7"
    :base0E "#a886ef"
    :base0F "#4455bb")
  "All colors for Base16 Skeletor are defined here.")

;; Define the theme
(deftheme base16-skeletor)

;; Add all the faces to the theme
(base16-theme-define 'base16-skeletor base16-skeletor-colors)

;; Mark the theme as provided
(provide-theme 'base16-skeletor)

(provide 'base16-skeletor-theme)

;;; base16-skeletor-theme.el ends here
