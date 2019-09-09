def bubbleSort(A):
    for i,ii in enumerate(A):
        for j,jj in enumerate(A[:-i]):
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A