import streamlit as st
import cv2
import numpy as np
from cryptography.fernet import Fernet
import base64

# Function to generate an encryption key
def generate_key(passcode):
    key = base64.urlsafe_b64encode(passcode.ljust(32).encode()[:32])
    return key

# Encrypt message
def encrypt_message(message, passcode):
    key = generate_key(passcode)
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    return encrypted

# Decrypt message
def decrypt_message(encrypted_message, passcode):
    key = generate_key(passcode)
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_message).decode()
    return decrypted

# Encode message into image
def encode_message(img, message, passcode):
    encrypted_message = encrypt_message(message, passcode)
    message_bytes = encrypted_message

    message_length = len(message_bytes)
    length_bin = format(message_length, '032b')

    flat_img = img.flatten()
    
    for i in range(32):
        flat_img[i] = (flat_img[i] & ~1) | int(length_bin[i])

    byte_index = 0
    bit_index = 0

    for i in range(32, len(flat_img)):
        if byte_index >= len(message_bytes):
            break

        bit = (message_bytes[byte_index] >> (7 - bit_index)) & 1
        flat_img[i] = (flat_img[i] & ~1) | bit

        bit_index += 1
        if bit_index == 8:
            bit_index = 0
            byte_index += 1

    encoded_img = flat_img.reshape(img.shape)
    return encoded_img

# Decode message from image
def decode_message(img, passcode):
    flat_img = img.flatten()

    length_bin = ''.join([str(flat_img[i] & 1) for i in range(32)])
    message_length = int(length_bin, 2)

    message_bytes = bytearray()
    current_byte = 0
    bit_index = 0

    for i in range(32, 32 + message_length * 8):
        if i >= len(flat_img):
            break

        current_byte = (current_byte << 1) | (flat_img[i] & 1)
        bit_index += 1

        if bit_index == 8:
            message_bytes.append(current_byte)
            current_byte = 0
            bit_index = 0

    try:
        decrypted_message = decrypt_message(bytes(message_bytes), passcode)
        return decrypted_message
    except Exception as e:
        return f"Decryption failed: {str(e)}"

# Streamlit UI
st.title("🔐 Steganography Tool")

option = st.selectbox("Choose an option:", ["Encode Message", "Decode Message"])

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if option == "Encode Message":
        message = st.text_area("Enter the secret message:")
        passcode = st.text_input("Enter passcode:", type="password")

        if st.button("Encode & Download"):
            encoded_img = encode_message(img, message, passcode)
            cv2.imwrite("encoded_image.png", encoded_img)
            st.success("Message encoded successfully!")
            st.download_button("Download Encoded Image", open("encoded_image.png", "rb"), file_name="encoded_image.png")

    elif option == "Decode Message":
        passcode = st.text_input("Enter passcode:", type="password")

        if st.button("Decode Message"):
            decoded_message = decode_message(img, passcode)
            st.info(f"Decoded Message: {decoded_message}")
