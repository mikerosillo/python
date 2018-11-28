def rockConflict(q):#function to check for duplicates if there is a duplicate
#in the array q it means we have a rockConflict
    if len(q)!=len(set(q)):#so we make a copy of q with only
    #one copy of the duplicates until we have no duplicates


        #print (set(q))
        return True
    else:
        return False
#to see if we have a diagonalConflict we check position againts position
#starting from left to rigth
def diagonalConflict(q):
    for col in range(7,0,-1):
        for i in range(col):
            if col-i==abs(q[col]-q[i]):
                return True
    return False

count=0
#this is how we generated our board
for i0 in range(8):
    for i1 in range(8):
        for i2 in range(8):
            for i3 in range(8):
                for i4 in range(8):
                    for i5 in range(8):
                        for i6 in range(8):
                            for i7 in range(8):
                                #this represents queens position
                                q=[i0,i1,i2,i3,i4,i5,i6,i7]
                                if rockConflict(q) or diagonalConflict(q):
                                    continue
                                count+=1
                                print('solution',count,'=',q)
