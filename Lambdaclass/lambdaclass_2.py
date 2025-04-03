# Write a function called **run_length_encode** that takes a string of uppercase letters as input and returns the run-length encoded version of that string.

# Run-length encoding is a simple form of data compression that replaces consecutive data elements (characters) with a single data value and count.
# For this exercise, a run of data is encoded as the character followed by the number of times it appears.

# **Test cases**

# | **Input string** | **Encoded** |
# | --- | --- |
# | *"AABBBCCCC"* | *"A2B3C4"
# Input string	Encoded
# "AABBBCCCC"	"A2B3C4"
# "WWWWWWWWWWWWBWWWWWWWWWWWWB"	"W12B1W12B1"
# "ABCDE"	"A1B1C1D1E1"
# Your function should handle any string of uppercase letters. If the count of consecutive characters is 1, you should still include the count in the output.

def run_lenght_encode(texto):
    actual = texto[0]
    encodeado = ""
    posicion = 1
    cantidad = 1
    while posicion < len(texto):
        if texto[posicion]  == actual:
            cantidad += 1
        else:
            encodeado += actual + str(cantidad)
            actual = texto[posicion]
            cantidad = 1
        posicion += 1
    return encodeado + actual + str(cantidad)

print(run_lenght_encode("AABBBCCCC"))
print(run_lenght_encode("WWWWWWWWWWWWBWWWWWWWWWWWWB"))
print(run_lenght_encode("ABCDE"))