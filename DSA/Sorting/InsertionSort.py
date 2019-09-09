def insertionSort(A, verbose=False):
	"""
	Insertion Sort Algorithm for change an unsorted Array into sorted array
	"""
    n = len(A)
    for i in range(1, n):
        temp = A[i]
        for j in range(i, -1, -1):
            if temp<A[j]:
                A[j+1]=A[j]
                A[j] = temp
            if temp>A[j]:
                break
        if verbose: print(A[:i],"===", A[i:])
    return A