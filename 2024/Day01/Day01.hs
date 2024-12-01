import System.IO
import Data.List

howMany :: Num a => (t -> Bool) -> [t] -> a
howMany p xs = sum [1 | x <- xs, p x]

main = do
  handle <- openFile "input.txt" ReadMode
  contents <- hGetContents handle
  let inputList = lines contents
-- Task 1 - Comparing the absolute differences between the 2 sorted list elements
  let list1 = sort [ read (head (words x)) :: Integer | x <- inputList]
  let list2 = sort [ read (last (words x)) :: Integer | x <- inputList]
  let distance = sum [ abs x | x <- zipWith (-) list1 list2]
--   print (list1)
--   print (list2)
--   print (distances)
  print distance

-- Task 2 - Calculating a "similarity score" - sum (list1 element * number of times appears in list2)
  let similarity = sum[ x * howMany (==x) list2 | x <- list1, x `elem` list2 ]
  print similarity

  hClose handle
