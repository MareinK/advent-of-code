(defn password-check [n]
    (let [s (str n)]
        (and
            (apply <= (map (comp read-string str) s))
            (re-matches #".*(\d)\1.*" s))))

(defn filter-passwords [a b]
    (filter password-check (range a (+ b 1))))

(defn solve []
    (count (filter-passwords 245182 790572)))

(solve)
