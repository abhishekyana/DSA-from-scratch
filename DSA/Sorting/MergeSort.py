def mergeSort(A):
    if len(A)==2:
        if A[1]<A[0]:
            return A[::-1]
        else:
            return A
    if len(A) in [0,1]:
        return A
    mid = len(A)//2
    return merge(mergeSort(A[:mid]), mergeSort(A[mid:]))
def merge(A, B):
    K=[]
    while min(len(A), len(B))>0:
        if A[0]<B[0]:
            K.append(A.pop(0))
        else:
            K.append(B.pop(0))
    return K+A if len(A) else K+B