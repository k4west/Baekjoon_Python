import sys
input = sys.stdin.readline

def main():
    INF = float('inf')
    c = [[2, 2, 2, 2, 2],
         [0, 1, 3, 4, 3],
         [0, 3, 1, 3, 4],
         [0, 4, 3, 1, 3],
         [0, 3, 4, 3, 1]]

    arr = list(map(int, input()[:-2].split()))
    dp = [INF]*5
    dp[0] = 0
    a0 = 0

    for a1 in arr:
        dp[a0] = min(dp[i] + c[i][a1] for i in range(5))
        for j in range(5):
            if j == a0:
                continue
            dp[j] += c[a0][a1]
        a0 = a1

    print(min(dp))

if __name__ == "__main__":
    main()