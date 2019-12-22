(load "util.lisp")

(defun fuel (mass) (floor (- (/ (parse-integer mass) 3) 2)))

(print (sum (mapcar 'fuel (file-lines "1.txt"))))
