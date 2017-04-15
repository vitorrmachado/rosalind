# http://rosalind.info/problems/revc/

_reverse_complement = ""

with open("rosalind_revc.txt", "r") as file:
    for _dna in file:
        for letter in _dna:
            if letter == 'A':
                _reverse_complement += "T"
            elif letter == 'T':
                _reverse_complement += "A"
            elif letter == "C":
                _reverse_complement += "G"
            elif letter == "G":
                _reverse_complement += "C"

print(_reverse_complement[::-1]) # [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.