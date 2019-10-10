

########################################################################################################################
# Problem 1
########################################################################################################################
# The task is to

print(f"PROBLEM 1:")
print(f"Simulating Diffie-Hellman...\n")

# parameters
p = 43
g = 5
a = 13
b = 11

print(f"The chosen g is a generator because gcd(p, g) = 1\n")

a_to_b = (g ** a) % p
b_to_a = (g ** b) % p

print(f"Alice sends g^a = {a_to_b} to Bob.")
print(f"Bob sends g^b = {b_to_a} to Alice.\n")

key_a = (b_to_a ** a) % p
key_b = (a_to_b ** b) % p

print(f"Alice computes {b_to_a}^a = {key_a}.")
print(f"Bob computes {a_to_b}^b = {key_b}.\n")


########################################################################################################################
########################################################################################################################


########################################################################################################################
# Problem 2
########################################################################################################################
# The task is to

print(f"PROBLEM 2:")
print(f"Simulating El Gamal encryption...\n")

# parameters
p = 43
g = 5
a = 11
b = 29
m = 22

pubk_a = (g ** a) % p
prik_a = a
pubk_b = (g ** b) % p
prik_b = b



print(f"First the public parameters are agreed on:\n"
      f"The prime p = {p}\n"
      f"Generator g = {g}\n"
      f"Alice's public key g^a = 5^11 = {pubk_a}\n")

shared_secret_b = (pubk_a ** b) % p
shared_secret_a = (pubk_b ** a) % p
s = shared_secret_b * m % p
print(f"Bob wants to send message (m = {m}) to Alice using El Gamal encryption.\n"
      f"First bob decides b = {b} and computes:\n"
      f"1) r = g^b = {pubk_b}\n"
      f"2) g^(ab) = (g^a)^b = {shared_secret_b}\n"
      f"3) s = g^(ab)m = {s}\n")

print(f"Bob then send (r, s) to Alice.\n")

inv_key = 2
while inv_key < p:
    if inv_key * shared_secret_a % p == 1:
        break
    else:
        inv_key += 1
if inv_key * shared_secret_a % p != 1:
    raise Exception("Something went wrong...")

message = inv_key * s % p
print(f"Alice computes:\n"
      f"1) g^(ab) = r^a = {shared_secret_a}\n"
      f"2) k = (g^(ab))^-1 = {inv_key}\n"
      f"3) message = k * s = {message}")



########################################################################################################################
########################################################################################################################
