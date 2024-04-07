import random
def start_game():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat

def add_new_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while mat[r][c]!=0:
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2

def get_curent_status(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return 'WON'
    for i in range(3):
        if (mat[3][i]==mat[3][i+1]) or (mat[i][3]==mat[i+1][3]):
            return 'NOT OVER'
        for j in range(3):
            if (mat[i][j]==mat[i+1][j]) or (mat[i][j]==mat[i][j+1]):
                return 'NOT OVER'
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return 'NOT OVER'
    return 'LOST'
def compress(mat):
    changed=False
    new_mat=[]
    for i in range(4):
        new_mat.append([0]*4)
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]
                if j!=pos:
                    changed=True
                pos+=1
    return new_mat,changed

def merge(mat):
    changed=False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                mat[i][j]=mat[i][j]*2
                mat[i][j+1]=0
                changed=True
    return mat,changed
                
def reverse(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    return new_mat

def transpose(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat
    

def move_left(grid):
    prev_grid=grid.copy()
    new_grid,change1=compress(grid)
    new_grid,change2=merge(new_grid)
    changed=change1 or change2
    new_grid,temp=compress(new_grid)
    return new_grid,changed

def move_right(grid):
    prev_grid=grid.copy()
    new_grid=reverse(grid)
    new_grid,change1=compress(new_grid)
    new_grid,change2=merge(new_grid)
    changed=change1 or change2
    new_grid,temp=compress(new_grid)
    new_grid=reverse(new_grid)
    return new_grid,changed
    
def move_up(grid):
    prev_grid=grid.copy()
    new_grid=transpose(grid)
    new_grid,change1=compress(new_grid)
    new_grid,change2=merge(new_grid)
    changed=change1 or change2
    new_grid,temp=compress(new_grid)
    new_grid=transpose(new_grid)
    return new_grid,changed
    
def move_down(grid):
    prev_grid=grid.copy()
    new_grid=transpose(grid)
    new_grid=reverse(new_grid)
    new_grid,change1=compress(new_grid)
    new_grid,change2=merge(new_grid)
    changed=change1 or change2
    new_grid,temp=compress(new_grid)
    new_grid=reverse(new_grid)
    new_grid=transpose(new_grid)
    return new_grid,changed
    
