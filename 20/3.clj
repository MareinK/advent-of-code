(def input
  (map cycle (clojure.string/split (slurp "3.txt") #"\n")))

(defn slope-check [x y]
  (-> (map nth
           (take-nth y input)
           (take-nth x (range)))
      (frequencies)
      (get \#)))

(println (slope-check 3 1))
(println (apply * (map slope-check [1 3 5 7 1] [1 1 1 1 2])))
