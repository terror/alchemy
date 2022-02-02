import random
import traceback
from functools import cached_property
from math import gcd
from typing import Union

# Select two prime numbers (p, q)
#
# p      = random prime
# q      = random prime
# N      = p * q
# phi(N) = (p - 1) (q - 1)
# e      = aribitrary small n where gcd(n, phi) === 1
# d      = modinv(e, phi)
#
# public  -> (e, N)
# private -> (d)
#
# E -> m^e mod N = c
# D -> c^d mod N = m
#
# **** Theory ****
#
# Easy to find product of two prime numbers (p, q)
# but hard to find prime factors from a given composite number
#
# Knowing the factors of `N` (p * q) is the trapdoor
#
# k * phi(n) + 1 = p * q
#
# phi(p)         = (p - 1)
# phi(pq)        = (p - 1) (q - 1)
#
# a ^ (p * q)          = a (mod N)
# a ^ (k * phi(n) + 1) = a (mod N)
# a ^ (ed)             = a (mod N)
# e * d                = k * (phi(N) + 1)
# d                    = (k * (phi(N) + 1)) / e

K = 2

PRIMES = [
  3,
  5,
  7,
  11,
  13,
  17,
  19,
  23,
  29,
  31,
  37,
  41,
  43,
  47,
  53,
  59,
  61,
  67,
  71,
  73,
  79,
  83,
  89,
  97,
  101,
  103,
  107,
  109,
  113,
  127,
  131,
  137,
  139,
  149,
  151,
  157,
  163,
  167,
  173,
  179,
  181,
  191,
  193,
  197,
  199,
  211,
  223,
  227,
  229,
  233,
  239,
  241,
  251,
  257,
  263,
  269,
  271,
  277,
  281,
  283,
  293,
  307,
  311,
  313,
  317,
  331,
  337,
  347,
  349,
  353,
  359,
  367,
  373,
  379,
  383,
  389,
  397,
  401,
  409,
  419,
  421,
  431,
  433,
  439,
  443,
  449,
  457,
  461,
  463,
  467,
  479,
  487,
  491,
  499,
  503,
  509,
  521,
  523,
  541,
  547,
  557,
  563,
  569,
  571,
  577,
  587,
  593,
  599,
  601,
  607,
  613,
  617,
  619,
  631,
  641,
  643,
  647,
  653,
  659,
  661,
  673,
  677,
  683,
  691,
  701,
  709,
  719,
  727,
  733,
  739,
  743,
  751,
  757,
  761,
  769,
  773,
  787,
  797,
  809,
  811,
  821,
  823,
  827,
  829,
  839,
  853,
  857,
  859,
  863,
  877,
  881,
  883,
  887,
  907,
  911,
  919,
  929,
  937,
  941,
  947,
  953,
  967,
  971,
  977,
  983,
  991,
  997
]

KEY_SIZE = 256

class Rng:
  @staticmethod
  def generate():
    while 1:
      candidate = Rng.__prime_candidate(KEY_SIZE)
      if not Rng.__miller_rabin(candidate):
        continue
      else:
        return candidate
    return -1

  @staticmethod
  def __n_bit_random(n):
    return random.randrange(2**(n - 1) + 1, 2**n - 1)

  @staticmethod
  def __prime_candidate(n):
    while 1:
      r = Rng.__n_bit_random(n)
      for div in PRIMES:
        if r % div == 0 and div**2 <= r:
          break
      else:
        return r

  @staticmethod
  def __miller_rabin(candidate):
    max_div = 0
    ec = candidate - 1

    while ec % 2 == 0:
      ec >>= 1
      max_div += 1

    assert (2**max_div * ec == candidate - 1)

    def __trial(round):
      if pow(round, ec, candidate) == 1:
        return False
      for i in range(max_div):
        if pow(round, pow(2, i) * ec, candidate) == candidate - 1:
          return False
      return True

    trials = 20
    for i in range(trials):
      round = random.randrange(2, candidate)
      if __trial(round):
        return False

    return True

class Identity(object):
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f'{self.name}: Public Key: {self.public_key}'

  def __dict__(self):
    return {'name': self.name, 'public_key': self.public_key}

  @cached_property
  def __p(self):
    return Rng.generate()

  @cached_property
  def __q(self):
    return Rng.generate()

  @cached_property
  def __phi(self):
    return (self.__p - 1) * (self.__q - 1)

  @cached_property
  def __d(self):
    return pow(self.e, -1, self.__phi)

  @property
  def __private_key(self):
    return (self.p, self.q)

  @cached_property
  def N(self):
    return self.__p * self.__q

  @cached_property
  def e(self):
    for n in range(2, self.__phi):
      if gcd(n, self.__phi) == 1:
        return n

  @property
  def public_key(self):
    return (self.N, self.e)

  def encrypt(self, message, recipient):
    return pow(message, recipient.e, recipient.N)

  def decrypt(self, message):
    return pow(message, self.__d, self.N)

def main(message):
  alice, bob = Identity('alice'), Identity('bob')
  print((received := bob.decrypt(alice.encrypt(message, bob))))
  assert received == message

if __name__ == '__main__':
  try:
    main(20)
  except Exception as error:
    traceback.print_exc()
    print(f'error: {str(error)}')
