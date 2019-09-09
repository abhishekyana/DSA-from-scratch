def binarysearch(A, elem):
	"""
	When given a sorted Array this function will search for the element in O(logn) time.
	input: Sorted Array A and Element to be search elem
	output: Bool of element presence in Array
	"""
	if A==[]:
		return False
	mid = len(A)//2
	midE = A[mid]
	if midE==elem:
		return True
	elif midE>elem:
		return binarysearch(A[:mid], elem)
	elif midE<elem:
		return binarysearch(A[mid+1:], elem)