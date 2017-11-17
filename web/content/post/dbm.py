#!/usr/local/bin/python3
# setup ###################################################
import sys
import math
inf = math.inf
zero = int(sys.argv[1])
arg = int(sys.argv[2])
# DBM 1 ###################################################
e1 = [[  0, -2,  0, -2],
      [  3,  0,  3,  0],
      [  0, -2,  0, -2],
      [  3,  0,  3,  0]]
# DBM 2 ###################################################
e2 = [[  0,inf,inf,inf],
      [inf,  0,inf,inf],
      [  2,inf,  0,inf],
      [  6,inf,inf,  0]]
# Resultant DBM ###########################################
e3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# intersection ############################################
def intersect(e1, e2, e3):
    for i in range(0,4):
        for j in range(0,4):
            if e1[i][j] <= e2[i][j]:
                e3[i][j] = e1[i][j]
            else:
                e3[i][j] = e2[i][j]
# canonicalization ########################################
def canonicalize(e3):
    for l in range(0,4):
        for i in range(0,4):
            for j in range(0,4):
                e3[i][j] = min(e3[i][j],e3[i][l]+e3[l][j])
# main ####################################################
intersect(e1, e2, e3)
canonicalize(e3)
# case: zero ##############################################
if zero == 1:
    e3[0][arg] = 0
    e3[arg][0] = 0
    ps = [1,2,3]
    ps.remove(arg)
    for index in ps:
        e3[arg][index] = e3[0][index]
        e3[index][arg] = e3[index][0]
    canonicalize(e3)
# results #################################################
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in e3]))
print( str(-1 * e3[0][1]) + ' <= x1 <= ' + str(e3[1][0]) )
print( str(-1 * e3[0][2]) + ' <= x2 <= ' + str(e3[2][0]) )
print( str(-1 * e3[0][3]) + ' <= x3 <= ' + str(e3[3][0]) )        
print( str(-1 * e3[2][1]) + ' <= x1 - x2 <= ' + str(e3[1][2]) )
print( str(-1 * e3[3][2]) + ' <= x2 - x3 <= ' + str(e3[2][3]) )
print( str(-1 * e3[3][1]) + ' <= x1 - x3 <= ' + str(e3[1][3]) )


