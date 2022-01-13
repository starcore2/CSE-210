#Space for import if needed
#While drawing it out I found how I can make ticktactoe work on a single list. 
#The trick is at cell 1 of a 3by3 grid if you want to go down, add 3. 
#If you want to go down and left add 2, down right is 4. 
#For any N of grid. N by N down is add N, up is -N, down right is N+1 and so on.
#I'm reminded of some 2-d software is actully a 1D software with this clever method comment someone made.

def main():
    print("Pick a grid size.")
    check =False
    false=False #I keep forgetting to captiliz false and true multiple times. This is to prevent that simple bug.
    true=True
    winner = False
    grid=emptyGrid
    while check != True:
        try:
            cells = int(input("Pick a number"))
            check = True
        except:
            print("the input encounter an error, Pick an INT number also known as a whole number.")
    grid = build_grid(cells)
    print("Player one will be X and player two will be O")
    expected_turns = cells*cells
    player_turn = 1
    check = False
    move_result = -1
    x=0
    y=0
    victory_check_start = expected_turns - cells
    while expected_turns > 0 and winner != True:
        print("Make a move")
        while y<cells:
            while x<cells:
                print("{}".format(grid[x+y*cells]), end='')
                x+=1
            print("")
            y+=1
            x=0
        y=0
        x=0
        while check != True:
            if player_turn = 1:
                player_turn = 0
                print("It's players X turn.")
                try:
                    grid=move(x,int(input("")),grid)
                    check = True
                except:
                    print("Error, try again player one.")
                    player_turn = 1
            elif player_turn = 0:
                player_turn =1
                print("It's players X turn.")
                try:
                    grid=move(x,int(input("")),grid)
                    check = True
                except:
                    print("Error, try again player one.")
                    player_turn = 0
            else:
                expected_turns = 0
                print("Turn error happened, ending game.")
        if expected_turns <= victory_check_start:
            if victory_check(grid,cells,emptyGrid) == -2:
                winner=True
        expected_turns-=1
        check = False
    if expected_turns == 0 and winner != True:
        draw()

def build_grid(cells):
    try:
        cells = int(cells)
    except TypeError:
        print("Invalid cell number type")
        return 0
    if cells < 1:
        print("That value is not going to work.")
        return 0
    end_of_list=cells*cells
    i=0
    grid = []
    while i<end_of_list:
        grid[i]=i+1
    return grid

def build_grid_edge(cells):
    try:
        cells = int(cells)
    except TypeError:
        print("Cell type error")
        return 0
    if cells < 1:
        print("That value is not going to work.")
        return 0
    square=cells*cells
    check = False
    edge=[1]
    edge+=cells
    edge+=cells*cells-cells
    edge+=cells*cells
    cell=cells
    i = 4
    c=1
    while check != True:
        i+=1
        if i > 10000:
            check = True
            print("Number was too big or unexpected error.")
        edge[i]+=cells+c
        edge[i+1]+=cells*c+cells
        edge[i+2]+=cells-(cells*c)
        edge[i+3]+=cells-c
        if edge[i]==edge[1] and edge[i+1] == edge[3] and edge[i+2] == edge[0] and edge[i+3] == edge[2]:
            edge.pop(i)
            edge.pop(i)
            edge.pop(i)
            edge.pop(i)
            check=True
            return edge
        elif edge[i]==edge[1] or edge[i+1] == edge[3] or edge[i+2] == edge[0] or edge[i+3] == edge[2]:
            print("Unexpected equal edge.")
        else:
            c+=1

def win(signs_needed):
    print(signs_needed+" has won.")

def draw():
    print("No one wins")

def move(sign, move, grid):
    #Valid Move checker.
    if grid.count(move)<=0:
        print("Invalid move")
        return -1
    grid[move-1] = sign
    return grid
def victory_check(grid, cells, emptyGrid):
    i=0
    k=0
    win = 0
    not_empty = 0
    target = cells
    cell=cells
    symol_check = 0
    e=[]
    f=0
    #edge=[1] 1,                       0
    #edge+=cells last,                 1
    #edge+=cells*cells-cells under 1,  2
    #edge+=cells*cells under last,     3
    if cells%2==0:
        while i<target: #This searches the rows
            while k < target:
                if grid[k+i*cells] != emptyGrid[k+i*cells]:
                    not_empty+=1
                    e+=grid[k+i*cells]
                k+=1
            if not_empty == cells:
                e[0]=symol_check
                while f<target:
                    if e[f] != symol_check:
                        f=target
                    elif grid[f]==cells and e[f] == symol_check:
                        win(symol_check)
                        return -2
                    else: 
                        f+=1
                f=0        
            i+=1
            k=0
            e=[]
        while i<target: #This should search the collumns
            while k < target:
                if grid[k*cells+i] != emptyGrid[k*cells+i]:
                    not_empty+=1
                    e+=grid
                k+=1
            if not_empty == cells:
                e[0]=symol_check
                while f<target:
                    if e[f] != symol_check:
                        f=target
                    elif grid[f]==cells and e[f] == symol_check:
                        win(symol_check)
                        return -2
                    else: 
                        f+=1
                f=0        
            i+=1
            k=0
            e=[]
        i=0
        k=0
    else:
        while i<target: #This searches the rows
            while k < target:
                if grid[k+i*cells] != emptyGrid[k+i*cells]:
                    not_empty+=1
                    e+=grid[k+i*cells]
                k+=1
            if not_empty == cells:
                e[0]=symol_check
                while f<target:
                    if e[f] != symol_check:
                        f=target
                    elif grid[f]==cells and e[f] == symol_check:
                        win(symol_check)
                        return -2
                    else: 
                        f+=1
                f=0        
            i+=1
            k=0
            e=[]
        while i<target: #This should search the collumns
            while k < target:
                if grid[k*cells+i] != emptyGrid[k*cells+i]:
                    not_empty+=1
                    e+=grid
                k+=1
            if not_empty == cells:
                e[0]=symol_check
                while f<target:
                    if e[f] != symol_check:
                        f=target
                    elif grid[f]==cells and e[f] == symol_check:
                        win(symol_check)
                        return -2
                    else: 
                        f+=1
                f=0        
            i+=1
            k=0
            e=[]
        i=0
        k=0
        cross=0
        e=[]
        while i<target:
            e+=grid[(cells+1)*i]
        symol_check = e[0]
        if e.count(symol_check)==4:
            win(symol_check)
        i=0
        e=[]
        while i<target:
            k=cells*cells-cells
            e+=grid[k-(cells-1)*i]
        symol_check = e[0]
        if e.count(symol_check)==4:
            win(symol_check)


        


if __name__ == "__main__":
    main()
