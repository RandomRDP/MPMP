from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

x= 0
i = 0
while x != 64:
    i += 1
    x = len(factors(i))
    print("i:{} x:{}".format(i,x))
print(factors(i))
