(defn digits [n]
    (map (comp read-string str) (str n)))

(defn run-lengths [n]
    (map count (partition-by identity (str n))))

(defn valid-password? [n]
    (and
        (apply <= (digits n))
        (.contains (run-lengths n) 2)))

(defn valid-passwords [a b]
    (filter valid-password? (range a (+ b 1))))

(defn solve []
    (count (valid-passwords 245182 790572)))

(solve)
