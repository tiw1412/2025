import random as r
l = []
bg = []
lw = []
dey = 0
count = int(input('Введите количество чисел: '))
op = count - 1 #r.randint(0, count - 1)
for i in range (count):
    qn = int(input('Введите число: '))
    l.append(qn)
std = 0
ixr = 0
hassorted = False

def rp(op, std, ixr, dey):
    l[op - 1], l[std] = l[std], l[op - 1]
    std += 1
    if l[std] > l[op]:
            ixr = std
            while l[ixr] < l[op]:
                l[ixr], l[ixr + 1] = l[ixr + 1], l[ixr]
                ixr += 1
            print(dey , l)
    if l[std] < l[op]:
        hassorted = True


print(op)
print(l)


while hassorted != True:
#for i in range(count ** 2):
    if l[op - 1] < l[op]:
        lw.append(l[op - 1])
        dey = 'Пр'
        rp(op, std, ixr, dey)
    if l[op - 1] >= l[op]:
        bg.append(l[op - 1])
        dey = 'Пк. '
        rp(op, std, ixr, dey)
print(l)
print(hassorted)
print(op)
print(l[op])
print(std)
print(l[std])
print(lw)
print(bg)