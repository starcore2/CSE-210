#Space for import if needed
#While drawing it out I found how I can make ticktactoe work on a single list. 
#The trick is at cell 1 of a 3by3 grid if you want to go down, add 3. 
#If you want to go down and left add 2, down right is 4. 
#For any N of grid. N by N down is add N, up is -N, down right is N+1 and so on.
#I'm reminded of some 2-d software is actully a 1D software with this clever method comment someone made.

def main():
    pass

def build_grid(cells):
    try:
        cells = int(cells)
    except TypeError:
        print("Invalid cell number type")
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
    square=cells*cells
    check = False
    edge=[1]
    edge+=cells
    edge+=cells*cells-cells
    edge+=cells*cells
    i = 0
    while check != True:
        i+=1
        if i > 10000:
            check = True
            print("Number was too big or unexpected error.")
        

def win(signs_needed, win_count):
    x=signs_needed+" has won"
    if win_count>1:
        x+=" by {} lines.".format(win_count)
    else:
        x+="."
    print(x)

def draw():
    print("No one wins")

def move(sign, move, grid):
    pass

def victory_check(grid, edgegrid):
    pass


if __name__ == "__main__":
    main()
