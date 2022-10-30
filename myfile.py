#Convert Text to Binary Format


message = "Hello World!"
binary = " ".join(format(ord(c), "b") for c in message)
print(binary)

#--------------------------------------------------------
#Convert  Binary to text Format

binary_txt = "1001000 1100101 1101100 1101100 1101111 100000 1010111 1101111 1110010 1101100 1100100 100001"
nrml_txt = "".join(chr(int(c,2)) for c in binary_txt.split(" "))
print(nrml_txt)