(load-file "processor.clj")

(with-in-str "1"
  (aoc/run (aoc/instructions "9.txt")))

(with-in-str "2"
  (aoc/run (aoc/instructions "9.txt")))
