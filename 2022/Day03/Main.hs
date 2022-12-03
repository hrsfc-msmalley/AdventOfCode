import System.IO
import Data.List
import Data.Tuple
import Data.Map (Map)
import qualified Data.Map as Map
import Data.Maybe


-- Build list of key value pairs for a-Z 1-52
alphabet = ['a'..'z']++['A'..'Z']
numbers = [1..52]
pairs = Map.fromList(zip alphabet numbers)

-- Function to get the value for a single character (but annoyingly returned as a list)
getValue :: [Char] -> Int
getValue x = fromJust(Map.lookup (head x) pairs)

-- Task 1: Chunks a list into 2 equal parts, returned as a tuple of 2 lists
halveList :: [a] -> ([a],[a])
halveList xs = ((take s xs), (drop s xs)) where s = div (length xs) 2

-- Task 1: checks the unique intersections of 2 list halves, taking the list as its input
intersectionListHalves :: (Eq a) => [a] -> [a]
intersectionListHalves xs = intersect (nub (fst(halveList xs))) (nub (snd(halveList xs)))

-- Task 2: chunks list into groups of 3
chunk3 :: [a] -> [[a]]
chunk3 xs
  | 3 <= length xs = take 3 xs:(chunk3 (drop 3 xs))
  | otherwise = []

-- Task 2: finds unique intersectinos of 3 lists, taking the list of lists as input
intersection3Lists :: (Eq a) => [[a]] -> [a]
intersection3Lists xss = foldl1 intersect xss

main = do
  handle <- openFile "input.txt" ReadMode
  contents <- hGetContents handle
  -- Task 1
  let outputIntersections = map intersectionListHalves (lines contents)
  let outputValues = map getValue outputIntersections
  print (sum outputValues)
  -- Task 2
  let outputGroups = chunk3 (lines contents)
  let outputGroupIntersections = map intersection3Lists outputGroups
  let outputGroupValues = map getValue outputGroupIntersections
  print (sum outputGroupValues)
  hClose handle
