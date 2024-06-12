# times to Drop K eggs for N floors

# DP[K][N] = min ( [ max(DP[K-1][i-1], DP[K][N-i]) + 1 for i in range(1, N+1) ])

# DP[i][0] = 0
# DP[0][j] = 0

def get_times_for_egg_drop1(K, N):

    DP = [ [ 0 for n in range(N+1) ] for k in range(K+1)]
    for n in range(1, N+1):
        DP[1][n] = n
    for k in range(1, K+1):
        DP[k][1] = 1

    if K < 2:
        return DP[K][N]
    
    for k in range(2, K+1):
        for n in range(2, N+1):
            DP[k][n] = n
            for i in range(1, n+1):
                DP[k][n] = min(DP[k][n], 1 + max(DP[k-1][i-1], DP[k][n-i]))

    print(DP)
    return DP[K][N]

print(get_times_for_egg_drop1(2, 100))





# Solution 2

# DP[k][m] = n:  means: k eggs and m times can test n floors

# DP[k][m] = DP[k-1][m-1] + DP[k][m-1] + 1
#              broken       not broken

# for N floors, test N times for worst cases

def get_times_for_egg_drop2(K, N):
    
    DP = [ [ 0 for n in range(N+1) ] for k in range(K+1) ]

    m = 0
    while DP[K][m] < N:
        m += 1
        for k in range(1, K+1):
            DP[k][m] = DP[k-1][m-1] + DP[k][m-1] + 1

    return m

print(get_times_for_egg_drop2(2, 100))



