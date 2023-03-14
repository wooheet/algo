# In the popular game of Bingo, a player has a card represented by a matrix mat of size (n x m) that contains all of the numbers from the range 1 to (n x m).
#
# The numbers are called out from an array arr of all the numbers from 1 to (n x m) in sequential order starting from the first element. When a number is called out, the player marks the corresponding number on the game card.
#
# Find the first number in the sequence at which either a row or a column is completely marked.
#
# Example
# Let, mat=[[3,1,8],[4,6,2],[7,5,9]] and arr = [5,4,8,7,6,1,9,2,3]
#
# The 2nd column is completely marked after 1 is called. Return 1.
#
#
#
# Function Description
# Completed the function getBingoNumber in the editor
#
# The function getBingoNumber has the following parameters:
# - int mat[n][m]: the bingo card
# - int arr[n*m]: the numbers in the order they are called
#
# Return
# int: the first number at which either a row or a column is completely marked
#
#
# Constraints
#
# 1 <= n*m <= 10^6
# 1 <= mat[n][m] <= n*m
# 1 <= arr[n*m] <= n*m
# Every element occurs exactly once in matrix mat and array arr.
#
#
#
# sample input 1:
#
#
# STDIN        FUNCTION
# 3       ->   mat[] size n = 3
# 2       ->   mat[] size m = 2
# 1 6     ->   mat = [[1,6],[2,4],[5,3]]
# 2 4
# 5 3
# 6       ->   k = n*m = 6
# 2       ->   arr = [2,4,3,1,5,6]
# 4
# 3
# 1
# 5
# 6
#
#
# sample output 1:
# 4
#
#
#
# Explanation
# Here, n=3, m=2
# mat = [[1,6],[2,4],[5,3]]
# arr = [2,4,3,1,5,6]
#
# When 4 is Called, the second row is completed.
#
#
#
#
# sample input 2:
#
#
# STDIN        FUNCTION
# 2       ->   mat[] size n = 2
# 3       ->   mat[] size m = 3
# 2 4 6     ->   mat = [[2,4,6],[5,1,3]]
# 5 1 3
# 6       ->   value of k = n*m = 6
# 2       ->   arr = [2,1,3,5,6,4]
# 1
# 3
# 5
# 6
# 4
#
#
# sample output 2:
# 5




