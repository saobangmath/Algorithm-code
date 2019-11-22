def check(r):
    for i in r:
        if (i==-1):
            return False
    return True
# sorted by increasing order with first element then decreasing order with second element
def key(x):
    return (x[0], ~x[1])

def check_valid(b):
    for e in b:
        if check(e) and (sum(e)/4) not in e:
            return False
    for i in range(4):
        c = [e[i] for e in b]
        if check(c) and (sum(c)/4) not in c:
            return False
    return True

def show(board):
    for i in range(4):
        for j in range(4):
            print(board[i][j],end=" ")
        print("\n")

    print("##########")
board=[[-1 for i in range(4)] for j in range(4)]
mark=[False for i in range(16)]

# backtracking algorithm 
# the algorithm might need some optimizations for other big value of square length ( in this case is just 4)
def backtrack(board,r,c):
    if (r==4):
        if (board not in res):
            show(board)
    else:
        if (c == 3):
            for num in range(16):
                if(not mark[num]):
                    board[r][c] = num
                    if (check_valid(board)):
                        mark[num] = True
                        backtrack(board,r+1,0)
                        mark[num] = False
                    board[r][c]=-1

        else:
            for num in range(16):
                if(not mark[num]):
                    board[r][c] = num
                    if (check_valid(board)):
                        mark[num] = True
                        backtrack(board,r,c+1)
                        mark[num] = False
                    board[r][c]=-1

backtrack(board,0,0)

