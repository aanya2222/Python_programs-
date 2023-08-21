def main():
    n = 5

    # Upper Triangle
    for rows in range(1, n + 1):
        # Print leading spaces
        for columns in range(n, rows, -1):
            print(" ", end="")

        # Print the first asterisk
        print("*", end="")

        # Print spaces between asterisks
        for columns in range(1, (rows - 1) * 2 + 1):
            print(" ", end="")

        # Print the last asterisk and move to the next line
        if rows == 1:
            print()
        else:
            print("*")

    # Lower Triangle
    for rows in range(n - 1, 0, -1):
        # Print leading spaces
        for columns in range(n, rows, -1):
            print(" ", end="")

        # Print the first asterisk
        print("*", end="")

        # Print spaces between asterisks
        for columns in range(1, (rows - 1) * 2 + 1):
            print(" ", end="")

        # Print the last asterisk and move to the next line
        if rows == 1:
            print()
        else:
            print("*")

if __name__ == "__main__":
    main()
