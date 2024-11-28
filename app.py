from collections import Counter
import itertools

# Frequência de letras no português
FREQUENCIA_PORTUGUES = "eaosrnidctulmpvghqbfzjxkyw"

def ataque_cifra_substituicao(texto_cifrado):
    """
    Tenta decifrar uma cifra de substituição com base na frequência de letras.
    """
    frequencia_cifrada = Counter(filter(str.isalpha, texto_cifrado.lower()))
    mapeamento = {cifrado: claro for cifrado, claro in zip(
        [x[0] for x in frequencia_cifrada.most_common()],
        FREQUENCIA_PORTUGUES
    )}
    texto_decifrado = ""
    for char in texto_cifrado:
        if char.lower() in mapeamento:
            substituto = mapeamento[char.lower()]
            texto_decifrado += substituto.upper() if char.isupper() else substituto
        else:
            texto_decifrado += char
    return texto_decifrado


def ataque_cifra_transposicao(texto_cifrado, max_tamanho_chave=10):
    """
    Tenta decifrar uma cifra de transposição por força bruta.
    """
    possibilidades = []
    texto_cifrado = texto_cifrado.replace(" ", "")  # Remove espaços
    for tamanho_chave in range(2, max_tamanho_chave + 1):
        linhas = [texto_cifrado[i:i + tamanho_chave] for i in range(0, len(texto_cifrado), tamanho_chave)]
        for permutacao in itertools.permutations(range(tamanho_chave)):
            tentativa = ""
            for linha in linhas:
                for idx in permutacao:
                    if idx < len(linha):
                        tentativa += linha[idx]
            possibilidades.append((tamanho_chave, tentativa))
    return possibilidades


def ataque_cifra_cesar(texto_cifrado):
    """
    Tenta decifrar uma cifra de César testando todas as 26 chaves possíveis.
    """
    tentativas = []
    for chave in range(26):
        texto_tentativa = ""
        for char in texto_cifrado:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                texto_tentativa += chr((ord(char) - base - chave) % 26 + base)
            else:
                texto_tentativa += char
        tentativas.append((chave, texto_tentativa))
    return tentativas


# Exemplo de uso
texto_cifrado_cesar = "Khoor zruog!"
texto_cifrado_substituicao = "Hqzgu zgu zxgz gzgu!"
texto_cifrado_transposicao = "Vemars uscootinq umndo"

# Ataque à cifra de César
print("Ataque à cifra de César:")
tentativas_cesar = ataque_cifra_cesar(texto_cifrado_cesar)
for chave, texto in tentativas_cesar:
    print(f"Chave {chave}: {texto}")

# Ataque à cifra de substituição
print("\nAtaque à cifra de substituição:")
texto_substituicao = ataque_cifra_substituicao(texto_cifrado_substituicao)
print(texto_substituicao)

# Ataque à cifra de transposição
print("\nAtaque à cifra de transposição:")
possibilidades_transposicao = ataque_cifra_transposicao(texto_cifrado_transposicao)
for chave, tentativa in possibilidades_transposicao[:5]:
    print(f"Chave {chave}: {tentativa}")
