(def input (clojure.string/split-lines (slurp "13.txt")))
(def init-time (read-string (first input)))
(def ids (->> (clojure.string/split (second input) #",")
              (map-indexed #(when (not= %2 "x") [%1 (read-string %2)]))
              (keep identity)
              (sort-by second)
              (reverse)))

(defn divides [n d]
  (= 0 (rem n d)))

(defn time-id-now [time]
  (some #(when (divides time (second %)) [time (second %)]) ids))

(defn all-ordered? [time]
  (every? #(divides (+ time (first %)) (second %)) ids))

;; part 1
(let [[time id] (->> (range init-time ##Inf)
                     (some time-id-now))]
  (println (* (- time init-time) id)))

;; part 2
(let [start 0
      [max-i max-id] (apply max-key second ids)
      offset (+ max-i (rem start max-id))]
  (->> (range (- start offset) ##Inf max-id)
       (filter all-ordered?)
       (first)
       (println)))
