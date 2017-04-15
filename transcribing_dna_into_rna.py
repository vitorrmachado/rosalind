# http://rosalind.info/problems/rna/

file = open("rosalind_rna.txt", "r")
_rna = ""
for _dna in file:
    for letter in _dna:
        if letter == 'T':
            _rna += 'U'
        else:
            _rna += letter
print(_rna)