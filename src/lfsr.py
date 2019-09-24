import math
import array
# Define functions to generate LFSRs based of irreducible polynomials over field F_2


# Function to generate Galois LSFR.
# INPUT: binary tuple/list/array representing an irreducible polynomial
# OUTPUT: python generator
# HOX: if the polynomial is irreducible, the period of the generator will be lower than maximum
def lfsr_galois(irred_poly):
    if type(irred_poly) == int:
        bits = math.ceil(math.log2(irred_poly))
    elif type(irred_poly) in {list, tuple, array.array}:
        bits = len(irred_poly)
        feedback = 0
        for i in range(bits):
            feedback += irred_poly[i] * 2 ** i
    else:
        raise Exception("Input parameter should be given as an integer, or a binary list/tuple/array")

    limit = 2 ** (bits - 1)
    cycle = limit - 1

    def gener():
        state = 1  # Set starting state
        while True:
            yield state
            # Step state
            state = state << 1
            if state >= limit:
                state = state ^ feedback

    return gener(), cycle


# Function to generate Fibonacci LSFR.
# INPUT: binary tuple/list/array representing an irreducible polynomial
# OUTPUT: python generator
# HOX: if the polynomial is irreducible, the period of the generator will be lower than maximum
def lfsr_fibonacci(irred_poly):
    if type(irred_poly) == int:
        bits = math.ceil(math.log2(irred_poly))
    elif type(irred_poly) in {list, tuple, array.array}:
        bits = len(irred_poly)
        mask = 0
        for i in range(bits):
            mask += irred_poly[i] * 2 ** i
    else:
        raise Exception("Input parameter should be given as an integer, or a binary list/tuple/array")

    limit = 2 ** (bits - 1)
    cycle = limit - 1

    def gener():
        state = 1  # Set starting state
        while True:
            yield state
            # Step state
            state = state << 1
            helper = state & mask
            last = 0
            while helper > 0:
                last += helper % 2
                helper = helper // 2
            last = (last % 2)
            state = (state + last) % limit

    return gener(), cycle
