import random
# initializing the  variable
mat=[[0,0,0,0],
    [0,2,0,0],
    [0,0,0,0],
    [0,0,0,0]]

for matt in mat:
    print(matt)
def comp(mat):
    # this function return all the non zeros to the left side of the list
    new_mat = []
    for i in range(4):
            new_mat.append([0] * 4)

    for i in range(4):
        pos = 0
        for j in range(4):
            if(mat[i][j] != 0):

                new_mat[i][pos] = mat[i][j]
                if(j != pos):
                    changed = True
                pos += 1

    return new_mat

def add(mat):
    # this function check if to values at the consicative index
    #  and add them togather and return the added list'''
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                
    return mat
   
def rev(mat):
    # this function return the revarsed list
    new_mat =[[0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
    
    for i in range(4):
        for j in range(4):
            new_mat[i][j]=mat[i][3-j]
        
    return new_mat


def transp(mat):
    # this function return the transposed list 
    new__mat2=[[0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
    for i in range (4):
        for j in range(4):
            new__mat2[j][i]=mat[i][j]
    return new__mat2




def slide_up(mat):
    # return alist that can able to merge upward
    game = transp(mat)
    game=comp(game)
    game = add(game)
    game = comp(game)
    game = transp(game)
    return game

def slide_down(mat):
    # retuen alist that can able to merge downward
    
    game=transp(mat)
    
    game=rev(game)
    game=comp(game)
    game=add(game)
    game=comp(game)
    game=rev(game)
    game =transp(game)
    return game 
def slide_left(mat):
    # return alist that can merge to the left side 
    
    new_math=comp(mat)
    new_math = add(new_math)
    new_math=comp(new_math)
    
    return new_math
    
def slide_right(mat):
    # return alist that can merge to the right side
    
   
    game=rev(mat)
    
    game=comp(game)
    
    game=add(game)
    
    game=comp(game)
    
    game = rev(game)
    
    return game  

# finally this infite while loop makes the game to continue with out break
while True:
    # puting 2 at ranadom index
    a = random.randint(0, len(mat)-1)
    b = random.randint(0, len(mat)-1)
    if mat[a][b]==0:
        mat[a][b]=2
    elif mat[a][b]!=0:
        a = random.randint(0, len(mat)-1)
        b = random.randint(0, len(mat)-1)
        mat[a][b]=2
    # asking the user to enter as the code says
    x = input("""Press the command : 'u or U' for upward,
    'D or d' for down ward,
    'L or l'for left,
    'R or r for right""" )
    # calling the function slide_up if the user enter "u"
    # to perform the upward movement
    if (x=="u" or x=="U"):
        ma=slide_up(mat)
        mat = ma
        for matt in mat:
            print(matt)
    # calling the function slide_dewn if the user enter "d"
    # to perform the downward movement
    elif (x == 'D' or x == 'd'):
        ma=slide_down(mat)
        mat=ma
        for matt in mat:
            print(matt)
    # calling the function slide_dewn if the user enter "d"
    # to perform the downward movement
    elif(x == 'L' or x == 'l'):
        ma=slide_left(mat)
        mat=ma
        for matt in mat:
            print(matt)
    # calling the function slide_dewn if the user enter "d"
    # to perform the downward movement
    elif(x == 'R' or x == 'r'):
        ma=slide_right(mat)
        mat=ma
        for matt in mat:
            print(matt)
    # if the user incase enter wrong key it says wrong key entered
    else:
            print("invalid key entered ")
    continue
