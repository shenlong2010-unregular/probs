'''
Create a function that takes a single word string and does the following:

1.Concatenates inator to the end if the word ends with a consonant,
otherwise, concatenate -inator instead.

2.Adds the word length of the original word to the end, supplied with "000".

inator_inator("Shrink") ➞ "Shrinkinator 6000"

inator_inator("Doom") ➞ "Doominator 4000"

inator_inator("EvilClone") ➞ "EvilClone-inator 9000"
'''

def inator_inator(inv):
    non_consonant = 'aeoui'
    if inv[-1].lower() in non_consonant:
        new_string = inv + '-inator ' + str(len(inv)) + '000'
        return new_string

    else:
        new_string = inv + 'inator ' + str(len(inv)) + '000'
        return new_string
print(inator_inator('Shrink'))

'''
def inator_inator(inv):
	original=inv
	if inv[-1] in 'ieuoaIEOUA':
		inv+="-"
	return inv+"inator {}000".format(len(original))
'''