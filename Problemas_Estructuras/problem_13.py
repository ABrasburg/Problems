# This problem was asked by Amazon.
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
def longest_substring_fuerza_bruta(s, k):
    if k >= len(s):
        return s
    todas = []
    letras = []
    inicio = True
    actual = ""
    for c in s:
        if actual == "":
            actual += c
            letras.append(c)
            continue
        if inicio:
            if c not in actual:
                letras.append(c)
                inicio = False
            actual += c
            continue
        if c in actual:
            actual += c
            continue
        todas.append(actual)
        while len(letras) == k:
            actual = actual[1:]
            for letra in letras:
                if letra not in actual:
                    letras.remove(letra)
        actual += c
        letras.append(c)
    todas.append(actual)
    max = ""
    for posibilidad in todas:
        if len(posibilidad) > len(max):
            max = posibilidad
    return max

def longest_substring_ventana(s, k): #para no  usar slicing
    if not s or k <= 0:
        return ""
    if k >= len(set(s)):
        return s
    char_count = {}
    
    # Variables para la ventana deslizante
    start = 0
    max_length = 0
    max_start = 0
    
    for end in range(len(s)):
        char_count[s[end]] = char_count.get(s[end], 0) + 1
        while len(char_count) > k:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start += 1
        if end - start + 1 > max_length:
            max_length = end - start + 1
            max_start = start
    
    return s[max_start:max_start + max_length]

print(longest_substring_fuerza_bruta("abcba", 2))
print(longest_substring_ventana("abcba", 2))