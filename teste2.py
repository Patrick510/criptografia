# --- Cifra de Substituição ---
def descriptografar_cifra_substituicao(texto_cifrado, mapeamento):
    """
    Descriptografa um texto cifrado usando a cifra de substituição com um mapeamento fornecido.
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
            texto_decifrado += char  # Mantém caracteres não mapeados
    return texto_decifrado


# --- Cifra de Transposição ---
def descriptografar_cifra_transposicao(texto_cifrado, chave):
    """
    Descriptografa um texto cifrado usando transposição com uma chave fornecida.
    :param texto_cifrado: Texto cifrado.
    :param chave: Tamanho da chave de transposição.
    :return: Texto descriptografado.
    """
    # Calcula o número de linhas e colunas
    num_colunas = chave
    num_linhas = -(-len(texto_cifrado) // num_colunas)  # Arredonda para cima
    num_vazios = num_colunas * num_linhas - len(texto_cifrado)

    # Preenche a matriz de transposição com os caracteres
    matriz = []
    idx = 0
    for i in range(num_linhas):
        linha = texto_cifrado[idx:idx + num_colunas]
        matriz.append(linha)
        idx += num_colunas

    # Corrige a última linha para ignorar vazios
    for i in range(num_vazios):
        matriz[-1] = matriz[-1][:-1]

    # Reconstrói o texto decifrado lendo por colunas
    texto_decifrado = ""
    for coluna in range(num_colunas):
        for linha in matriz:
            if coluna < len(linha):
                texto_decifrado += linha[coluna]
    return texto_decifrado


# Teste das Funções
# Cifra de Substituição
texto_cifrado_substituicao = "Hqzgu zgu zxgz gzgu!"
mapeamento_substituicao = {'h': 'e', 'q': 's', 'z': 'a', 'g': 'o', 'u': 'r'}
print("Descriptografado (Substituição):", descriptografar_cifra_substituicao(texto_cifrado_substituicao, mapeamento_substituicao))

# Cifra de Transposição
texto_cifrado_transposicao = "Vemars uscootinq umndo"
chave_transposicao = 5
print("Descriptografado (Transposição):", descriptografar_cifra_transposicao(texto_cifrado_transposicao, chave_transposicao))
