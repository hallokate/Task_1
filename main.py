from itertools import permutations


N = int(input('Введите количество рунктов: '))
points=[]
for i in range(N):
    t = input('Введите координаты пункта: ')
    a = tuple(int(x) for x in t.split())
    points.append(a)


'''
point_1 = (0, 0)
point_2 = (0, 4)
point_3 = (4, 4)
point_4 = (4, 0)
'''
'''
point_1 = (0, 2)
point_2 = (2, 5)
point_3 = (6, 6)
point_4 = (8, 4)
point_5 = (5, 2)
'''
'''
points=[]
points.append(point_1)
points.append(point_2)
points.append(point_3)
points.append(point_4)
'''
'''
points.append(point_1)
points.append(point_2)
points.append(point_3)
points.append(point_4)
points.append(point_5)
'''

num=''
for i in range(len(points)):
    num += str(i)

comb = permutations(num)

def get_total_lenght(new_c):
    tot_len = 0
    for i in range(1, len(new_c)):
        tot_len += get_lenght(new_c[i-1], new_c[i])
    tot_len += get_lenght(new_c[0], new_c[-1])
    return tot_len

def get_lenght(a,b):
    return ((points[b][0] - points[a][0]) ** 2 + (points[b][1] - points[a][1]) ** 2) ** 0.5


all_new_c = []
min = 0
min_c = None

for c in comb:
    if c[0] == '0':
        new_c = []
        for i in range(len(c)):
            new_c.append(int(c[i]))
        new_lenght = get_total_lenght(new_c)
        if min == 0 or min > new_lenght:
            min = new_lenght
            min_c = new_c

min_c_str = ''
min_c_str += '(' + str(points[min_c[0]][0]) + ', ' + str(points[min_c[0]][1]) + ')'
length = 0
for i in range(1, len(min_c)):
    length += get_lenght(min_c[i-1], min_c[i])
    min_c_str += '->(' + str(points[min_c[i]][0]) + ', ' + str(points[min_c[i]][1]) + ')[' + str(length) + ']'
min_c_str += '->(' + str(points[min_c[0]][0]) + ', ' + str(points[min_c[0]][1]) + ')[' + str(min) + ']'
min_c_str += ' = ' +  str(min)
print(min_c_str)







