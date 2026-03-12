def create_matrix(n):
    mat = [[0]*n for _ in range(n)]

    row_begin = 0
    col_begin = 0
    row_end = n-1
    col_end = n-1
    k=1
    while ((row_begin<=row_end) and (col_begin<=col_end)):
        for i in range(col_begin, col_end+1):
            mat[row_begin][i] = k
            k +=1
        row_begin +=1
        for i in range(row_begin, row_end+1):
            mat[i][col_end] = k
            k +=1
        col_end -=1
        if row_begin<=row_end:
            for i in range(col_end, col_begin-1, -1):
                mat[row_end][i] = k
                k +=1
            row_end -=1
        if col_begin <= col_end:
            for i in range(row_end, row_begin-1, -1):

                mat[i][col_begin] = k
                k += 1
            col_begin += 1
    print("2D List: ")
    print(mat)
    print("Matrix Format: ")
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ")
        print()



def main():
    n = int(input("Enter the value of n: "))
    create_matrix(n)

if __name__ == "__main__":
    main()