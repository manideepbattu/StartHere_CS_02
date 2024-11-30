from PIL import Image
import random

def load_image(file_path):
    img = Image.open(file_path).convert('RGB')
    return img

def get_pixel_data(img):
    width, height = img.size
    pixels = list(img.getdata())
    return pixels, width, height

def encrypt_pixels(pixels, key):
    random.seed(key)
    encrypted_pixels = pixels[:]
    random.shuffle(encrypted_pixels)
    return encrypted_pixels

def decrypt_pixels(encrypted_pixels, key):
    random.seed(key)
    indices = list(range(len(encrypted_pixels)))
    random.shuffle(indices)
    decrypted_pixels = [None] * len(encrypted_pixels)
    for i, pixel_index in enumerate(indices):
        decrypted_pixels[pixel_index] = encrypted_pixels[i]
    return decrypted_pixels

def reconstruct_image(pixels, width, height):
    img = Image.new('RGB', (width, height))
    img.putdata(pixels)
    return img

# Example usage
file_path = 'image.jpg'  # Provide a valid path to an image
key = 1234  # Example key

try:
    img = load_image(file_path)
    pixels, width, height = get_pixel_data(img)

    # Encryption
    encrypted_pixels = encrypt_pixels(pixels, key)
    encrypted_img = reconstruct_image(encrypted_pixels, width, height)
    encrypted_img.save('encrypted_image.png')

    # Decryption
    decrypted_pixels = decrypt_pixels(encrypted_pixels, key)
    decrypted_img = reconstruct_image(decrypted_pixels, width, height)
    decrypted_img.save('decrypted_image.png')

    print("Encryption and decryption completed successfully.")
except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
