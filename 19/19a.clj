(load-file "processor-old.clj")

(def program (aoc/instructions "19.txt"))

(reduce
 +
 (for [x (range 50)
       y (range 50)]
   (let [[send recv] (aoc/run-async program)]
     (send x)
     (send y)
     (recv))))

