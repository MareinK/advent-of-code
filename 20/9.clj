(def k 25)

(defn check-num [xs x]
  (let [xs-set (set xs)]
    (some #(contains? xs-set (- x %)) xs)))

(def input
  (->> (clojure.string/split-lines (slurp "9.txt"))
       (map read-string)))

(def value
  (->> input
       ((juxt (partial partition k 1) (partial drop k)))
       (apply map vector)
       (filter (partial apply (complement check-num)))
       (first)
       (second)))

(println value)

(defn all-partitions [coll]
  (mapcat #(partition % 1 coll) (range 2 (count coll))))

(->> input
     (all-partitions)
     (filter #(= value (reduce + %)))
     (first)
     ((juxt (partial apply min) (partial apply max)))
     (reduce +)
     (println))
