#Space for import if needed
#While drawing it out I found how I can make ticktactoe work on a single list. 
#The trick is at cell 1 of a 3by3 grid if you want to go down, add 3. 
#If you want to go down and left add 2, down right is 4. 
#For any N of grid. N by N down is add N, up is -N, down right is N+1 and so on.
#I'm reminded of some 2-d software is actully a 1D software with this clever method comment someone made.

def main():
    pass

def build_grid(cells):
    end_of_list=cells*cells
    i=0
    while i<end_of_list:
        pass

def win(signs_needed):
    pass

def draw():
    print("No one wins")

def move(sign, move, grid):
    pass

def victory_check(grid):
    pass


if __name__ == "__main__":
    main()
