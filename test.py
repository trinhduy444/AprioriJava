# def T(n):
#     if n == 1:
#         return 1
#     return 3*T(n-1)
# n = 5
# x = 3 *(3**(n-2))
# print((T(n)))
# print(x) 
###################33333333333333333

##################################
# def Arr(A):
#     c =0
#     for i in range(1,  A+1):
#        for j in range(i , A+1):
#         # print(A[i],A[j])
#         # if A[i] == A[j]: return False
#         c += 1

#     return c
# A = 5
# # print(len(A))
# print(Arr(A))

# def T(n):
#     if n == 1 :
#         return 1
#     return 2*(T(n-1)) +1
# n = 4
# x = 2*(2**(n-1) -1 )+ 1
# print((T(n)))
# print("x=",x)
def matrix_multiplication(A, B):
    h, w = len(A), len(B[0])
    result = [[0 for x in range(w)] for y in range(h)]
    for i in range(h):
        for j in range(w):
            for k in range(len(A[0])):
                result[i][j] += A[i][k] * B[k][j]
    return result

A= [[2,3,4],[1,0,0]]
B= [[0,1000],[1,100],[0,10]]
print(matrix_multiplication(A,B))