def bubble(lst):
    l = len(lst)
    for i in xrange(l):
        for j in xrange(l-1,i, -1):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

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
    print "sorted: ", bubble(lst)
