def upper_triangular_pattern(rows):
    for i in range(rows):
        for j in range(rows):
            if j < i:
                print(' ', end=' ')
            else:
                print('*', end=' ')
        print()

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    print("Upper Triangular Pattern:")
    upper_triangular_pattern(rows)
