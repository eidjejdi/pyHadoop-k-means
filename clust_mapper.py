#!/home/hadoop/anaconda3/bin
import sys
import numpy as np

f = open('centroid.csv', 'r', encoding='UTF8')
sys.stdin = open('100개.csv', 'r', encoding='UTF8')
sys.stdout = open('mapper.out', 'w')

c = []
for text in f:
   line = text.split(" ")
   c.append([float(line[0]), float(line[1]), float(line[2]), float(line[3])]) 
c = np.array(c)

iris = []
for text in sys.stdin:
    line = text.split(",")
    points = np.array([float(line[0]), float(line[1]), float(line[2]), float(line[3])])
    print(np.argmin(np.sum((points - c)**2, axis=1)), points[0], points[1], points[2],points[3])
    
sys.stdout.close()



