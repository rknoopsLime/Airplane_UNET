import numpy as np
import pandas as pd

def return_list_of_primes(cities):
    NumberOfCities = len(cities)
    primes = []
    for possiblePrime in range(2, len(cities)):

        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False

        if isPrime:
            primes.append(possiblePrime)
            print('found prime:'+str(possiblePrime))
    return primes

def save_primes(primes):
    np.save('prime_list.npy', primes)
    
def load_primes(PATH = 'prime_list.npy'):
    return np.load(PATH)