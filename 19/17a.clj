(load-file "processor-old.clj")

(defn scaffolds [recv n x y]
  (if (< n 1975)
    (let [v (recv)
          r (scaffolds
             recv
             (inc n)
             (if (= v 10) 0 (inc x))
             (if (= v 10) (inc y) y))]
      (if (= v 35)
        (conj r [x y])
        r))
    #{}))

(defn intersection? [scaf s]
  (every?
   (partial contains? scaf)
   (for [d [[0 -1] [0 1] [-1 0] [1 0]]]
     (map + s d))))

(defn intersections [scaf]
  (filter (partial intersection? scaf) scaf))

(let [[send recv] (aoc/run-file-async "17.txt")]
  (apply
   +
   (map
    (partial apply *)
    (intersections (scaffolds recv 0 0 0)))))
