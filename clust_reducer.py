#!/home/hadoop/anaconda3/bin
import sys
import numpy as np

f = open('centroid.csv', 'r', encoding='UTF8')
sys.stdin = open('mapper.out', 'r', encoding='UTF8')
sys.stdout = open('centroid.csv', 'w')


centroids = np.zeros((3, 4))
counts = np.zeros(3)



for text in sys.stdin:
    line = text.split(" ")
    counts[int(line[0])] += 1
    for i in range(1,5):
        centroids[int(line[0]), i-1] += float(line[i])

for i in range(3):
    centroids[i] /= counts[i]
    for j in range(4):
        print(centroids[i][j], end=" ")
    print()

sys.stdout.close()