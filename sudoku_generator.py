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
    return index

def test_which_BLOCK():
    indeces = np.linspace(1,81,81)
    results = which_BLOCK(indeces)
    show_BOARD(results)

def is_row_valid(num):
    row = which_row()

def is_column_valid(num):
    column = which_column()

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





# test_which_BLOCK()