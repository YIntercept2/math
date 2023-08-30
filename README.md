# math
A varied collection of minor notes on math

d10estimate.py - is a new bound on the D(10) dedekind, with explaination. More of a notebook than a script proper.

determine.py - was a throwaay used for generating determinant matrices provided a set of elements, and element names.

factor.py - is a naive factorization algorithm.

genprimes7a.py - is a novel prime generator. It works by first generating the quasi lucas-carmichael numbers (QLCs) which include as a subset the prime numbers, and then applies tests to filter out a subset of numbers, leaving behind the primes. Because
QLCs are quicker to find than the primes by themselves, and because testing primality is easier than generating primes, it follows that generating QLCs and filtering out false-primes is faster generally than generating the primes themselves. 

