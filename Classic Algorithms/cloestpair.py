import math
import random
import numpy


def eulicd(pt0, pt1):
    return math.sqrt(sum(map(lambda x, y: (x - y) ** 2, pt0, pt1)))


def oneNorm(pt0, pt1):
    return sum(map(lambda x, y: abs(x - y), pt0, pt1))


def infNorm(pt0, pt1):
    return max(map(lambda x, y: abs(x - y), pt0, pt1))


def pNorm(pt0, pt1):
    return (sum(map(lambda x, y: (x - y) ** p, pt0, pt1))) ** (1. / p)


def distance(pt0, pt1):
    return infNorm(pt0, pt1)


def BruceForceCloestPair(ptlst):
    mindist = distance(ptlst[0], ptlst[1])
    pair = (ptlst[0], ptlst[1])
    for i in xrange(len(ptlst)):
        for j in xrange(i + 1, len(ptlst)):
            dist = distance(ptlst[i], ptlst[j])
            if dist < mindist:
                mindist = dist
                pair = (ptlst[i], ptlst[j])
    return mindist, pair


def medianDivide(xsort, ysort):
    l = len(xsort)
    median = xsort[l / 2][0]
    leftx = xsort[0:l / 2]
    rightx = xsort[l / 2:]
    lefty = []
    righty = []
    for i in ysort:
        if i[0] < median:
            lefty.append(i)
        else:
            righty.append(i)
    return median, leftx, lefty, rightx, righty


def DivideConquer(xsort, ysort):
    if len(xsort) <= 3:
        return BruceForceCloestPair(xsort)
    median, leftx, lefty, rightx, righty = medianDivide(xsort, ysort)
    min0, pair0 = DivideConquer(leftx, lefty)
    min1, pair1 = DivideConquer(rightx, righty)
    (m, pair) = (min0, pair0) if min0 < min1 else (min1, pair1)
    leftj, rightj = median - m, median + m
    yy = []
    for pt in ysort:
        if leftj < pt[0] < rightj:
            yy.append(pt)
    l = len(yy)
    for i in range(l):
        for j in range(i + 1, min(l, i + 8)):
            dist = distance(yy[i], yy[j])
            if dist < m:
                m, pair = dist, (yy[i], yy[j])
    return m, pair


def ClosetPair(ptlst):
    from copy import deepcopy
    xsort = deepcopy(ptlst)
    xsort = sorted(xsort, key=lambda pt: pt[0])
    ysort = deepcopy(ptlst)
    ysort = sorted(ysort, key=lambda pt: pt[1])
    return DivideConquer(xsort, ysort)


# test code
def genRandomMatrix(m, n):
    return [[random.random() for j in xrange(n)] for i in xrange(m)]

if __name__ == "__main__":
    ptlst = genRandomMatrix(60, 3)
    ret0 = ClosetPair(ptlst)
    ret1 = BruceForceCloestPair(ptlst)
    if ret0[0] > ret1[0]:
        print "wrong"
    else:
        print "right"
