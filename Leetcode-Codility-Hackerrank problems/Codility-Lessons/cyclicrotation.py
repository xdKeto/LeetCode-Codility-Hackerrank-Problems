def solution(A, K):
    size = len(A)
    copy = A.copy()
    
    for i in range(len(A)):
        newindex = (i + K) % size
        copy[newindex] = A[i]
    
    return A