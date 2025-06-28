def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char  # keep punctuation, space, digits
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("==== Caesar Cipher Tool ====")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice. Please type 'e' or 'd'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (0-25): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if choice == 'e':
        encrypted = caesar_cipher_encrypt(message, shift)
        print(f"\n🔐 Encrypted Message: {encrypted}")
    else:
        decrypted = caesar_cipher_decrypt(message, shift)
        print(f"\n🔓 Decrypted Message: {decrypted}")

if __name__ == "__main__":
    main()
