import src.lfsr as lfsr

########################################################################################################################
# Problem 1
########################################################################################################################
# The task is to

print(f"PROBLEM 1:")
print(f"Finding multiplicative inverses...\n")

# irreducible polynomial is x^8 + x^4 + x^3 + x + 1
irred_poly = [1, 1, 0, 1, 1, 0, 0, 0, 1]
gener, cycle = lfsr.lfsr_galois(irred_poly)
l1 = []
# find and skip unit
while next(gener) != 1:
    continue
# Save the elements in the order generated
while True:
    e = next(gener)
    if e == 1:
        break
    else:
        l1.append(e)

# Create dict that maps each element to its (multiplicative) inverse
l2 = l1.copy()
l2.reverse()
mult_inv = dict(zip(l1, l2))


def mult_inv_hex(x):
    return hex(mult_inv[int(x, 16)])

print(f"The multiplicative inverse of {hex(0x02)} is {mult_inv_hex('02')}.")
print(f"The multiplicative inverse of {hex(0x40)} is {mult_inv_hex('40')}.")

########################################################################################################################
########################################################################################################################

########################################################################################################################
# Problem 6
########################################################################################################################
#

print(f"PROBLEM 6:\n")

# Define the encryption and decryption functions
lookup_sbox = {0: 4,
              1: 3,
              2: 5,
              3: 6,
              4: 1,
              5: 0,
              6: 7,
              7: 2}

lookup_sbox_inv = dict(map(lambda p: (p[1], p[0]), lookup_sbox.items()))


def sbox(x):
    if x not in lookup_sbox.keys():
        return None
    else:
        return lookup_sbox[x]


def sbox_inv(x):
    if x not in lookup_sbox_inv.keys():
        return None
    else:
        return lookup_sbox_inv[x]


def enc1(x, key):
    if x > 7 or key > 7:
        raise Exception(f"Illegal arguments!")
    state = x ^ key
    state = sbox(state)
    x3 = state % 2
    x2 = state // 2 ** 1 % 2
    x1 = state // 2 ** 2 % 2
    state = x1 * 2 ** 2 + x3 * 2 + x2
    return state


def dec1(x, key):
    if x > 7 or key > 7:
        raise Exception(f"Illegal arguments!")
    state = x
    x3 = state % 2
    x2 = state // 2 ** 1 % 2
    x1 = state // 2 ** 2 % 2
    state = x1 * 2 ** 2 + x3 * 2 + x2
    state = sbox_inv(state)
    state = state ^ key
    return state


def enc2(x, key):
    state = x ^ key
    state = sbox(state)
    state = state ^ key
    return state


def dec2(x, key):
    state = x ^ key
    state = sbox_inv(state)
    state = state ^ key
    return state

# The following is known:
#   0 should map to 2 (over e1+e2)
#   7 should map to 1 (over e1+e2)

print("Encrypting 0 using different keys and decrypting 2 using different keys.")

# Try encrypting 0 using different keys
table_0 = dict(map(lambda k: (enc1(0, k), k), range(8)))

# Check the result from decrypting 2 using different keys
# Prune the entries of table_enc1_0
key_candidates = set()
for k in range(8):
    p = dec2(2, k)
    if p in table_0.keys():
        key_cand = (table_0[p], k)
        key_candidates.add(key_cand)

print(f"The keys the match in the middle are\n {key_candidates}.\n")
print("Encrypting 7 using different keys and decrypting 1 using different keys.")

# Try encrypting 7 using different keys
table_7 = dict(map(lambda k: (enc1(7, k), k), range(8)))

# Check the result from decrypting 1 using different keys
# Prune the entries of table_7
key_candidates_2 = set()
for k in range(8):
    p = dec2(1, k)
    if p in table_7.keys():
        key_cand = (table_7[p], k)
        key_candidates_2.add(key_cand)

print(f"The keys the match in the middle are\n {key_candidates_2}.\n")

key_candidates_3 = key_candidates.intersection(key_candidates_2)

print(f"The intersection of these candidate sets is {key_candidates_3}. "
      f"Let's try these different keys to see if any of them are a match.\n")

for k1, k2 in key_candidates_3:
    print(f"{(k1, k2)}: encrypt({0}) = {enc2(enc1(0, k1), k2)}")
    print(f"{(k1, k2)}: encrypt({7}) = {enc2(enc1(7, k1), k2)}")


########################################################################################################################
########################################################################################################################

