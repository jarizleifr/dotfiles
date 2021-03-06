;;; early-init.el -*- lexical-binding: t; -*-

;; Set garbage collection threshold to 128MiB
(defvar default-gc-cons-threshold 134217728)
(setq gc-cons-threshold most-positive-fixnum
      gc-cons-percentage 0.6) 
(add-hook 'after-init-hook (lambda () (setq gc-cons-threshold default-gc-cons-threshold)))

;; Prevent flashing of white background (value from skeletor theme)
(set-face-attribute 'default nil :background "#111122" :foreground "#d7ceef")

;; Likewise, remove menus, toolbars and scrollbars before GUI is rendered
(push '(menu-bar-lines . 0) default-frame-alist)
(push '(tool-bar-lines . 0) default-frame-alist)
(push '(vertical-scroll-bars) default-frame-alist)

;; Use UTF-8 as default encoding
(set-language-environment "UTF-8")

