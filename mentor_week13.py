def bothInAandB(L1, L2):
    common=[]
    for a in L1:
        for b in L2:
            if a == b & a not in common:
                common.append(a)
    common.sort()
    return common

def list_copy(L):
    C = L[0:]
    return C

def append(L,a):
    L.append(a)


fp = open("InData.txt", "r")


x = int(fp.readline())
A = list(int(x) for x in fp.readline().split())
B = list(int(x) for x in fp.readline().split())

fp.close()
print("Q1: ", end=" ")
print(x)
print(A)
print(B)


print("Q2: ", end=" ")
append(A,x)
print(A)


print("Q3: ", end=" ")
C = list_copy(A)
print(C)

print("Q4: ")
C = bothInAandB(A,B)
print(C)
