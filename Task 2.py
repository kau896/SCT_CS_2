from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(r"C:\Users\kaumu\Desktop\SkillCraft Technology\task2img.jpg")
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and blue channels
            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel

    img.save(r"C:\Users\kaumu\Desktop\SkillCraft Technology\encrypted_image.jpg")
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(r"C:\Users\kaumu\Desktop\SkillCraft Technology\encrypted_image.jpg")
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and blue channels back
            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel

    img.save(r"C:\Users\kaumu\Desktop\SkillCraft Technology\decrypted_image.jpg")
    print("Image decrypted successfully!")

 # image path
input_image = r"C:\Users\kaumu\Desktop\SkillCraft Technology\task2img.jpg"
encrypted_image = r"C:\Users\kaumu\Desktop\SkillCraft Technology\decrypted_image.jpg"
decrypted_image = r"C:\Users\kaumu\Desktop\SkillCraft Technology\encrypted_image.jpg"


# Encrypt the image
encrypt_image(input_image, encrypted_image, key=None)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image, key=None)