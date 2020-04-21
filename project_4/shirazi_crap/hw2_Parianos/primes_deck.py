from kanren import isvar, run, membero
from kanren.core import success, fail, goaleval, condeseq, eq, var
from sympy.ntheory.generate import prime, isprime
import itertools as it

#check if the elements of x are prime
def prime_check(x):
    if isvar(x):
       return condeseq([(eq,x,p)] for p in map(prime, it.count(1)))
    else:
       return success if isprime(x) else fail

x = var()
# Check if an element in the list is a prime number
list_nums = (23, 4, 27, 17, 13, 10, 21, 29, 3, 32, 11, 19)
print('\n List of primes in the list:')
print(set(run(0, x, (membero, x, list_nums), (prime_check, x))))

# Print first 7 prime numbers
print('\n List of first 7 prime numbers:')
print(run(7, x, prime_check(x)))
