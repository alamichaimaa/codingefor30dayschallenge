import math


def encryption(s):
    # Write your code here
    length=math.sqrt(len(s))
    row=math.ceil(length)

    column =math.ceil(length)
    print(row, column)
    j=0
    matrix=[]
    for i in range(row):
        matrix.append(s[j:j+column])
        j+=column
    ls=[]
    for col in range(column):
        col_str=''
        for row in matrix:
            if col < len(row):
                col_str+=row[col]
        ls.append(col_str)

        
    print(' '.join(ls))
    print(matrix)
    
s='haveaniceday'

encryption(s)