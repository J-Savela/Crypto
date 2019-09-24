########################################################################################################################
# Problem 1
########################################################################################################################
# The task is to find the invertible elements of Z_20.
# ==> Iterate thru x, y in 0..19 and check whether xy == 1

print(f"PROBLEM 1:")
print(f"Finding multiplicative inverses...\n")
invertibles = set()
for y in range(20):
    for x in range(0, y + 1):
        result = (x * y) % 20
        if result == 1:
            print(f"{x} * {y} = {x * y} = {result}")
            invertibles.add(x)
            invertibles.add(y)

print(f"\nThe invertible elements are {invertibles}.\n\n")

########################################################################################################################
########################################################################################################################


########################################################################################################################
# Problem 3
########################################################################################################################
# The task is to find all primitive roots modulo 17.
# This is equivalent to finding all generators of the multiplicative group of integers modulo 17.
# ==> Thus find all generators...

print(f"PROBLEM 3:")
print(f"Computing generators...\n")
generators = set()
group = set(range(1, 17))
for x in group:
    generated = set()
    newElem = x
    while True:
        if newElem in generated:
            break
        generated.add(newElem)
        newElem = newElem * x % 17
    if generated == group:
        generators.add(x)

print(f"The generators are {generators}.\n\n")

########################################################################################################################
########################################################################################################################


########################################################################################################################
# Problem 4
########################################################################################################################
# The task is to construct a addition/multiplication tables for GF(2^3) using the polynomial x^3 + x^2 + 1.

print(f"PROBLEM 4 part a:")
print(f"Computing the operation tables for GF(2^3) using the polynomial x^3 + x^2 + 1.\n")

# Represent polynomials as lists
field = [[x, y, z] for x in range(2) for y in range(2) for z in range(2)]

# Create a function to add polynomials
def add(x, y):
    length = max(len(x), len(y))
    z = list(map(lambda a: 0, range(length)))
    for i in range(length):
        a = 0
        if i < len(x):
            a += x[i]
        if i < len(y):
            a += y[i]
        z[i] = a % 2
    return z

# Create function to multiply polynomials
def multiply(x, y):
    length = max(len(x), len(y))
    z = list(map(lambda a: 0, range(length)))
    for i in range(len(y)):
        if y[i] == 1:
            z = add(z, list(map(lambda a: 0, range(i))) + x)
    return z

# Create a function that reduces polynomials wrt magic law 1 given by x^3 + x^2 + 1.
def magic_law1(x):
    z = x.copy()
    for i in range(len(x) - 1, 2, -1):
        if z[i] == 1:
            modifier = list(map(lambda a: 0, range(i - 3))) + [1, 0, 1, 1]
            z = add(z, modifier)
    return z

def add_field1(x, y):
    return magic_law1(add(x, y))

def multiply_field1(x, y):
    return magic_law1(multiply(x, y))

# Create function to return nicer representation
def prettyPrint(x):
    return f"{x[2]}{x[1]}{x[0]}"

# Create function to print a table
def createTable(elems, op):
    elems = list(elems)
    # Create header row
    print(f"{'':4}| ", end='')
    for e in elems:
        print(f"{prettyPrint(e):4}", end='')
    print("")
    # Print horizontal line
    print("----|-", end='')
    for i in range(len(elems)):
        print("----", end='')
    print("")
    for x in elems:
        print(f"{prettyPrint(x):4}| ", end='')
        for y in elems:
            print(f"{prettyPrint(op(x, y)):4}", end='')
        print("")

print(f"Addition table:")
createTable(field, add_field1)
print(f"\n\nMultiplication table:")
createTable(field, multiply_field1)
print("\n")


print(f"PROBLEM 4 part b:")
# Make sure the polynomial x^3 + x^2 + 1 is irreducible.

def degree(x):
    for i in range(len(x) - 1, -1, -1):
        if x[i] == 1:
            break
    return i

