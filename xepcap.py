# Cho m bò đực và n bò cái, nhiệm vụ của bạn là xếp một cặp bò đực và cái trong đó cân nặng của con bò đực phải lớn hơn con bò cái, mỗi con bò chỉ được phép ghép 1 lần

# INPUT
# Dòng 1 ghi số m và n cách nhau bởi dấu cách
# Dòng 2 dãy m số nguyên dương
# Dòng 3 dãy n số nguyên dương

# OUTPUT
# Ghi ra một số nguyên dương duy nhất là số cặp nhiều nhất xếp được

with open("xepcap.INP") as f:
    m, n = list(map(int, f.readline().split()))
    m_a = list(map(int, f.readline().split()))
    n_a = list(map(int, f.readline().split()))

c = 0
k = 0
for i in m_a:
    for j in range(k, n):
        if i > n_a[j]:
            k += 1
            c += 1

with open("xepcap.OUT", "w") as f:
    f.write(str(c))