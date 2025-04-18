# Trong một trang trại gà có nuôi n con gà thuộc nhiều loài gà khác nhau, những con gà cùng loại thì được ký hiệu bằng một mã số giống nhau. Với mã số là một số nguyên dương. Em hãy lập trình ếm xem trong trang trại loài gà nào có số lượng nhiều nhất và có bao nhiêu con

# INPUT
# Dòng 1 ghi số nguyên dương n
# Dòng 2 dãy n số nguyên dương

# OUTPUT
# Một dòng duy nhất ghi mã số loại gà nhiều nhất và số lượng cách nhau bởi dấu cách

with open("traiga.INP") as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))

d = {}
for i in a:
    if d.get(i):
        d[i] += 1
    else:
        d[i] = 1

with open("traiga.OUT", "w") as f:
    print(f"{max(d, key=d.get)} {max(d.values())}")
    f.write(f"{max(d, key=d.get)} {max(d.values())}")