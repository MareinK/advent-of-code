(load-file "processor-old.clj")

(let [program (assoc (aoc/instructions "13.txt") 0 2)
      [send recv] (aoc/run-async program)]
  ; (defn receive [n] (for [_ (range n)] (recv)))
  ; (partition 3 (receive (* 1057 3))))  
  (defn state [n]
    (if
     (= n 0)
      [nil nil nil]
      (let [[x y t] [(recv) (recv) (recv)]]
        (cond
          (= t 3)
          (assoc (state (dec n)) 0 x)
          (= t 4)
          (assoc (state (dec n)) 1 x)
          (= x -1)
          (assoc (state (dec n)) 2 t)
          :else
          (state (dec n))))))
  (defn move [s]
    (let [[x x'] s]
      (cond
        (< x x')
        (send 1)
        (> x x')
        (send -1)
        :else
        (send 0))))
  (move (state 1057))
  (move (state 4))
  (state 3))
