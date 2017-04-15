# http://rosalind.info/problems/iprb/

k, m, n = float(18), float(18), float(16)

'''
	Crossing:
	AA x Aa: AA, Aa, AA, Aa
	crossings that give us individuals with an dominant allele:
	AA x AA, AA x Aa, AA x aa, Aa x Aa, Aa x aa
	
	1) the probability that parent 1 is AA
	2) the probability that parent 1 is Aa * the probability parent 2 is AA * 1
	3) the probability that parent 1 is Aa * the probability parent 2 is Aa * 0.75
	4) the probability that parent 1 is Aa * the probability parent 2 is aa * 0.5
	5) the probability that parent 1 is aa * the probability parent 2 is aA * 0.5
	6) the probability that parent 1 is aa * the probability parent 2 is AA * 1

	the probability of the parent 1 to be AA: k / (k + m + n)
'''

total = (k + m + n)

p1 = k / total
p2 = (m / total) * (k / (total - 1))
p3 = (m / total) * ((m - 1)/ (total - 1)) * 0.75
p4 = (m / total) * (n / (total - 1)) * 0.5
p5 = (n / total) * (m / (total - 1)) * 0.5
p6 = (n / total) * (k / (total - 1))

print('%f' % (p1 + p2 + p3 + p4 + p5 + p6))