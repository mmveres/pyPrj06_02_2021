if __name__ == '__main__':
    with open("text.txt","a") as myfile:
        myfile.write("\nhi people")

    with open("text.txt","r") as myfile:
        for line in myfile:
            print(line, end="")