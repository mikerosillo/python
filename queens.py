def rowConflict(q):
    if len(q)!=len(set(q)):
        #print (set(q))
        return True
    else:
        return False
def diagonalConflict(q):
    for col in range(7,0,-1):
        for i in range(col):
            if col-i==abs(q[col]-q[i]):
                return True
    return False

count=0
for i0 in range(8):
    for i1 in range(8):
        for i2 in range(8):
            for i3 in range(8):
                for i4 in range(8):
                    for i5 in range(8):
                        for i6 in range(8):
                            for i7 in range(8):
                                q=[i0,i1,i2,i3,i4,i5,i6,i7]
                                if rowConflict(q) or diagonalConflict(q):
                                    continue
                                count+=1
                                print('solution',count,'=',q)
