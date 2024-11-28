import string

def cifra_de_cesar(texto, deslocamento):
    resultado = ""
    
    for char in texto:
        if char.isalpha():
            deslocamento_base = 65 if char.isupper() else 97
            resultado += chr((ord(char) - deslocamento_base + deslocamento) % 26 + deslocamento_base)
        else:
            resultado += char

    return resultado

def cifra_substituicao(texto, chave_substituicao):
    alfabeto = string.ascii_lowercase
    chave_substituicao = chave_substituicao.lower()
    mapa_substituicao = dict(zip(alfabeto, chave_substituicao))
    
    resultado = ""
    
    for char in texto:
        if char.isalpha():
            char_lower = char.lower()
            novo_char = mapa_substituicao[char_lower]
            
            if char.isupper():
                resultado += novo_char.upper()
            else:
                resultado += novo_char
        else:
            resultado += char
    
    return resultado

def cifra_transposicao(texto, chave):
    texto = texto.replace(" ", "")
    n_linhas = len(texto) // chave + (1 if len(texto) % chave != 0 else 0)
    matriz = ['' for _ in range(n_linhas)]
    for i, char in enumerate(texto):
        linha = i % n_linhas
        matriz[linha] += char
    
    return ''.join(matriz)

texto = "Texto de exemplo"
deslocamento = 3
print(cifra_de_cesar(texto, deslocamento))  

chave = "qazwsxrfvtycgbhnujmikolp"
print(cifra_substituicao(texto, chave))  

chave = 4
print(cifra_transposicao(texto, chave))
