def lower_triangular_pattern(rows):
    for i in range(rows):
        line = ''
        for j in range(i + 1):
            line += '* '
        print(line)

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    print("Lower Triangular Pattern:")
    lower_triangular_pattern(rows)