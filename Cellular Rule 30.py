import matplotlib.pyplot as plt


def int_to_binary(x,n):
    binary = ''
    for i in range(n-1,-1,-1):
        if x-2**i >= 0:
            x -= 2**i
            binary += '1'
        else:
            binary += '0'
    return binary

def binary_to_int(x):
    number = 0
    for i in range(len(x)-1, -1, -1):
        number += int(x[len(x)-i-1])*2**i
    return number

rule = int_to_binary(30,8)
cells_t0 = ['0' for i in range(1001)]
cells_t0[500] = '1'
cells_t1 = ['0' for i in cells_t0]
cells = []
for i in range(int(len(cells_t0)* 0.5)):
    new = []
    for i,cell in enumerate(cells_t0):
        neighbors = cells_t0[max(i-1,0)] + cells_t0[i] + cells_t0[min(i+1,len(cells_t0)-1)]
        new.append(rule[len(rule) - 1 - binary_to_int(neighbors)])
    cells.append([1-int(x) for x in cells_t0])
    cells_t0 = new
cells.append([1-int(x) for x in cells_t0])

plt.matshow(cells, cmap='Greys', interpolation='sinc')
plt.show()
