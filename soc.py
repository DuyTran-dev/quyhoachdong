# Sóc là một loài động vật rất nhanh nhẹn, thông minh. Mỗi khi di chuyển chú thường nhảy lên, xuống một cách nhanh chóng. Hôm này Sóc định dạo chơi trên một dãy đồi núi nhấp nhô, đoạn lên cao, đoạn xuống thấp. Địa hình đồi núi được xác định là một dãy các bật từ trái sang phải với độ cao khác nhau. Giữa các dãy độ cao trên điểm cân bằng gì được gọi là độ cao dương, ngược lại dưới điểm cần bằng thid dược gọi là độ cao âm. Dãy đồi núi bao gồm N (N <= 10^5) bậc, mỗi bậc có một giá trị dộ cao có thể âm hoặc dương nằm trong khoảng [-10^9, 10^9]. Ban đầu Sóc ở vị trí điểm cần bằng (độ cao 0), mỗi bước nhẩy Sóc có thể nhay sang phải tối thiểu là 1 bước và tối đa là k bước (k<=100). Khi dừng lại ở một bậc nào thì độ cao của bậc đó được cộng vào tổng độ cao mà Sóc đã nhảy. Bởi vì có ý định dạo chơi trên dãy núi, nên Sóc sẽ dừng lại ở bắt cứ bặc nào miễn sao Sóc đạt được tổn độ cao lớn nhất có thể. Bạn hãy xác định xem Sóc sẽ đạt được tổng  độ cao lớn nhất là bao nhiêu?
# INPUT
# Dòng đầu tiên chứa 2 số nguyên dương N và K mỗi số cách nhau một dấu cách
# Dòng thứ hai chứa N số nguyên là dãy độ cao các bậc, các số cách nhau ít nhất một dấu cách

# OUTPUT
# Một dòng duy nhất chứa một số nguyên là tổng độ cao lớn nhất mà Sóc đạt được

with open("soc.INP") as f:
    n, k = list(map(int, f.readline().split()))
    a = list(map(int, f.readline().split()))

dp = [-float('inf')] * n
dp[0] = 0
for i in range(1, n):
    for j in range(max(0, i - k), i): 
        dp[i] = max(dp[i], dp[j] + a[i])

print(max(dp))
