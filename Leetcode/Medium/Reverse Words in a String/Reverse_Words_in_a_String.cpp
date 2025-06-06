#include <string>
#include <sstream>
#include <vector>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        // Usamos stringstream para separar palabras por espacios
        stringstream ss(s);
        string word;
        vector<string> words;

        // Extraemos las palabras, ignorando espacios múltiples
        while (ss >> word) {
            words.push_back(word);
        }

        // Construimos el string resultado con las palabras invertidas
        string reversed;
        for (int i = (int)words.size() - 1; i >= 0; i--) {
            reversed += words[i];
            if (i != 0) {
                reversed += " ";
            }
        }

        return reversed;
    }
};
