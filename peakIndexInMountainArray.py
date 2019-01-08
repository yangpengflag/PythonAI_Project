

def peakIndexInMountainArray(self, A):
    lenth = len(A)
    for x in range(lenth):
        if(A[x]>A[x+1]):
            print(x)
            return x
        else:
            continue
A= [0,1,0]
B = [0,2,3,0]
peakIndexInMountainArray(A,A)
peakIndexInMountainArray(B,B)



def peakIndexInMountainArray1(self, A):

    idx = A.index(max(A))
    print(idx)
    return idx

A= [0,1,0]
B = [0,2,3,0]
peakIndexInMountainArray1(A,A)
peakIndexInMountainArray1(B,B)


def peakIndexInMountainArray2(self, A):
    a = max(A)
    for i in range(len(A)):
        if A[i] == a:
            print(i)
            return i

A= [0,1,0]
B = [0,2,3,0]
peakIndexInMountainArray2(A,A)
peakIndexInMountainArray2(B,B)

# 这种写法好像有问题，待解决
def peakIndexInMountainArray3(self, A):
    for i in range(len(A)):
        while(A[i] < A[i+1]):
            i+=1
            print(i)
            return i

A= [0,1,0]
B = [0,2,3,0]
peakIndexInMountainArray3(A,A)
peakIndexInMountainArray3(B,B)



