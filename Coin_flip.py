import random

def coin_flip(times):
    heads=0
    tails=0
    for x in range(times):
        i=random.choice([0,1])
        if i==0:
            heads+=1
            print ('heads')
        else:
            tails+=1
            print('tails')
    print ('heads: ' + str(heads))
    print ('tails: ' + str(tails))
