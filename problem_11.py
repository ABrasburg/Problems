# This problem was asked by Twitter.
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

class Autocompletar:
    def __init__(self, palabras):
        self.completar = {}
        for palabra in palabras:
            parcial = ""
            for caracter in palabra:
                parcial += caracter
                lista = self.completar.get(parcial, [])
                if palabra in lista:
                    continue
                lista.append(palabra)
                self.completar[parcial] = lista

    def obtener(self, prefijo):
        return self.completar.get(prefijo, [])
    
autocompletar = Autocompletar(["dog", "deer", "deal"])
print(autocompletar.obtener("de"))
    