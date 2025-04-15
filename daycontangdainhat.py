# Cho một dãy gồm n phần tử,tìm dãy con(không liên tiếp) , tăng dần (không ngặt) dài nhất

# INPUT
# Dòng đầu tiên chưa số n
# Dòng thứ 2 gồm N số trong khoảng int

# OUTPUT
# Dòng duy nhất chứa độ dài dãy con tăng dài nhất

# ----------------------------------------------
# nếu a[i] > a[j] thì l[i] = max(l[i], l[j] + 1)
# trong đó j là chỉ số sau i

with open("daycontangdainhat.INP") as fi:
    n = int(fi.readline())
    a = list(map(int, fi.readline().split()))

l = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            l[i] = max(l[i], l[j] + 1)

with open("daycontangdainhat.OUT", "w") as fo:
    fo.write(str(max(l)))