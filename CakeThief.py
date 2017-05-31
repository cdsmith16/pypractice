
def maxcount(cake_tuples,duffel,topcount):
    max = topcount
    for cake in cake_tuples:
        newduffel = duffel - cake[0]
        #print(newduffel)
        if (newduffel) < 0:
            pass
            #print("skip, duffel too full")
            #print("keep old duffel %d and topcount %d" % (duffel,topcount))
        else:
            #print("room for more!")
            newcount = maxcount(cake_tuples,newduffel,topcount+cake[1])
            if newcount > max:
                max = newcount
    return max

"""The cakes come in duffel bags with a certain weight capacity.
The cakes come in an array of tuples with a weight and value.
Example cakes: [(7,160),(4,55),(8,90)]
Example duffel: 400"""
def max_duffel(cake_tuples,duffel):
    cake_tuples = sorted(cake_tuples,key = lambda x: (x[1]/float(x[0])), reverse=True)
    count = 0
    for i in range(len(cake_tuples)):
        newcount = maxcount(cake_tuples[i:],duffel,0)
        #print(newcount)
        if newcount > count:
            count = newcount
    return count

caketupetest = [(7,160),(3,90),(2,15)]
dufftest = 20
print(caketupetest)
print(max_duffel(caketupetest,dufftest))