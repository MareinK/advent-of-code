{-# LANGUAGE OverloadedStrings #-}

import Data.Char
import Data.Text (pack, unpack, replace)

main = print . solve =<< readFile "day05.txt"

solve = length . converge removePairs

converge :: Eq a => (a -> a) -> a -> a
converge = until =<< ((==) =<<)

removePairs :: String -> String
removePairs x = foldl remove x pairs

pairs :: [String]
pairs = l ++ map reverse l where
    l = [[x, toUpper x] | x <- ['a'..'z']]

remove :: String -> String -> String
remove s p = unpack $ replace (pack p) "" (pack s)
