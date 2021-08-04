'''
    Project Name: Word Search Game
    Name: Zixi Zhong
    Purpose: This program searches for words in a list on a grid, both input into the
        program
'''


def read_lists():
    l = input()
    g = input()

    word_list = open(l).read().lower().split()

    grid_lines = open(g).readlines()
    grid = []
    for i in range(len(grid_lines)):
        inner_list = grid_lines[i].strip('\n').split()
        grid.append(inner_list)
        inner_list = []
    return word_list, grid



def search_helper(grid, word_list, possible):
    for i in range(len(grid)):
        for j in range(len(grid[i]) - 3):
            for k in range(3, len(grid[i]) + 1):
                letters = grid[i][j:j + k]
                word = ''.join(letters)
                if occurs_in(word, word_list):
                    possible.append(word)


    
def horizontal_right(grid, word_list, possible):
    for i in range(len(grid)):
        grid[i].reverse()
    search_helper(grid, word_list, possible)


    
def vertical_top(grid, word_list, possible):
    flipped_grid = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid)):
            row.append(grid[j][i])
        flipped_grid.append(row)
    search_helper(flipped_grid, word_list, possible)


def vertical_bottom(grid, word_list, possible):
    flipped_grid = []
    for i in range(len(grid)):
        word = []
        for j in range(len(grid)):
            word.append(grid[j][i])
        word.reverse()
        flipped_grid.append(word)
    search_helper(flipped_grid, word_list, possible)        


def diagonal(grid, word_list, possible):
    for i in range(len(grid)):
        grid[i].reverse()

    flip = []

    for i in range(len(grid) * 2 - 1):
        row = []
        for j in range((len(grid) - 1), -1, -1):
            if 0 <= i - j < len(grid):
                row.append(grid[i-j][j])
        flip.append(row)

    search_helper(flipped_grid, word_list, possible) 

    search_helper(flipped_grid, word_list, possible) 
   
   
def occurs_in(s, L):
    if s.lower() in L:
        return True
    return False


def print_words(possible):
    unique = set()
    for item in possible:
        unique.add(item)
    unique = sorted(unique)
    for word in unique:
        print(word)

    
def main():
    possible = []
    
    word_list, grid = read_lists()
    search_helper(grid, word_list, possible)
    horizontal_right(grid, word_list, possible)
    vertical_top(grid, word_list, possible)
    vertical_bottom(grid, word_list, possible)
    diagonal(grid, word_list, possible)

    print_words(possible)


main()