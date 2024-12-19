'''

There is a matrix with . and X, where X represents battleship, always of length 3. Battleship can be vertical or horizontal, never diagonal. Given a function bomb_at(i,j), returns True if battleship is present at (i,j) in the matrix. Print the head, middle, tail coordinates of the battleship.

I asked a question to clarify, and as it turns out there will always be one battleship.

.........
.....X...
.....X...
.....X...
.........

After seeing this question, guess what my well-trained monotonous mind thought the solution would be? Depth First Search. And I began writing the solution. I wrote a recursive solution.. in around 8 minutes. But the solution didn’t work because (i,j) was recursively calling (i+1,j),(i-1,j),(i,j+1),(i,j-1). And (i+1,j) will again call (i,j) internally.. leading to an infinite loop. One easy way to solve this is to manipulate original matrix, and replace X with . after its done.. but I do not have access to the matrix. So in the remaining 7 Minutes I started thinking about other solutions. But Time ran out while I was coding my other solution.

'''


def print_battleship(matrix):
    def bomb_at(i, j):
        return True if matrix[i][j] == 'X' else False
    
    rows, cols = len(matrix), len(matrix[0])

    coordinates = []

    for i in range(rows):
        for j in range(cols):
            if bomb_at(i, j):
                if bomb_at(i, j+1) and bomb_at(i, j+2):
                    # check right cells
                    coordinates = [ (i, j), (i, j+1), (i, j+2)]
                elif bomb_at(i+1, j) and bomb_at(i+2, j):
                    coordinates = [ (i, j), (i+1, j), (i+2, j)]
                break
    
    if coordinates:
        print(coordinates)

