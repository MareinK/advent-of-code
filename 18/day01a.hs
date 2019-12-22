import Text.Regex.PCRE

main = print . sum . map (read . (=~ "-?\\d+")) . lines =<< readFile "day01.txt"
