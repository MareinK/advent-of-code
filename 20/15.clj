(defn fmap [f m]
  (zipmap (keys m) (map f (vals m))))

(defn round [{i :i seen :seen prev :prev}]
  {:i (inc i)
   :seen (assoc seen prev (dec i))
   :prev (if (contains? seen prev) (- i 1 (get seen prev)) 0)})

(def nums (map read-string (clojure.string/split (slurp "15.txt") #",")))

(doseq [k [2020 30000000]]
  (time (as-> {:i (count nums)
               :seen (into {} (map vector (butlast nums) (range)))
               :prev (last nums)} $
          (iterate round $)
          (nth $ (- k (count nums)))
          (:prev $)
          (println $))))
