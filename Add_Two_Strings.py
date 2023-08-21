def addBinary(A, B):
    if len(A) > len(B):
        return addBinary(B, A)

    diff = len(B) - len(A)
    padding = '0' * diff
    A = padding + A
    res = ''
    carry = '0'

    for i in range(len(A) - 1, -1, -1):
        if A[i] == '1' and B[i] == '1':
            if carry == '1':
                res = '1' + res
                carry = '1'
            else:
                res = '0' + res
                carry = '1'
        elif A[i] == '0' and B[i] == '0':
            if carry == '1':
                res = '1' + res
                carry = '0'
            else:
                res = '0' + res
                carry = '0'
        elif A[i] != B[i]:
            if carry == '1':
                res = '0' + res
                carry = '1'
            else:
                res = '1' + res
                carry = '0'

    if carry == '1':
        res = carry + res

    # To remove leading zeroes
    index = 0
    while index + 1 < len(res) and res[index] == '0':
        index += 1
    return res[index:]

# Driver code
def main():
    a = "1101"
    b = "100"
    print(addBinary(a, b))

if __name__ == "__main__":
    main()
