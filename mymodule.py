print("module imported")

def findindex(to_search,list):
	""" return index of a value if present in a list"""
	for i,j in enumerate(list):
		if j==to_search:
			return i

	return -1