(def input
  (->>
   (clojure.string/split-lines (slurp "12.txt"))
   (map (juxt first (comp read-string #(subs % 1))))))

(def cardinals
  {\N [0 1]
   \S [0 -1]
   \E [1 0]
   \W [-1 0]})

(def rotations
  {\L #(vector (- %2) %1)
   \R #(vector  %2 (- %1))})

(doseq [[init-dir cardinals-affect] [[[1 0] :pos]
                                     [[10 1] :dir]]]
  (->> (loop [[[action value] & instrs] input
              pos [0 0]
              dir init-dir]
         (cond
           (contains? cardinals action) (let [moves (repeat value (get cardinals action))
                                              [new-pos new-dir] (case cardinals-affect
                                                                  :pos [(apply mapv + pos moves) dir]
                                                                  :dir [pos (apply mapv + dir moves)])]
                                          (recur instrs new-pos new-dir))
           (contains? rotations action) (let [iters (iterate (partial apply (get rotations action)) dir)]
                                          (recur instrs pos (nth iters (quot value 90))))
           (= action \F) (recur instrs (apply mapv + pos (repeat value dir)) dir)
           (nil? action) pos))
       (map #(Math/abs %))
       (reduce +)
       (println)))
