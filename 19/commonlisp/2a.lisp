(load "util.lisp")

(defun input (filename)
  (with-open-file (stream filename)
    (loop for line = (read-line stream nil)
          while line
          collect line)))

;; (print (uiop:split-string "," (input "2.txt")))
(print (mapcar `parse-integer (uiop:split-string "12,34,56,78" :separator ",")))
