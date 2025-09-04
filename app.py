from base64 import b64encode, b64decode

input_str = "Hello, World!"
encoded_bytes = b64encode(input_str.encode('utf-8'))
encoded_str = encoded_bytes.decode('utf-8')
print(f"Encoded: {encoded_str}")
print(f"Decoded: {b64decode(encoded_str).decode('utf-8')}")