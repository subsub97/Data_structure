def solve(A):
    if(A.count('0') == A.count('1')):
        return(len(A))
    else:
        n = len(A)
        count = 0
        start = 0
        end = n
        a = 0
        while count != n:

            count +=2
            a -=2

            if count == n:
                count = 0
                start += 1
                end -= 1
                n -= 2
                a=0
        print("end")



A = input().strip()
print(solve(A))