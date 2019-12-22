(ns aoc
  (:require [clojure.core.async
             :refer [>!! <!!]]
            [clojure.java.io :as io])
  (:import [java.io InputStream OutputStream]))

(defn chan-instream [c]
  (proxy [InputStream] []
    (read [dst off len]
      (aset-byte dst off (<!! c))
      1)))

(defn chan-outstream [c]
  (proxy [OutputStream] []
    (write [dst off len]
      (dorun (for [i (range len)]
               (>!! c (nth dst (+ off i))))))))

(defmacro with-in-chan [c & body]
  `(with-open [c# (io/reader (chan-instream ~c))]
     (binding [*in* c#] ~@body)))

(defmacro with-out-chan [c & body]
  `(let [c# (io/writer (chan-outstream ~c))]
     (binding [*out* c#] ~@body)))
