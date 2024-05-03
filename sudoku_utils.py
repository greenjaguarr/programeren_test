import numpy as np
class Sudoku():
    def __init__(self):
        # self.BOARD = np.zeros(81,dtype='int')
        self.BOARD = [0]*81
        self.BLOCK1= np.array([1,2,3,10,11,12,19,20,21]) #We gebruiken index beginnend bij 0
        self.BLOCK2= self.BLOCK1+3
        self.BLOCK3= self.BLOCK2+3
        self.BLOCK4= self.BLOCK1+27
        self.BLOCK5= self.BLOCK4+3
        self.BLOCK6= self.BLOCK5+3
        self.BLOCK7= self.BLOCK4+27
        self.BLOCK8= self.BLOCK7+3
        self.BLOCK9= self.BLOCK8+3
        self.BLOCKS = [self.BLOCK1,self.BLOCK2,self.BLOCK3,self.BLOCK4,self.BLOCK5,self.BLOCK6,self.BLOCK7,self.BLOCK8,self.BLOCK9]


# BLOCK_to_name = { BLOCK:str(j)for j,BLOCK in enumerate(BLOCKS)}
# print(BLOCK7)
    def test_BLOCKS(self):
        for i in range(1,82):
            i_is_found = False
            for BLOCK in self.BLOCKS:
                if i in BLOCK:
                    i_is_found = True
            if i_is_found == False:
                print("Something went wrong",i)

    # Make functions
    def show_BOARD(self):
        '''Properly turns 81 items long list to print'''
        for i in range(3):
            #Print3blocks
            for j in range(3):
                start= 27*i + 9*j
                stop = start + 9
                to_print = self.BOARD[start:stop]
                print(to_print)
            if not i==2:
                print('-----------------------------')
            else:
                print('-----------------------------')
                print('-----------------------------')


    def test_show_BOARD(self):
        self.BOARD[:5] = [1,2,3,4,5]
        self.show_BOARD(self.BOARD)

    def mask(self,i:int):
        masked_board = np.copy(self.BOARD)
        masked_board[i+1:] = 0
        return masked_board


    def which_BLOCK(self,i:int)->int:
        '''This function returns the BLOCK that i is in'''
        msd=(i)//27
        # lsd = (i-27*msd) // 9 
        lsd = ((i)%9)//3
        index = 3*msd + lsd + 1
        #Could also iterate through each block to look if index is there
        return index

    def test_which_BLOCK(self):
        indeces = np.linspace(0,80,81)
        results = self.which_BLOCK(indeces)
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
    def which_row(self,i:int)->int:
        return ((i) // 9) + 1

    def test_which_row(self):
        indeces = np.linspace(1,81,81)
        rows = self.which_row(indeces)
        for index,row in zip(indeces,rows):
            # print(index,row)
            if not (index - (row-1)*9) in range(10):
                print(f"Test which row didnt pass because {index} resulted in {row}")
                pass
        print("Test which column finished")

    def which_column(self,i:int)->int:
        return (i%9) + 1

    def test_which_column(self):
        indeces = np.linspace(0,80,81)
        columns = self.which_column(indeces)
        for index,column in zip(indeces,columns):
            # print(index,column, (index-column)/9)
            if not (index+1-column)/9 == (index+1-column)//9:
                print(f"Test which column didnt pass because {index} resulted in {column}")
        print("Test which column finished")

    def is_column_valid(self,num,i)->bool:
        column = self.which_column(i)
        indices = np.array([1,10,19,28,37,46,55,64,73]) + column - 2
        masked_board = self.mask(i)
        to_check = masked_board[indices]
        if num in to_check: return False
        else: return True

    def is_row_valid(self,num,i)->bool:
        row = self.which_row(i)
        indices = (row-1)*9 + np.array([1,2,3,4,5,6,6,7,8,9]) - 1
        masked_board = self.mask(i)
        to_check = masked_board[indices]
        if num in to_check: return False
        else: return True

    def is_block_valid(self,num,i)->bool:
        block_index = self.which_BLOCK(i)
        block = self.BLOCKS[block_index-1]
        masked_board = self.mask(i)
        to_check = masked_board[block-1]
        if num in to_check: return False
        else: return True


    def is_valid(self,num:int,i:int)->bool:
        '''This function tests is num can be places at place i in BOARD'''
        row_valid = self.is_row_valid(num,i)
        if not row_valid: return False
        block_valid = self.is_block_valid(num,i)
        if not block_valid: return False
        column_valid = self.is_column_valid(num,i)
        if not column_valid: return False
        return True


if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.test_which_BLOCK()
    sudoku.test_which_row()
    sudoku.test_which_column()