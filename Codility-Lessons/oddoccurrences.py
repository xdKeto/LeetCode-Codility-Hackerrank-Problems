def solution(A):
    for i in range(0, len(A), 2):
        if i < len(A) - 1:
            if A[i] != A[i+1]:
                return A[i]
        else:
            return A[i] 