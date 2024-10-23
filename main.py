# Michael Ostrowski

def encode(password: str):
    # initialize an empty string to store the password
    encoded_password = ""

    # iterate over each character in the password
    for digit in password:
        encoded_digit = (int(digit) + 3)
        encoded_password += str(encoded_digit)

    return encoded_password


# Nicholas Chaves

def decode(encoded_password: str):
    decoded_password=''
    for i in encoded_password:
        decoded_digit=int(i)-3
        if decoded_digit<0:
            decoded_digit+=10
        decoded_password+=str(decoded_digit)
    return decoded_password

def main():
    # initialize variables
    encoded_password = ''
    original_password = ''

    while True:
        # display menu
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        option = int(input('\nPlease enter an option: '))

        if option == 1:
            original_password = input("Please enter your password to encode: ")
            encoded_password = encode(original_password)
            print('Your password has been encoded and stored!')

        elif option == 2:
            decoded_password=decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}')

        elif option == 3:
            break

if __name__ == '__main__':
    main()
