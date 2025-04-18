# Một dãy số được gọi là được biệt khi đọc từ trái sang phải cũng giống như đọc từ phải sang trái
# Cho số nguyên dương n và dãy số a gồm n phần tử mỗi phần tử là số nguyên dương. Hãy tìm ít nhất các phần tử cần chèn thêm vào đễ dãy A trở thành dãy số đặc biệt

# INPUT
# Dòng 1 ghi số n
# Dòng 2 dãy n số nguyên dương

# OUTPUT
# Sô nguyên duy nhất kết quả tìm được

with open("daysodacbiet.INP") as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))

a1 = a[0:int(n/2)]
a2 = a[int(n/2):n]

if len(a2) > len(a1):
    del a2[0]
a2.reverse()

c = 0
for i in range(int(n/2)):
    if a1[i] != a2[i]:
        c += 2

with open("daysodacbiet.OUT", "w") as f:
    f.write(str(c))