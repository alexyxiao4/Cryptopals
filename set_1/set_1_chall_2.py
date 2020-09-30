

hex_input_one = input("Enter the first hexadecimal string: ")
bytes_input_one = bytes.fromhex(hex_input_one)
hex_input_two = input("Enter the second hexadecimal string: ")
bytes_input_two = bytes.fromhex(hex_input_two)

final_byte = []
for (i, j) in zip(bytes_input_one, bytes_input_two):
    final_byte.append(i ^ j)
list_to_byte = bytes(final_byte)

print(list_to_byte.hex())