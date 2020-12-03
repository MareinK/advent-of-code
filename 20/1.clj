(println
 (let [nums (map read-string (clojure.string/split (slurp "numbers.txt") #"\n"))]
   (first
    (for [a nums
          b nums
          c nums
          :when (= 3141 (+ a b c))]
      (list a b c)))))
