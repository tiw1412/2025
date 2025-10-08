import random as r
l = []
bg = []
lw = []
dey = 0
z = 0
count = int(input('Введите количество чисел: '))
#r.randint(0, count - 1)
for i in range (count):
    qn = int(input('Введите число: '))
    l.append(qn)
std = 0
ixr = 0
hassorted = False

# def rp(op, std, ixr, dey):
#     if l[std] > l[op]:
#             ixr = std
#             while l[ixr] < l[op]:
#                 l[ixr], l[ixr + 1] = l[ixr + 1], l[ixr]
#                 ixr += 1
#             print(dey , l)
#     if l[std] <= l[op]:
#         hassorted = True

op = count - 1
print(op)
print(l)

if l[std] < l[op]:
     std += 1
while hassorted != True:
# for i in range (count ** 2):
    #if l[std] >= l[op]:
    if l[op - 1] >= l[op]:
            l[op], l[op - 1] = l[op - 1], l[op]
            # l[op] = l[std]
            l[op], l[std] = l[std], l[op] 
            op -= 1
            print(l)
            print(l[op])
            print(l[std])
            print(op)
            print(std)
            if l[std] < l[op]:
                hassorted = True
            if op == 1:
                l[op], l[op - 1] = l[op - 1], l[op]
                op -= 1
                hassorted = True
                break
    if l[op - 1] < l[op]:
            l[op], l[op - 1] = l[op - 1], l[op]
            # l[op] = l[std]
            l[op], l[std] = l[std], l[op] 
            std += 1
            op -= 1
            print(l)
            print(l[op])
            print(l[std])
            print(op)
            print(std)
            if l[std] < l[op]:
                hassorted = True        
            if op == 1:
                l[op], l[op - 1] = l[op - 1], l[op]
                op -= 1
                hassorted = True
                break
    

#while hassorted != True:
# for i in range(count):
#     if l[op - 1] < l[op]:
#         lw.append(l[op - z])
#         # z += 1
#         # if op - z == -1:
#         #     break
#             # l[op - 1], l[std] = l[std], l[op - 1]
#             # std += 1
#             # dey = 'Пр'
#             # rp(op, std, ixr, dey)
#     if l[op - 1] >= l[op]:
#         bg.append(l[op - z])
#         # z += 1
#         # if op - z == -1:
#         #     break
#               zov (24.02.2022)        
#             # l[op - 1], l[std] = l[std], l[op - 1]
#             # dey = 'Пк. '
#             # rp(op, std, ixr, dey)



#for i in range(count - (len(lw) + len(lw))):


        
# op = len(lw)
# std = 0
# while std != op:
#     lw[op - 1], lw[std] = lw[std], lw[op - 1]
#     std += 1

# op = len(bg)
# std = 0
# while std != op:
#     bg[op - 1], bg[std] = bg[std], bg[op - 1]
#     std += 1

o = lw + bg

print(l)
print(hassorted)
print(op)
print(l[op])
print(std)
print(l[std])
print(lw)
print(bg)
print(o)