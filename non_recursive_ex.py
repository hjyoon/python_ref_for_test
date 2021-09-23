import time
N = 50


def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


def fibo_dp(n, dp):
    if dp[n] != -1:
        return dp[n]
    if n < 2:
        return n
    else:
        dp[n-1] = fibo_dp(n-1, dp)
        dp[n-2] = fibo_dp(n-2, dp)
        return dp[n-1] + dp[n-2]


def fibo_non_recursive(n):
    res = 0
    st = []
    st.append(n)
    while st:
        v = st.pop()
        if v < 2:
            res += v
        else:
            st.append(v-2)
            st.append(v-1)
    return res


def fibo_non_recursive_dp(n, dp):
    # 비재귀 스택으로 dp어떻게 구현하는지 아직 모르겠다.
    res = 0
    st = []
    st.append(n)
    while st:
        v = st.pop()
        if dp[v] != -1:
            res += dp[v]
        else:
            if v < 2:
                res += v
            else:
                st.append(v-2)
                st.append(v-1)
    return res


def dynamic(n):
    dp = [0] * (N+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


dp = [-1]*(N+1)
# print(fibo_dp(N, dp))
# print(fibo(N))
# print(dynamic(N))
# print(fibo_non_recursive(N))
print(fibo_non_recursive_dp(N, dp))
