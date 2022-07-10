# Alfabeto
abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# Frequência de caractéres - Inglês
en_freq = {'A':8.167,'B':1.492,'C':2.782,'D':4.253,'E':12.702,'F':2.228,'G':2.015,'H':6.094,'I':6.966,'J':0.153,'K':0.772,'L':4.025,'M':2.406,'N':6.749,'O':7.507,'P':1.929,'Q':0.095,'R':5.987,'S':6.327,'T':9.056,'U':2.758,'V':0.978,'W':2.360,'X':0.150,'Y':1.974,'Z':0.074}
# Frequência de caractéres - Português
pt_freq = {'A':14.63,'B':1.04,'C':3.88,'D':4.99,'E':12.57,'F':1.02,'G':1.30,'H':1.28,'I':6.18,'J':0.40,'K':0.02,'L':2.78,'M':4.74,'N':5.05,'O':10.73,'P':2.52,'Q':1.20,'R':6.53,'S':7.81,'T':4.34,'U':4.63,'V':1.67,'W':0.01,'X':0.47,'Y':0.01,'Z':0.47}

class CryptoManager:
    def cypher(self, key, plainText):
        self.__add_text(plainText)
        key = self.__process_key(key, self.internalText)
        temp = [abc[(abc.index(self.internalText[i]) + abc.index(key[i])) % 26] for i in range(len(self.internalText))]
        self.internalText = ''.join(temp).upper()
    
    def decypher(self, key, cypherText):
        self.__add_text(cypherText) # TODO
        self.internalText = self.__re_add_spaces(self.internalText)

    def attack(self, lang, cypherText):
        self.__add_text(cypherText) # TODO
        self.internalText = self.__re_add_spaces(self.internalText)
        
    def __add_text(self, text):
        ## Caches where the spaces should be added when printing again
        self.__cache_spaces(text)
        ## Caches the cypher without spaces
        self.internalText = ''.join(text.split(' ')).lower()

    def __cache_spaces(self, text):
        self.spaceIndexes = []
        #### Gets space indexes
        while True:
            index = text.rfind(' ')
            if index != -1:
                text = text[:index]
                self.spaceIndexes.append(index)
            else:
                break
        #### Repositions indexes to match cleaned up string
        new_space_indexes = []
        space_count = len(self.spaceIndexes)
        for i in self.spaceIndexes:
            space_count -= 1
            new_space_indexes.append(i - space_count)
        self.spaceIndexes = new_space_indexes

    def __re_add_spaces(self, text):
        for i in self.spaceIndexes:
            text = text[:i] + ' ' + text[i:]
        return text
    
    def __process_key(self, key, text):
        key = ''.join(key.split(' ')).lower()
        textLen = len(text)
        while (textLen > len(key)):
            key += key
        key = key[:textLen]
        return key

if __name__ == '__main__':
    manager = CryptoManager()
    option = input("Qual opção:\n 1 - Cifrar\n 2 - Decifrar\n 3 - Atacar\n")
    if (option == '1'):
            key = input('Digite a chave: ')
            manager.cypher(key, input('Digite o texto a cifrar: '))
            print(f"Resultado: {manager.internalText}")
    elif (option == '2'):
            key = input('Digite a chave: ')
            manager.decypher(key, input('Digite a cifra: '))
            print(f"Resultado: {manager.internalText}")
    else:
        lang = input('Escolha a língua:\n 0 - Inglês\n 1 - Português\n')
        if (not lang == '0' and not lang == '1'):
            print("Idioma inválido!")
            exit()
        else:
            manager.attack(lang, input('Digite o texto a ser atacado: '))
            print(f"Resultado: {manager.internalText}")
