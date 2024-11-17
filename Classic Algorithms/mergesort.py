import random


def merge(lst0, lst1):
    ret = []
    while lst0 and lst1:
        if lst0[0] <= lst1[0]:
            ret.append(lst0.pop(0))
        else:
            ret.append(lst1.pop(0))
    ret.extend(lst0)
    ret.extend(lst1)
    return ret


def mergesort(lst):
    if len(lst) <= 1:
        return lst
    # random to avoid dead loop for special sequence
    r = lst[random.randint(0, len(lst) - 1)]
    left, mid, right = [], [], []
    for i in lst:
        if i < r:
            left.append(i)
        elif i == r:
            mid.append(i)
        else:
            right.append(i)
    left = mergesort(left)
    left.extend(mid)
    right = mergesort(right)
    ret = merge(left, right)
    return ret


if __name__ == "__main__":
    print "please input integer number array"
    lst = []
    while 1:
        try:
            n = raw_input(">")
        except:
            print ""
            break
        lst.extend([int(i) for i in n.split()])
    print "origin: ", lst
    print "sorted: ", mergesort(lst)
