'''
实现冒泡排序
传入参数：nums 需要排序的数组
传入参数：isAsc 排序模式，升序还是降序，默认升序
'''

def bubbleSort(nums,isAsc):
    for i in range(len(A)-1):  # 外循环每一次把有序的数增加一个
        for j in range(len(A)-i-1):  # 内循环每次把无序部分中的最大值放到最上面
            if(isAsc):  # 是否升序
                if(A[j] > A[j+1]):
                 A[j], A[j+1] = A[j+1], A[j]

            else:  # 降序
                if (A[j] < A[j + 1]):
                    A[j], A[j + 1] = A[j + 1], A[j]



A=[3,4,2,22,7,8]
bubbleSort(nums=A,isAsc=True)
print(A)

bubbleSort(nums=A,isAsc=False)
print(A)


