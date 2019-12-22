import Data.Char (ord)
import Data.List (union, (\\))
import qualified Data.Map as Map
import Data.Maybe (fromMaybe)
import Text.Regex.TDFA ((=~))

type NodeEdges a = (a, [a])
type Graph a = Map.Map a [a]
type Workers a = Map.Map a Int

nWorkers = 5
stepTime = 60

main = print . solve . parse =<< readFile "day07.txt"

parse :: String -> Graph String
parse = addEmptyNodes . Map.fromListWith (++) . map parseLine . lines

parseLine :: String -> NodeEdges String
parseLine = (\[k,v] -> (k, [v])) . map last . (=~ " ([A-Z]) ")

addEmptyNodes :: Ord a => Graph a -> Graph a
addEmptyNodes g = Map.union g (Map.fromList [(k,[]) | k <- concat $ Map.elems g])

solve :: Graph String -> Int
solve g = time nWorkers g Map.empty

time :: Int -> Graph String -> Workers String -> Int
time n g ws
    | itemsCompleted == Map.keys g = 0
    | otherwise = 1 + time n g updateWorkers
    where
        nIdle = n - (length $ filter (> 0) $ Map.elems ws)
        itemsSatisfied = filter (all (flip elem itemsCompleted) . parents g) (Map.keys g)
        itemsCompleted = Map.keys $ Map.filter (<= 0) ws
        nextItems = take nIdle (itemsSatisfied \\ Map.keys ws)
        updateWorkers = Map.map (subtract 1) $ Map.union ws $ Map.fromList $ map startWorker nextItems
        startWorker x = (x, stepTime + ord (head x) - 64)

children :: Ord a => Graph a -> a -> [a]
children g k = fromMaybe [] (Map.lookup k g)

parents :: Ord a => Graph a -> a -> [a]
parents g k = filter (elem k . children g) (Map.keys g)
