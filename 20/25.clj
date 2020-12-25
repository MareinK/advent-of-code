(def subject-number 7)
(def modulus 20201227)

(defn modular-exponential-inverse [b c m]
  (loop [i 0, a 1]
    (if (= a c)
      i
      (recur (inc i) (mod (* a b) m)))))

(defn mod-pow [b e m]
  (.modPow (biginteger b) (biginteger e) (biginteger m)))

(defn loop-size [public-key]
  (modular-exponential-inverse subject-number public-key modulus))

(def public-keys (map read-string (clojure.string/split-lines (slurp "25.txt"))))

(println (mod-pow (first public-keys) (loop-size (second public-keys)) modulus))
