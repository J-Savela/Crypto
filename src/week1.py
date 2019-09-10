########################################################################################################################
# Problem 1
########################################################################################################################
# The Caesar substitution cipher has only 26 keys.
# ==> Try all keys

def strToCode(x):
    ints = []
    for c in x:
        ints.append(ord(c)-ord('a'))
    return ints


def codeToStr(x):
    cs = ""
    for i in x:
        cs += chr(i+ord('a'))
    return cs

def caesar(x, offset):
    offset = offset % 26
    code = strToCode(x)
    for i in range(len(code)):
        code[i] = (code[i] + offset) % 26
    return codeToStr(code)

print(f"PROBLEM 1:\n\n"
      f"Ciphertext: 'lyjdlfyltdmpeepceslyyzdlfyl'\n"
      f"Cipher type: Caesar substitution cipher\n\n"
      f"Trying all keys:")

for i in range(26):
    print(f"{i}: {caesar('lyjdlfyltdmpeepceslyyzdlfyl', i)}")

print(f"\nThe plaintxt message is 'anysaunaisbetterthannosauna'\n\n")

########################################################################################################################
########################################################################################################################


########################################################################################################################
# Problem 2
########################################################################################################################
print("Problem 2:\n")

ciphertext = "bpubh ai bhcpc epc rk hkpici ar cbkr"
freq = dict(map(lambda x: (x, 0), "abcdefghijklmnopqrstuvwxyz"))
for i in range(len(ciphertext)):
    if ciphertext[i] != ' ':
        freq[ciphertext[i]] += 1


def replace(cs, repl):
    newtext = ""
    for i in range(len(cs)):
        c = cs[i]
        if c == ' ':
            newtext += c
            continue
        if c not in repl.keys():
            newtext += '-'
        else:
            newtext += repl[c]
    return newtext


print(replace(ciphertext, {'p': 't', 'c': 'e'}))
print(replace(ciphertext, {'p': 't', 'c': 'e', 'e': 'a'}))
print(replace(ciphertext, {'p': 'r', 'c': 'e', 'e': 'a'}))
print(replace(ciphertext, {'p': 'r', 'c': 'e', 'e': 'a', 'b': 't', 'h': 'h'}))
print(replace(ciphertext, {'p': 'r', 'c': 'e', 'e': 'a', 'b': 't', 'h': 'h', 'u': 'u'}))
print(replace(ciphertext, {'p': 'r', 'c': 'e', 'e': 'a', 'b': 't', 'h': 'h', 'u': 'u', 'a': 'i', 'i': 's'}))
print(replace(ciphertext, {'p': 'r', 'c': 'e', 'e': 'a', 'b': 't', 'h': 'h', 'u': 'u', 'a': 'i', 'i': 's', 'k': 'o'}))
print(replace(ciphertext, {'p': 'r', 'c': 'e', 'e': 'a', 'b': 't', 'h': 'h', 'u': 'u', 'a': 'i', 'i': 's', 'k': 'o', 'r': 'n'}))
########################################################################################################################
########################################################################################################################

