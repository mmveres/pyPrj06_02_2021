def print_vector():
    my_arr = [1, 2, 3, 4, 9, 5]
    for item in my_arr:
        print(item, end=", ")
    print()


def print_vector_by_index():
    my_arr = [1, 2, 3, 4, 9, 5]
    for i in range(len(my_arr)):
        print("arr[", i, "]=", my_arr[i])


def print_sum_matrix(matrix):
    sum_matrix = 0
    sum_row_list = []
    for row in matrix:
        print("**************")
        sum_row = 0
        for cell in row:
            sum_row += cell
            print(cell, end="\t")
        print(" = ", sum_row)
        sum_matrix += sum_row
        sum_row_list.append(sum_row)
    print("**************")
    print(sum_matrix)
    print(sum_row_list)


def print_diag_matrix(matrix):
    print(len(matrix))
    print(len(matrix[0]))
    print(len(matrix[1]))
    print(len(matrix[2]))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                print(matrix[i][j], end='\t')
            else:
                print("*", end='\t')
        print()


def print_matrix(matrix):
    for row in matrix:
        for cell in row:
            print(cell, end="\t")
        print()


if __name__ == '__main__':
    matrix = [
        [1,1,1],
        [2,2,2],
        [3,3,3]
    ]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i<j:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] =temp

    print_matrix(matrix)