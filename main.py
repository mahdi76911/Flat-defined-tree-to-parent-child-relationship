# Read First Column and convert it to child id

import numpy as np
import csv


def dep(inp):
    return inp.count('.')


def convert(path):
    fileName = path[path.rfind('/'):path.rfind('.')]
    directory = path[:path.rfind('/')]

    # read data
    dataFile = np.array([np.array(i.strip().split(',')) for i in open(path).readlines()])

    x = [d[0] for d in dataFile[1:]]

    # make list
    res = []
    last = [0]
    for ix, i in enumerate(x):
        if dep(i) > dep(x[last[-1]]):
            last.append(ix)
        elif dep(i) < dep(x[last[-1]]):
            while dep(i) < dep(x[last[-1]]):
                last.pop()

        res.append(last[-1])

    # res = np.transpose(res)

    # write to file
    with open(directory + '/' + fileName + '_res.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for i in res:
            wr.writerow([i])

    print("done")


# Checking
"""
from sklearn.metrics import mean_squared_error

y = []
for i in dataFile[1:]:
    d = i[3]
    if d == '':
        y.append(0)
    else:
        y.append(int(d))
print(mean_squared_error(y[0:91], res[0:91], squared=False))
"""

# GUI
exec(open('gui.py').read(), {'function': convert})
# , {'cnn_obj': cnn_clf}
