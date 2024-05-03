from sudoku_utils import Sudoku
import random

fill_amount_start = 0
global to_fill
to_fill = 81
# def fill(fill_amount):
#     counter+=1
#     if fill_amount == to_fill: #Exit condition
#         print('#We are done', fill_amount)
#         return "oppleuren"#Void function
    
#     index = 81 - (to_fill-fill_amount)
#     possible_numbers = [1,2,3,4,5,6,7,8,9]
#     for num in possible_numbers:
#         if sudoku.is_valid(num,index):
#             sudoku.BOARD[index]=num
#             result = fill(fill_amount+1)
#             if result == "oppleuren":
#                 # print("hasteflats")
#                 return "oppleuren"
#         else:
#             pass #Waarom werkt het enigszins
#     #No numbers were valid
#     # print("Hello there")


# sudoku = Sudoku()
# sudoku.fill = fill

# if help:
#     s = [1,2,3,4,5,6,7,8,9,4,5,6,7,8,9,1,2,3,7,8,9,1,2,3,4,5,6,2,1,4,3]
#     sudoku.BOARD[:len(s)] = s
#     fill_amount_start = len(s)
# sudoku.show_BOARD()

# sudoku.fill(fill_amount=fill_amount_start)

# sudoku.show_BOARD()
times = []
import time
N = 20 #Number of sudokus to be generated
sudokus = []
times.append(time.time())
for k in range(N):
    print(f"Iteration {k+1} out of {N}")
    global counter
    counter=0
    sudoku = Sudoku()
    randstart = random.sample(range(1,10),9)
    print(randstart)
    sudoku.BOARD[:9] = randstart
    # sudoku.fill = fill
    sudoku.fill(fill_amount=9)
    sudokus.append(sudoku.BOARD)
    sudoku.show_BOARD()
    times.append(time.time())

print(sudokus)
with open("fresh_sudoku's.txt",'w') as outfile:
    for sudoku in sudokus:
        outfile.write(str(sudoku))
        outfile.write(',\n')

import matplotlib.pyplot as plt
import numpy as np
dt = np.diff(times)
print(np.mean(dt))
plt.figure()
plt.plot(dt,'.')
plt.show()