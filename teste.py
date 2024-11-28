from collections import Counter
import itertools

# Frequência de letras no português
FREQUENCIA_PORTUGUES = "eaosrnidctulmpvghqbfzjxkyw"


# --- Função para Cifra de César ---
def descriptografar_cifra_cesar(texto_cifrado, chave):
    """
    Descriptografa um texto cifrado usando a Cifra de César, dado uma chave.
    :param texto_cifrado: Texto cifrado.
    :param chave: Deslocamento para descriptografar.
    :return: Texto descriptografado.
    """
    texto_decifrado = ""
    for char in texto_cifrado:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            texto_decifrado += chr((ord(char) - base - chave) % 26 + base)
        else:
            texto_decifrado += char
    return texto_decifrado


# --- Função para Cifra de Substituição ---
def descriptografar_cifra_substituicao(texto_cifrado, mapeamento):
    """
    Descriptografa um texto usando a cifra de substituição com um mapeamento fornecido.
    :param texto_cifrado: Texto cifrado.
    :param mapeamento: Dicionário de mapeamento letra-cifrada para letra-real.
    :return: Texto descriptografado.
    """
    texto_decifrado = ""
    for char in texto_cifrado:
        if char.lower() in mapeamento:
            substituto = mapeamento[char.lower()]
            texto_decifrado += substituto.upper() if char.isupper() else substituto
        else:
            texto_decifrado += char
    return texto_decifrado


# --- Função para Cifra de Transposição ---
def descriptografar_cifra_transposicao(texto_cifrado, chave):
    """
    Descriptografa um texto cifrado usando transposição com uma chave fornecida.
    :param texto_cifrado: Texto cifrado.
    :param chave: Tamanho da chave de transposição.
    :return: Texto descriptografado.
    """
    # Calcula o número de colunas e linhas na matriz de transposição
    num_colunas = chave
    num_linhas = len(texto_cifrado) // num_colunas
    if len(texto_cifrado) % num_colunas != 0:
        num_linhas += 1

    # Reorganiza o texto cifrado em colunas
    matriz = ['' for _ in range(num_colunas)]
    idx = 0
    for coluna in range(num_colunas):
        for linha in range(num_linhas):
            if idx < len(texto_cifrado):
                matriz[coluna] += texto_cifrado[idx]
                idx += 1

    # Concatena as colunas para obter o texto original
    texto_decifrado = ''.join(''.join(coluna) for coluna in zip(*matriz))
    return texto_decifrado.strip('_')


# Cifra de César
texto_cifrado_cesar = "Khoor zruog!"
chave_cesar = 3
print("Descriptografado (César):", descriptografar_cifra_cesar(texto_cifrado_cesar, chave_cesar))

# Cifra de Substituição
texto_cifrado_substituicao = "Hqzgu zgu zxgz gzgu!"
mapeamento_substituicao = {'h': 'e', 'q': 's', 'z': 'a', 'g': 'o', 'u': 'r'}  # Exemplo de mapeamento
print("Descriptografado (Substituição):", descriptografar_cifra_substituicao(texto_cifrado_substituicao, mapeamento_substituicao))

# Cifra de Transposição
texto_cifrado_transposicao = "Vemars uscootinq umndo"
chave_transposicao = 5  # Exemplo de chave
print("Descriptografado (Transposição):", descriptografar_cifra_transposicao(texto_cifrado_transposicao, chave_transposicao))