def trim(x):
    return x[:(degree(x) + 1)]

factor_candidates = [(x, y) for x in field for y in field if degree(x) + degree(y) == 3]
found_factors = False
for x, y in factor_candidates:
    if trim(multiply(x, y)) == [1, 0, 1, 1]:
        found_factors = True
        break
if found_factors:
    print(f"The polynomial is not irreducible!!!!")
else:
    print(f"The polynomial is irreducible!!!!")

print("\n")
########################################################################################################################
########################################################################################################################

########################################################################################################################
# Problem 5
########################################################################################################################
# The task is to construct a addition/multiplication tables for GF(2^3) using the polynomial x^3 + x + 1.

print(f"PROBLEM 5 part a:")
print(f"Computing the operation tables for GF(2^3) using the polynomial x^3 + x + 1.\n")

# Create a function that reduces polynomials wrt magic law 2 given by x^3 + x + 1.
def magic_law2(x):
    z = x.copy()
    for i in range(len(x) - 1, 2, -1):
        if z[i] == 1:
            modifier = list(map(lambda a: 0, range(i - 3))) + [1, 1, 0, 1]
            z = add(z, modifier)
    return z

def add_field2(x, y):
    return magic_law2(add(x, y))

def multiply_field2(x, y):
    return magic_law2(multiply(x, y))

print(f"Addition table:")
createTable(field, add_field2)
print(f"\n\nMultiplication table:")
createTable(field, multiply_field2)
print("\n")


print(f"PROBLEM 5 part b:")


# Define isomorphism candidates
def h1(x):
    a = x[2]
    b = x[1]
    c = x[0]
    y = [0, 0, 0]
    y[0] = (a + b + c) % 2
    y[1] = (a) % 2
    y[2] = (a + b) % 2
    return y


def h2(x):
    a = x[2]
    b = x[1]
    c = x[0]
    y = [0, 0, 0]
    y[0] = (c) % 2
    y[1] = (a + b) % 2
    y[2] = (b) % 2
    return y


def h3(x):
    a = x[2]
    b = x[1]
    c = x[0]
    y = [0, 0, 0]
    y[0] = (a + b + c) % 2
    y[1] = (a + b) % 2
    y[2] = (b) % 2
    return y


# Create function to test a candidate for isomorphism
def test_candidate(candidate):
    still_valid = True
    for x in field:
        if not still_valid:
            break
        for y in field:
            if not still_valid:
                break
            lhs = trim(candidate(multiply_field1(x, y)))
            rhs = trim(multiply_field2(candidate(x), candidate(y)))
            if lhs != rhs:
                print(f"Found a counterexample:\n"
                      f"h({prettyPrint(x)} *_f {prettyPrint(y)}) = {prettyPrint(lhs)}\n"
                      f"h({prettyPrint(x)}) *_g h({prettyPrint(y)}) = {prettyPrint(rhs)}\n"
                      f"{prettyPrint(lhs)} != {prettyPrint(rhs)}\n")
                still_valid = False
            lhs = trim(candidate(add_field1(x, y)))
            rhs = trim(add_field2(candidate(x), candidate(y)))
            if lhs != rhs:
                print(f"Found a counterexample:\n"
                      f"h({prettyPrint(x)} +_f {prettyPrint(y)}) = {prettyPrint(lhs)}\n"
                      f"h({prettyPrint(x)}) +_g h({prettyPrint(y)}) = {prettyPrint(rhs)}\n"
                      f"{prettyPrint(lhs)} != {prettyPrint(rhs)}\n")
                still_valid = False
    if still_valid:
        print(f"Isomorphism laws hold!!!")


print(f"Testing isomorphism candidates:\n")
print(f"Testing candidate 1")
test_candidate(h1)
print(f"\nTesting candidate 2")
test_candidate(h2)
print(f"\nTesting candidate 3")
test_candidate(h3)



########################################################################################################################
########################################################################################################################

