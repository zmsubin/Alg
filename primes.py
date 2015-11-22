import math

def primes(n):
    candidates = set(range(2, n))

    for i, num in enumerate(list(candidates)[:len(candidates)/2]):
        for candidate in list(candidates)[i+1:]:
            if candidate % num == 0:
                candidates.remove(candidate)

    return list(candidates)

def largest_prime_factor(n, candidates, minimum):
    for candidate in candidates:
        if candidate <= minimum:
            next

        if n % candidate == 0:
            return n / candidate

    return None


def primes_alt(n):
    candidates = set(xrange(2, n))

    for num in list(candidates)[:len(candidates)/2+1]: #[:len(candidates)/2]:
        if num not in candidates:
           next
        for j in xrange(2,n/num+1):
           if j*num in candidates:
              #print "num,j"
              #print num
              #print j
              candidates.remove(j*num)

    return list(candidates)
