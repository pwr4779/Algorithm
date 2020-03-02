
def hanoi(n, A, B, C):
    if (n == 1):
        move.append([A, C])
    else:
        hanoi(n - 1, A, C, B)
        move.append([A, C])
        hanoi(n - 1, B, A, C)


if __name__ == "__main__":
    n = int(input())
    move=[]
    hanoi(n, 1, 2, 3)
    print(len(move))
    for i in range(len(move)):
        print(str(move[i][0]) +" "+ str(move[i][1]))