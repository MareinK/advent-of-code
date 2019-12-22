(load "util.lisp")

(defun fuel (mass)
    (let ((f (floor (- (/ mass 3) 2))))
        (if (> f 0)
            (+ f (fuel f))
            0)))

(print (sum (mapcar 'fuel (mapcar `parse-integer (file-lines "1.txt")))))
