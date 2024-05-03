from sudoku_utils import Sudoku

fill_amount_start = 0
to_fill = 81
def fill(fill_amount):
    if fill_amount == to_fill: #Exit condition
        print('#We are done', fill_amount)
        return "oppleuren"#Void function
    
    index = 81 - (to_fill-fill_amount)
    possible_numbers = [1,2,3,4,5,6,7,8,9]
    for num in possible_numbers:
        if sudoku.is_valid(num,index):
            sudoku.BOARD[index]=num
            result = fill(fill_amount+1)
            if result == "oppleuren":
                # print("hasteflats")
                return "oppleuren"
        else:
            pass #Waarom werkt het enigszins
    #No numbers were valid
    # print("Hello there")
    if fill_amount<9:
        print("whoopsieeee")
help = False

    
    

sudoku = Sudoku()
sudoku.fill = fill

if help:
    s = [1,2,3,4,5,6,7,8,9,4,5,6,7,8,9,1,2,3,7,8,9,1,2,3,4,5,6,2,1,4,3]
    sudoku.BOARD[:len(s)] = s
    fill_amount_start = len(s)
sudoku.show_BOARD()

sudoku.fill(fill_amount=fill_amount_start)

sudoku.show_BOARD()