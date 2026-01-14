#---encryption function---
def encryption_func(shift1, shift2):
    with open("raw_text.txt", "r") as file:
        text = file.read()
    
    encrypted_text = ""
    
    for ch in text:
        if ch.islower():
            if 'a' <= ch <= 'm':  # a-m shift forward by shift1 * shift2
                shift = shift1 * shift2
                encrypted_text += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            elif 'n' <= ch <= 'z':  # n-z shift backward by shift1 + shift2
                shift = shift1 + shift2
                encrypted_text += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
        elif ch.isupper():
            if 'A' <= ch <= 'M':  # A-M shift backward by shift1
                shift = shift1
                encrypted_text += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            elif 'N' <= ch <= 'Z':  # N-Z shift forward by shift2^2
                shift = shift2 ** 2
                encrypted_text += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        else:
            # Spaces, tabs, newlines, special characters, and numbers remain unchanged
            encrypted_text += ch
    
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)

#---decryption file---
def decryption_func(shift1, shift2):
    with open("encrypted_text.txt", "r") as file:
        text = file.read()

    decrypted_text = ""

    for ch in text:
        if ch.islower():
            if 'a' <= ch <= 'z':
                decrypted_text += chr((ord(ch) - ord('a') - (shift1 * shift2)) % 26 + ord('a'))

        elif ch.isupper():
            if 'A' <= ch <= 'Z':
                decrypted_text += chr((ord(ch) - ord('A') + shift1) % 26 + ord('A'))

        else:
            decrypted_text += ch

    with open("decrypted_text.txt", "w") as file:
        file.write(decrypted_text)


#---Verification function---
def verification_func():
    with open("raw_text.txt", "r") as f1, open("decrypted_text.txt", "r") as f2:
        if f1.read().strip() == f2.read().strip():
            print("Decryption was successful.")
        else:
            print("Decryption was not successful")


#---Main function---
def main():
    shift1 = int(input("shift1: "))
    shift2 = int(input("shift2: "))

    encryption_func(shift1, shift2)
    decryption_func(shift1, shift2)
    verification_func()


if __name__ == "__main__":
    main()
