from PIL import Image
import os

def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Simple math operation with key (mod 256 to stay in RGB range)
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save(output_path)
    print(f"[✔] Image encrypted and saved to {output_path}")

def decrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Revert the encryption
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save(output_path)
    print(f"[✔] Image decrypted and saved to {output_path}")

def main():
    print("=== Simple Image Encryptor/Decryptor ===")
    choice = input("Choose operation (e = encrypt, d = decrypt): ").lower()
    
    if choice not in ('e', 'd'):
        print("Invalid option.")
        return

    image_path = input("Enter path to image: ")
    if not os.path.exists(image_path):
        print("File not found.")
        return

    try:
        key = int(input("Enter numeric key (1-255): "))
        if not (1 <= key <= 255):
            raise ValueError
    except ValueError:
        print("Invalid key. Use an integer between 1 and 255.")
        return

    output_path = input("Enter output file name (e.g., output.png): ")

    if choice == 'e':
        encrypt_image(image_path, key, output_path)
    else:
        decrypt_image(image_path, key, output_path)

if __name__ == "__main__":
    main()
