with open("fresh_sudoku's.txt",'r') as infile:
    sudokus = infile.read()
print(type(sudokus))
sudokus = sudokus.split(sep=',\n') #This is the chosed delimiter
print(type(sudokus))
print(sudokus[:3])
if sudokus[-1] == '':
    sudokus = sudokus[:-1] #There is a useless last part
print(sudokus[:3])
def parse(sudoku:str):
    res = [int(i) for i in sudoku if i.isdigit()]
    return res
new_sudokus=[]
for sudoku in sudokus:
    new_sudokus.append(parse(sudoku))
print(len(new_sudokus[0]))


