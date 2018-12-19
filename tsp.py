#j value in i-th index means that node j goes right after node i
#node j goes right after node i means that j values in ith index


def Adjacency(x,forward):
    y = [0]*len(x)
    for z in range(len(x)):
        if(forward):
            i = x[z]
        else:
            j = x[z]
        if(z+1 == len(x)):
            z=0
        else:
            z+=1
        if(forward):
            j = x[z]
        else:
            i= x[z]
        y[i] = j
        #print(y)
    return y 

print("Forward:")
print(Adjacency([0,8,1,5,7,3,6,2,4,9],False))
print("Backwards:")
print(Adjacency([0,8,1,5,7,3,6,2,4,9],True))
