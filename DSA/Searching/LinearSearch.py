def linearsearch(A, elem):
	"""
	Linear Search Algorithm that searches for an element in a n array with O(n) time complexity
	"""
	for a in A:
		if a==elem:
			return True
	return False