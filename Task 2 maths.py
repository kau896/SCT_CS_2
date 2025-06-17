import cv2
import numpy as np

# Encryption key (keep it secret )
ENCRYPTION_KEY = 123  # You can change this

# Read the image
img = cv2.imread(r"C:\Users\kaumu\Desktop\SkillCraft Technology\task2img.jpg")  # Replace with your file name
if img is None:
    raise ValueError("Image not found! Check path.")

# Encrypt image using XOR
encrypted_img = cv2.bitwise_xor(img, ENCRYPTION_KEY)

# Save encrypted image
cv2.imwrite(r"C:\Users\kaumu\Desktop\SkillCraft Technology\encrypted_image.png", encrypted_img)
print(" Encrypted image saved as 'encrypted_image.png'")

# Decrypt image (same operation since XOR is reversible)
decrypted_img = cv2.bitwise_xor(encrypted_img, ENCRYPTION_KEY)

# Save decrypted image
cv2.imwrite(r"C:\Users\kaumu\Desktop\SkillCraft Technology\decrypted_image.png", decrypted_img)
print(" Decrypted image saved as 'decrypted_image.png'")


cv2.waitKey(0)
cv2.destroyAllWindows()
