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

(defn do_replace [opcodes]
  (assoc (assoc opcodes 1 12) 2 2))

(println (nth (process (do_replace (input)) 0) 0))
