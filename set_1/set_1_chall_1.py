from base64 import b64encode


hex_input = input("Enter the hexadecimal string: ")
byte_input = bytes.fromhex(hex_input)
print(b64encode(byte_input))