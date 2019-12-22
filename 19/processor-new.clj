(defrecord Processor [mem ip rb val in? out? halt?])
(def proc0 (Processor. {} 0 0 nil false false false))

(defn stalled? [proc]
  (or
   (and (:in? proc) (nil? (:val proc)))
   (and (:out? proc) (some? (:val proc)))
   (:halt? proc)))

(defn step [proc]
  (assoc proc :halt? true))

(defn run [proc]
  (if (stalled? proc)
    proc
    (recur (step proc))))

(run proc0)
