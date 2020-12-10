(def k 3)

(def input
  (->> (clojure.string/split-lines (slurp "10.txt"))
       (map read-string)))

(->> input
     (sort)
     (reverse)
     ((juxt butlast rest))
     (apply map -)
     (concat [1 k])
     (frequencies)
     (vals)
     (reduce *)
     (println))


;; (def paths
;;   (memoize
;;    (fn [graph x]
;;      (if (zero? x)
;;        [[]]
;;        (map #(conj % x) (mapcat (partial paths graph) (get graph x)))))))

(def count-paths
  (memoize
   (fn [graph x]
     (if (zero? x)
       1
       (reduce + (map (partial count-paths graph) (get graph x)))))))

(->> input
     ((juxt identity (comp list (partial + k) (partial apply max))))
     (apply concat [0])
     ((fn [nums] (map (fn [num] [num (filter #(< (- num k 1) % num) nums)]) nums)))
     (into {})
     (#(count-paths % (apply max (keys %))))
     (println))
