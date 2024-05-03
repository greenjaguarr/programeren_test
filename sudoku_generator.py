import numpy as np
BOARD = np.zeros(81,dtype='int')
BLOCK1= np.array([1,2,3,10,11,12,19,20,21])
BLOCK2= BLOCK1+3
BLOCK3= BLOCK2+3
BLOCK4= BLOCK1+27
BLOCK5= BLOCK4+3
BLOCK6= BLOCK5+3
BLOCK7= BLOCK4+27
BLOCK8= BLOCK7+3
BLOCK9= BLOCK8+3
BLOCKS = [BLOCK1,BLOCK2,BLOCK3,BLOCK4,BLOCK5,BLOCK6,BLOCK7,BLOCK8,BLOCK9]
# BLOCK_to_name = { BLOCK:str(j)for j,BLOCK in enumerate(BLOCKS)}
# print(BLOCK7)
def test_BLOCKS():
    for i in range(1,82):
        i_is_found = False
        for BLOCK in BLOCKS:
            if i in BLOCK:
                i_is_found = True
        if i_is_found == False:
            print("Something went wrong",i)

# Make functions
def show_BOARD(local_BOARD):
    '''Properly turns 81 items long list to print'''
    for i in range(3):
        #Print3blocks
        for j in range(3):
            start= 27*i + 9*j
            stop = start + 9
            to_print = local_BOARD[start:stop]
            print(to_print)
        if not i==2:
            print('-----------------------------')

def test_show_BOARD():
    BOARD[:5] = [1,2,3,4,5]
    show_BOARD(BOARD)


def which_BLOCK(i:int)->int:
    '''This function returns the BLOCK that i is in'''
    msd=(i-1)//27
    # lsd = (i-27*msd) // 9 
    lsd = ((i-1)%9)//3
    index = 3*msd + lsd + 1
    #Could also iterate through each block to look if index is there
    return index

def test_which_BLOCK():
    indeces = np.linspace(1,81,81)
    results = which_BLOCK(indeces)
    # print(results)
    # show_BOARD(results)
    expected_results=[1,1,1,2,2,2,3,3,3,
                      1,1,1,2,2,2,3,3,3,
                      1,1,1,2,2,2,3,3,3,
                      4,4,4,5,5,5,6,6,6,
                      4,4,4,5,5,5,6,6,6,
                      4,4,4,5,5,5,6,6,6,
                      7,7,7,8,8,8,9,9,9,
                      7,7,7,8,8,8,9,9,9,
                      7,7,7,8,8,8,9,9,9]
    for result,expected_result in zip(results,expected_results):
        if not result==expected_result:
            print("Test which block failed.")
    print("Test which block finished")
def which_row(i:int)->int:
    return ((i-1) // 9) + 1

def test_which_row():
    indeces = np.linspace(1,81,81)
    rows = which_row(indeces)
    for index,row in zip(indeces,rows):
        # print(index,row)
        if not (index - (row-1)*9) in range(10):
            print(f"Test which row didnt pass because {index} resulted in {row}")
            pass
    print("Test which column finished")

def which_column(i:int)->int:
    return ((i-1)%9) + 1

def test_which_column():
    indeces = np.linspace(1,81,81)
    columns = which_column(indeces)
    for index,column in zip(indeces,columns):
        # print(index,column, (index-column)/9)
        if not (index-column)/9 == (index-column)//9:
            print(f"Test which column didnt pass because {index} resulted in {column}")
    print("Test which column finished")

def is_column_valid(num):
    column = which_column()
    pass

def is_row_valid(num):
    row = which_row()
    pass

def is_block_valid(num):
    block = which_BLOCK()

def is_valid(BOARD,num:int,i:int)->bool:
    '''This function tests is num can be places at place i in BOARD'''
    row_valid = is_row_valid()
    if not row_valid: return False
    block_valid = is_block_valid()
    if not block_valid: return False
    column_valid = is_column_valid()
    if not column_valid: return False
    return True


test_which_BLOCK()
test_which_column()
test_which_row()