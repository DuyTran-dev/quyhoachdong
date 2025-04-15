# Cho n đồ vật khác nhau, đồ vật thứ i có trọng lượng w_i​  và giá trị v_i​. Bạn mang theo một chiếc túi có tải trọng tối đa là W, nhiệm vụ của bạn là chọn ra các đồ vật để cho vào túi sao cho tổng giá trị của các đồ vật lấy được là lớn nhất có thể?

# INPUT
# Dòng thứ nhất ghi hai số nguyên n và s là số lượng đồ vật và trọng lượng tối đa của cái túi

# OUTPUT
# Một dòng duy nhất ghi số nguyên giá trị tối đa có thể mang theo

with open("balo.INP") as f:
    n, s = list(map(int, f.readline().split()))
    w = list(map(int, f.readline().split()))
    v = list(map(int, f.readline().split()))

dp = []
for i in range(n):
    dp.append([0] * (s + 1))
tong = 0

for i in range(n):
    for j in range(s + 1):
        if j >= w[i]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i]] + v[i])
            pass
        else:
            dp[i][j] = dp[i - 1][j]
    if max(dp[i]) >= tong:
        tong = max(dp[i])

with open("balo.OUT", "w") as f:
    f.write(str(tong))