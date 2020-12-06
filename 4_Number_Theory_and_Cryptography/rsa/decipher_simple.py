from encrypt import Encrypt


def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
    for potential_message in potential_messages:
        if ciphertext == Encrypt(potential_message, modulo, exponent):
            return potential_message
    return "don't know"


modulo = 101
exponent = 12

for msg in ["attack", "don't attack", "wait"]:
    ciphertext = Encrypt(msg, modulo, exponent)
    print(msg)
    print(ciphertext)
    print(DecipherSimple(ciphertext, modulo, exponent, ["attack", "don't attack", "wait"]))
