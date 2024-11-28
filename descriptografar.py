import string

def descriptografar_cifra_de_cesar(texto, deslocamento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            deslocamento_base = 65 if char.isupper() else 97
            resultado += chr((ord(char) - deslocamento_base - deslocamento) % 26 + deslocamento_base)
        else:
            resultado += char
    return resultado

def descriptografar_cifra_substituicao(texto, chave_substituicao):
    alfabeto = string.ascii_lowercase
    chave_substituicao = chave_substituicao.lower()
    mapa_substituicao_invertido = {v: k for k, v in zip(alfabeto, chave_substituicao)}

    resultado = ""
    for char in texto:
        if char.isalpha():
            char_lower = char.lower()
            novo_char = mapa_substituicao_invertido[char_lower]
            if char.isupper():
                resultado += novo_char.upper()
            else:
                resultado += novo_char
        else:
            resultado += char
    return resultado

def descriptografar_cifra_transposicao(ciphertext, key):
    num_rows = len(ciphertext) // key
    num_extra_chars = len(ciphertext) % key
    matrix = ['' for _ in range(num_rows + (1 if num_extra_chars > 0 else 0))]
    index = 0
    for col in range(key):
        for row in range(num_rows):
            matrix[row] += ciphertext[index]
            index += 1
        if col < num_extra_chars:
            matrix[-1] += ciphertext[index]
            index += 1
    return ''.join(matrix)

texto_cesar = "Whawr gh hahpsor"
deslocamento = 3
print(descriptografar_cifra_de_cesar(texto_cesar, deslocamento))

texto_criptografado_substituicao = "Ispih ws spsgnch"
chave_substituicao = "qazwsxrfvtycgbhnujmikolp"
print(descriptografar_cifra_substituicao(texto_criptografado_substituicao, chave_substituicao))

texto_criptografado_transposicao = "Toxledeoxemtep"
chave = 4
print(descriptografar_cifra_transposicao(texto_criptografado_transposicao, chave))
