(println
 (let [input (map #(re-find #"(\d*)-(\d*) (\w): (\w*)" %) (clojure.string/split (slurp "2.txt") #"\n"))]
   (count
    (filter
     #(let [[_ a b c cs] %]
        (<=
         (read-string a)
         (or (get (frequencies cs) (first c)) 0)
         (read-string b)))
     input))))

(defn xor [& args]
  (->> args
       (filter identity)
       (count)
       (= 1)))

(println
 (let [input (map #(re-find #"(\d*)-(\d*) (\w): (\w*)" %) (clojure.string/split (slurp "2.txt") #"\n"))]
   (count
    (filter
     #(let [[_ a b c cs] %]
        (xor
         (= (first c) (nth cs (dec (read-string a))))
         (= (first c) (nth cs (dec (read-string b))))))
     input))))
