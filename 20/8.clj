(->> (clojure.string/split-lines (slurp "8.txt"))
     (mapv #(clojure.string/split % #" "))
     ((fn [instrs]
        (loop [ip 0
               ips #{}
               acc 0]
          (if (contains? ips ip)
            acc
            (let [instr (nth instrs ip)
                  op (first instr)
                  val (-> (second instr) (read-string))
                  ips-new (conj ips ip)]
              (case op
                "nop" (recur (inc ip) ips-new acc)
                "acc" (recur (inc ip) ips-new (+ acc val))
                "jmp" (recur (+ ip val) ips-new acc)))))))
     (println))

(->> (clojure.string/split-lines (slurp "8.txt"))
     (mapv #(clojure.string/split % #" "))
     ((fn [instrs]
        (for [ip (keep-indexed #(when (->> (first %2) (contains? #{"nop" "jmp"})) %1) instrs)
              :let [op (-> (nth instrs ip) (first))
                    op-new (get {"nop" "jmp" "jmp" "nop"} op)
                    instrs (assoc-in instrs [ip 0] op-new)]]
          (loop [ip 0
                 ips #{}
                 acc 0]
            (cond
              (contains? ips ip) nil
              (< ip (count instrs)) (let [instr (nth instrs ip)
                                          op (first instr)
                                          val (-> (second instr) (read-string))
                                          ips-new (conj ips ip)]
                                      (case op
                                        "nop" (recur (inc ip) ips-new acc)
                                        "acc" (recur (inc ip) ips-new (+ acc val))
                                        "jmp" (recur (+ ip val) ips-new acc)))
              :else acc)))))
     (filter identity)
     (first)
     (println))
