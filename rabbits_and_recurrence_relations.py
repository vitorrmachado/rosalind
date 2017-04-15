# http://rosalind.info/problems/fib/

#1 1 4 7 19 -> Fx-1 + (Fx-2 x 3)
n = int(input('Insert the N value: '))
k = int(input('Insert the K value: '))
init = 1
dictionary = {1 : 1}


for num in range(2,n+1):
    fx1 = dictionary[num-1]

    if num - 2 in dictionary:

        fx2 = dictionary[num-2]
    else:
        fx2 = 0

    rabbits = fx1 + (fx2 * k)

    dictionary[num] = rabbits

print('The number of rabbits present in month {n} is {rabbits}'.format(n=n, rabbits=dictionary[n]))
print(dictionary)