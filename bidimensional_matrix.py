from copy import copy


def msum(arr, arr1):
    arraysum = []
    try:
        for i in range(len(arr)):
            arraysum.append([x + y for x, y in zip(arr[i], arr1[i])])
    except IndexError:
        print("Matrix needs to be a squared one!")

    return arraysum


def tr(arr):
    accum = 0
    j = 0

    try:
        for i in range(len(arr)):
            accum += arr[i][j]
            j += 1
    except IndexError:
        print("Matrix needs to be a bidimensional one.")

    return accum


def transpose(arr):
    temp = []
    array = []

    try:
        for i in range(len(arr[0])):
            for j in range(len(arr)):
                temp.append(arr[j][i])
            array.append(copy(temp))
            temp.clear()
    except IndexError:
        print("Matrix needs to be a bidimensional one.")

    return array


def dotproduct(arr, arr1):
    temp = []
    array = []

    try:
        m = len(arr)
        n = len(arr[0])
        m1 = len(arr1)
        n1 = len(arr1[0])

        print("First array dimensions(m, n): ", (m, n))
        print("Second array dimensions(m, n): ", (m1, n1))

        if m == n1 and n == m1:
            for i in range(m):
                temp.clear()
                for k in range(m):
                    accum = 0
                    for j in range(n):
                        accum += arr[i][j] * arr1[j][k]
                    temp.append(accum)
                array.append(copy(temp))

        elif n == m1:
            for i in range(m):
                temp.clear()
                for k in range(m1):
                    accum = 0
                    for j in range(n):
                        accum += arr[i][j] * arr1[j][k]
                    temp.append(accum)
                array.append(copy(temp))

        elif n1 == m:
            for i in range(m1):
                temp.clear()
                for k in range(m):
                    accum = 0
                    for j in range(n1):
                        accum += arr1[i][j] * arr[j][k]
                    temp.append(accum)
                array.append(copy(temp))

        else:
            raise ValueError("The number of columns in the first matrix must be equal of rows in the second matrix.")

    except IndexError as e:
        print("Error: ", e)

    return array


A = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

# Note that B is a identity matrix.
B = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# Note that C is a simetric matrix, in other words, C^T = C
C = [
    [4, 3, -1],
    [3, 2, 0],
    [-1, 0, 5]
]

# D is a anti-simetric matrix, D^T = -D
D = [
    [0, -3, 1],
    [3, 0, -7],
    [-1, 7, 0]
]

E = [
    [10, 20],
    [50, 60]
]

F = [
    [70, 80]
]

print("Matrix sum A+B = ", *msum(A, B), sep='\n')
print()
print("Trace of A = ", tr(A))
print()
print("Transposed matrix of A", *transpose(A), sep='\n')
print()
print("Simetric transposed matrix of C that's = C", *transpose(C), sep='\n')
print()
print("Anti-simetric transposed matrix of D that's = -D", *transpose(D), sep='\n')
print()
print("Dot product of E and F = ", *dotproduct(E, F), sep='\n')
print()
print("Dot product of A and B = ", *dotproduct(A, B), sep='\n')
