import numpy as np
import matplotlib.pyplot as plt
from csv import reader

folder = '/home/cuonghn/'
name = 'perplexities.csv'

name1 = folder + name
name2 = folder + 'Desktop/' + name

with open(name1, 'r') as f1:
    data1 = list(reader(f1))

with open(name2, 'r') as f2:
    data2 = list(reader(f2))

step = 10

y1 = [float(i[0]) / 5 for i in data1]
y2 = [float(i[0]) / 5 for i in data2]

plt.plot(range(step -1, len(y1), step), y1[step -1::step], 'r.-', label='l1')
plt.plot(range(step -1, len(y2), step), y2[step -1::step], 'b*-', label='l2')
# l3, = plt.plot(range(step -1, len(y2), step), y2[step -1::step], 'b^-', label='l2')
plt.legend(loc = 4, ncol = 2)
#plt.legend(handles=[l1, l2])
plt.xlabel('num minibatch')
plt.ylabel('log predictive')

# plt.show()
plt.savefig('f1.png')
