{-# LANGUAGE OverloadedStrings #-}

import Data.Char
import Data.Text (pack, unpack, replace)
import Debug.Trace

main = print . solve =<< readFile "day05.txt"

solve x = minimum $ map (length . flip improve x) ['a'..'z']

improve :: Char -> String -> String
improve x = converge removePairs . remove ([toUpper x]) . remove [x] . trace ("improve " ++ [x])

converge :: Eq a => (a -> a) -> a -> a
converge = until =<< ((==) =<<)

removePairs :: String -> String
removePairs x = foldl (flip remove) x pairs

pairs :: [String]
pairs = l ++ map reverse l where
    l = [[x, toUpper x] | x <- ['a'..'z']]

remove :: String -> String -> String
remove p s = unpack $ replace (pack p) "" (pack s)
