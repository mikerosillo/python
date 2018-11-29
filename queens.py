def rowConflict(q):
    if len(q)!=len(set(q)):
        #print (set(q))
        return True
    else:
        return False


def diagonalConflict4(q):
    for col in range(3,0,-1):
        for i in range(col):
            if col-i==abs(q[col]-q[i]):
                return True
    return False


def diagonalConflict8(q):
    for col in range(7,0,-1):
        for i in range(col):
            if col-i==abs(q[col]-q[i]):
                return True
    return False

def diagonalConflict5(q):
    for col in range(4,0,-1):
        for i in range(col):
            if col-i==abs(q[col]-q[i]):
                return True
    return False

def diagonalConflict6(q):
    for col in range(5,0,-1):
        for i in range(col):
            if col-i==abs(q[col]-q[i]):
                return True
    return False

def diagonalConflict7(q):
    for col in range(6,0,-1):
        for i in range(col):
            if col-i==abs(q[col]-q[i]):
                return True
    return False

def diagonalConflict9(q):
    for col in range(8,0,-1):
        for i in range(col):
            if col-i==abs(q[col]-q[i]):
                return True
    return False


def findSolution(n):
    count=0
    if n == 4:
        for i0 in range(n):
            for i1 in range(n):
                for i2 in range(n):
                    for i3 in range(n):
                        q=[i0,i1,i2,i3]
                        if rowConflict(q) or diagonalConflict4(q):
                            continue
                        count+=1
                        print('solution',count,'=',q)
    elif n == 8:
        count=0
        for i0 in range(n):
            for i1 in range(n):
                for i2 in range(n):
                    for i3 in range(n):
                        for i4 in range(n):
                            for i5 in range(n):
                                for i6 in range(n):
                                    for i7 in range(n):
                                        q=[i0,i1,i2,i3,i4,i5,i6,i7]
                                        if rowConflict(q) or diagonalConflict8(q):
                                            continue
                                        count+=1
                                        print('solution',count,'=',q)
    elif n == 5:
        count=0
        for i0 in range(n):
            for i1 in range(n):
                for i2 in range(n):
                    for i3 in range(n):
                        for i4 in range(n):
                            q=[i0,i1,i2,i3,i4]
                            if rowConflict(q) or diagonalConflict5(q):
                                continue
                            count+=1
                            print('solution',count,'=',q)
    elif n == 6:
        count=0
        for i0 in range(n):
            for i1 in range(n):
                for i2 in range(n):
                    for i3 in range(n):
                        for i4 in range(n):
                            for i5 in range(n):
                                q=[i0,i1,i2,i3,i4,i5]
                                if rowConflict(q) or diagonalConflict6(q):
                                    continue
                                count+=1
                                print('solution',count,'=',q)
    elif n == 7:
        count=0
        for i0 in range(n):
            for i1 in range(n):
                for i2 in range(n):
                    for i3 in range(n):
                        for i4 in range(n):
                            for i5 in range(n):
                                for i6 in range(n):
                                    q=[i0,i1,i2,i3,i4,i5,i6]
                                    if rowConflict(q) or diagonalConflict7(q):
                                        continue
                                    count+=1
                                    print('solution',count,'=',q)
    elif n == 9:
        count=0
        for i0 in range(n):
            for i1 in range(n):
                for i2 in range(n):
                    for i3 in range(n):
                        for i4 in range(n):
                            for i5 in range(n):
                                for i6 in range(n):
                                    for i7 in range(n):
                                        for i8 in range(n):
                                            q=[i0,i1,i2,i3,i4,i5,i6,i7,i8]
                                            if rowConflict(q) or diagonalConflict9(q):
                                                continue
                                            count+=1
                                            print('solution',count,'=',q)




findSolution(9)  
