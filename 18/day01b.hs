import qualified Data.Set as Set
import Text.Regex.PCRE

main = print . firstdup . scanl (+) 0 . cycle . map (read . (=~ "-?\\d+")) . lines =<< readFile "day01.txt"

firstdup l = helper Set.empty l where
    helper seen (x:xs) = if Set.member x seen then x else helper (Set.insert x seen) xs
    helper seen []     = error "no duplicates"
