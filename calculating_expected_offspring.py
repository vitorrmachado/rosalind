# http://rosalind.info/problems/iev/

offsprings = 2
a = offsprings * 19559 #AA-AA - Prob. 1
b = offsprings * 18136 #AA-Aa - Prob. 1
c = offsprings * 19532 #AA-aa - Prob. 1
d = offsprings * 17068 #Aa-Aa - Prob. 3/4
e = offsprings * 19995 #Aa-aa - Prob. 2/4
f = offsprings * 19049 #aa-aa - Prob. 0

total = (1 * a) + (1 * b) + (1 * c) + ((3/4) * d) + ((2/4) * e) + (0 * f)

print(total)