def remove_duplicate(s):
    index = 0
    c = list(s)
    for i in range(len(c)):
        for j in range(i):
            if c[i] == c[j]:
                break
        if i == j:
            c[index] = c[i]
            index += 1
    return ''.join(c[:index])

def remove_white_space(ch, key):
    c = list(key)
    for i in range(len(c)):
        for j in range(len(ch)):
            if c[i] == ch[j]:
                c[i] = ' '
    key = ''.join(c)
    key = key.replace(" ", "")
    return key

def make_pair(pt):
    s = ""
    c = 'a'
    for i in range(len(pt)):
        if pt[i] == ' ':
            continue
        else:
            c = pt[i]
            s += pt[i]
        if i < len(pt) - 1:
            if pt[i] == pt[i + 1]:
                s += "x"
    if len(s) % 2 != 0:
        s += "x"
    print(s)
    return s

def find_ij(a, b, x):
    y = [0] * 4
    if a == 'j':
        a = 'i'
    elif b == 'j':
        b = 'i'
    for i in range(5):
        for j in range(5):
            if x[i][j] == a:
                y[0] = i
                y[1] = j
            elif x[i][j] == b:
                y[2] = i
                y[3] = j
    if y[0] == y[2]:
        y[1] += 1
        y[3] += 1
    elif y[1] == y[3]:
        y[0] += 1
        y[2] += 1
    for i in range(4):
        y[i] %= 5
    return y

def encrypt(pt, x):
    ch = list(pt)
    a = [0] * 4
    i = 0
    while i < len(pt):
        if i < len(pt) - 1:
            a = find_ij(pt[i], pt[i + 1], x)
            if a[0] == a[2]:
                ch[i] = x[a[0]][a[1]]
                ch[i + 1] = x[a[0]][a[3]]
            elif a[1] == a[3]:
                ch[i] = x[a[0]][a[1]]
                ch[i + 1] = x[a[2]][a[1]]
            else:
                ch[i] = x[a[0]][a[3]]
                ch[i + 1] = x[a[2]][a[1]]
        i += 2
    pt = ''.join(ch)
    return pt

# Main driver method
def main():
    pt = "instruments"
    key = "monarchy"
    
    key = remove_duplicate(key)
    ch = list(key)
    st = "abcdefghiklmnopqrstuvwxyz"
    st = remove_white_space(ch, st)
    c = list(st)
    
    x = [[' ' for _ in range(5)] for _ in range(5)]
    index_of_st = 0
    index_of_key = 0
    
    for i in range(5):
        for j in range(5):
            if index_of_key < len(key):
                x[i][j] = ch[index_of_key]
                index_of_key += 1
            else:
                x[i][j] = c[index_of_st]
                index_of_st += 1
    
    for i in range(5):
        print(' '.join(x[i]))
    
    pt = make_pair(pt)
    pt = encrypt(pt, x)
    
    print(pt)

if __name__ == "__main__":
    main()
