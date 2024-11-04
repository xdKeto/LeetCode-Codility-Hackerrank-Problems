def solution(N):
    a = bin(N)[2:] # jadiin binary
    gap = 0
    maxgap = 0
    
    for i in a:
        if int(i) == 0:
            gap += 1
        elif int(i) == 1:
            maxgap = max(maxgap, gap)
            gap = 0
    
    return maxgap

