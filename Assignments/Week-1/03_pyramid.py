def pyramid_pattern(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "* " * (i + 1))

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    print("Pyramid Pattern:")
    pyramid_pattern(rows)
