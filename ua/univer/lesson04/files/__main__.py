def write_mas_to_file(mas, filename="mas.txt"):
    with open(filename, "w") as myfile:
        for value in mas:
            myfile.write(str(value))
            myfile.write("\n")

def write_mas_to_file_in_row(mas, filename="mas.txt"):
    with open(filename, "w") as myfile:
        for value in mas:
            myfile.write(str(value))
            myfile.write(" ")

def write_mas_to_csv_in_row(mas, filename="mas.csv"):
    with open(filename, "w") as myfile:
        for value in mas:
            myfile.write(str(value))
            myfile.write(";")

def read_mas_from_file(filename="mas.txt"):
    mas =[]
    with open(filename, "r") as myfile:
        for line in myfile:
            mas.append(int(line))
    return mas

def read_mas_from_file_in_row(filename="mas.txt"):
    mas =[]
    with open(filename, "r") as myfile:
        for line in myfile:
            words = line.strip().split(" ")
            for word in words:
                mas.append(int(word))
    return mas

def read_mas_from_csv_in_row(filename="mas.csv"):
    mas =[]
    with open(filename, "r") as myfile:
        for line in myfile:
            words = line.strip().split(";")
            for word in words:
                if word.isdigit():
                    mas.append(int(word))
    return mas

def write_matrix_to_file(matrix, filename ="matrix.txt"):
    with open(filename, "w") as myfile:
        for row in matrix:
            for cell in row:
                myfile.write(str(cell))
                myfile.write(" ")
            myfile.write("\n")


def read_matrix_from_file(filename ="matrix.txt"):
    matrix = []
    with open(filename, "r") as myfile:
        for line in myfile:
            row = []
            words = line.strip().split(" ")
            for word in words:
                row.append(int(word))
            matrix.append(row)
    return matrix

if __name__ == '__main__':
    mas = [1,2,3,4,5,6,6]
 #   write_mas_to_csv_in_row(mas,"mas_row.csv")
    mas1 = read_mas_from_csv_in_row("mas_row.csv")
    print(mas1)
 #   print(sum(mas1))
 #   print(sum(mas1)/len(mas1))
    matrix = [
        [1,1,1],
        [2,2,2]
    ]
    write_matrix_to_file(matrix)
    matrix1 = read_matrix_from_file()
    print(matrix1)