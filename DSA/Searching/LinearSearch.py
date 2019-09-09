def linearsearch(A, elem):
	"""
	Linear Search Algorithm that searches for an element in an array with O(n) time complexity.
	inputs: Array A and element e, that has to be searched
	output: True/False
	"""
	for a in A:
		if a==elem:
			return True
	return False
