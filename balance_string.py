def solve(A):
    if (A.count('0') == A.count('1')):
        return (len(A))
    else:
        if (A.count("0") > A.count("1")):
            Gap = A.count("1") * 2 + 1
        else:
            Gap = A.count("0") * 2 + 1

    for i in range(0, len(A) - 1):
        for j in range(0, i + 1):
            B = A[j:j + Gap]
            if (B.count("0") == B.count("1")):
                same = B.count("0") * 2
                return same
        Gap -= 1


A = input().strip()
print(solve(A))