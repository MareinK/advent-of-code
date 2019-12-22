(defn input []
  (vec (map read-string (clojure.string/split (slurp "2.txt") #","))))

(defn opcode_arith [opcodes, i, op]
  (assoc
    opcodes
    (nth opcodes (+ i 3))
    (op
      (nth opcodes (nth opcodes (+ i 1)))
      (nth opcodes (nth opcodes (+ i 2))))))

(defn process [opcodes, i]
  (case (nth opcodes i)
    1 (process (opcode_arith opcodes i +) (+ i 4))
    2 (process (opcode_arith opcodes i *) (+ i 4))
    99 opcodes))

(defn do_replace [opcodes, a, b]
  (assoc (assoc opcodes 1 a) 2 b))

(defn solve [opcodes]
  (reduce + (for [x (range 100) y (range 100)]
    (if (= (nth (process (do_replace (vec (input)) x y) 0) 0) 19690720)
      (+ (* 100 x) y)
      0))))

(println (solve (input)))
