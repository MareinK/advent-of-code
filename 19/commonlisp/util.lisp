(load "/usr/lib/quicklisp/setup")
(ql:quickload "uiop")

(defun file-lines (filename)
  (with-open-file (stream filename)
    (loop for line = (read-line stream nil)
          while line
          collect line)))

(defun sum (list) (reduce '+ list))
