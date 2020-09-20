# O(n) time / O(1) space - where n is the lenght of the array
def isValidSubsequence(array, sequence):	
	seqIndex = 0
	for i in array:
		if seqIndex == len(sequence):
			break
		if sequence[seqIndex] == i:
			seqIndex += 1
	return seqIndex == len(sequence)

# O(n) time / O(1) space - where n is the lenght of the array
def isValidSubsequence(array, sequence):
    arrIndex = 0
	seqIndex = 0
	
	while arrIndex < len(array) and seqIndex < len(sequence):
		if array[arrIndex] == sequence[seqIndex]:
			seqIndex += 1
		arrIndex += 1
	return seqIndex == len(sequence)