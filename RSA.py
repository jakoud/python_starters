import random
import Crypto.Util.number as crypto


def greatest_common_divisor(number1, number2):
    while number2 != 0:
        number1, number2 = number2, number1 % number2

    return number1


def generate_keys():
    p = crypto.getPrime(8)
    q = crypto.getPrime(8)

    while q == p:
        q = crypto.getPrime(8)

    n = p*q
    phi = (p-1)*(q-1)

    e = random.randint(1, phi)
    while greatest_common_divisor(phi, e) != 1:
        e = random.randint(1, phi)

    for i in range(1, phi+1):
        d = int((i*phi+1)/e)
        if d*e % phi == 1:
            break

    return (n, e), (n, d)


def main():
    print("This is an algorithm showing RSA encryption/decryption")
    message = str(input('Type in your message:  '))
    public_key, private_key = generate_keys()

    encrypted_list = [str((ord(letter)**public_key[1]) % public_key[0]) for letter in message]
    print('Your encrypted string is:    ', ''.join(encrypted_list))

    decrypted_list = [chr((int(number)**private_key[1]) % private_key[0]) for number in encrypted_list]
    print('Your decrypted string is:    ', ''.join(decrypted_list))


main()
