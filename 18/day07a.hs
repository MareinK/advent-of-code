import Data.List (sort)
import qualified Data.Map as Map
import Data.Maybe (fromMaybe)
import Text.Regex.TDFA ((=~))

type NodeEdges a = (a, [a])
type Graph a = Map.Map a [a]

main = print . solve . parse =<< readFile "day07.txt"

parse :: String -> Graph String
parse = Map.fromListWith (++) . map parseLine . lines

parseLine :: String -> NodeEdges String
parseLine = (\[k,v] -> (k, [v])) . map last . (=~ " ([A-Z]) ")
    
solve :: Graph String -> String
solve g = concat $ path g [] (sort $ roots g)

path :: Ord a => Graph a -> [a] -> [a] -> [a]
path g s (x:xs) = x:(path g seen frontier) where
    seen = x:s
    frontier = sort $ filter (\x -> (not $ wasSeen x) && parentsSeen x) (children g x ++ xs)
    wasSeen = flip elem seen
    parentsSeen = all wasSeen . parents g
path g s [] = []

roots :: Ord a => Graph a -> [a]
roots g = filter (null . parents g) (Map.keys g)

children :: Ord a => Graph a -> a -> [a]
children g k = fromMaybe [] (Map.lookup k g)

parents :: Ord a => Graph a -> a -> [a]
parents g k = filter (elem k . children g) (Map.keys g)
