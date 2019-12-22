import Control.Monad
import Data.Function
import Data.List
import Data.List.Split
import qualified Data.Map as Map
import Data.Map ((!))
import Data.Maybe
import Text.Regex.PCRE

type SleepTimes    = [(Int,Int)]
type GuardSleepMap = Map.Map Int SleepTimes

main = print . solve . parse =<< readFile "day04.txt"

parse :: String -> GuardSleepMap
parse = Map.map sort . Map.fromListWith (++) . map parseGuard . splitGuards . sort . lines where
    splitGuards :: [String] -> [[String]]
    splitGuards = split (dropInitBlank $ keepDelimsL $ whenElt (isInfixOf "Guard"))
    parseGuard :: [String] -> (Int, SleepTimes)
    parseGuard (x:xs) = (read $ tail $ x =~ "#\\d+", parseTimes xs)
    parseGuard []     = (-1, [])
    parseTimes :: [String] -> SleepTimes
    parseTimes = map ((\(x:y:_) -> (x,y)) . map (read . tail . (=~ ":\\d+"))) . chunksOf 2

solve :: GuardSleepMap -> Int
solve m = gid * min  where
    gid = mostsleepguard m
    min = mostsleepminute (m ! gid)
    mostsleepguard :: GuardSleepMap -> Int
    mostsleepguard = snd . fromJust . Map.lookupMax . invertmap . Map.map (sum . map (uncurry subtract))
    mostsleepminute :: SleepTimes -> Int
    mostsleepminute = mostcommon . concat . map (\(x,y) -> [x..y-1])

invertmap :: Ord b => Map.Map a b -> Map.Map b a
invertmap = Map.foldrWithKey (flip Map.insert) Map.empty

mostcommon :: Ord a => [a] -> a
mostcommon = head . maximumBy (compare `on` length) . group . sort
