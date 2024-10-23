"""
Cifras para a criptografia
"""
from math import ceil #função que arredonda pra cima

def cifra_cesar(msg: str, key:int, reverse: bool = False) -> str:
    """
    Cifra de César simples com base em Unicode
    """
    #Se reverse for true, executa a função de descriptografar
    if reverse: 
        key = -key
    
    #Faz a cifra de cesar, converte em unicode, soma com a chave e converte de volta, faz isso para cada caractere
    msg_cifrada = ""
    for c in msg:
        uni_c = ord(c) #Converte em código unicode
        carac_c = chr(uni_c + key) #Soma com a key (deslocamento) e converte de volta em caractere
        msg_cifrada += carac_c #Adiciona na mensagem


    return msg_cifrada


def cifra_transposicao(msg: str, key:int, reverse: bool = False) -> str:
    """
    Cifra de transposição simples com base na chave como número de colunas
    """

    if reverse:
        return cifra_transposicao_descriptografar(msg, key)
    
    #Adiciona espaço em branco na mensagem se faltar caractere para preencher a matriz
    while len(msg) % key != 0:
        msg+=' '

    matriz = []
    for i in range(0,len(msg),key):
        #Divide a mensagem em grupos do tamanho da chave, a quantidade de colunas
        msg_separada = (msg[i:i+key]) 

        #Cria uma linha da matriz separando os caracteres
        linha = ["".join(caractere) for caractere in msg_separada] 
        matriz.append(linha)

    msg_criptografada = '' #iniciando a mensagem como string vazia
    for linha in range(len(matriz[0])): #passando pelas linhas da matriz
        for coluna in range(len(matriz)): #passando pelas colinas
            msg_criptografada += matriz[coluna][linha] #pega o caractere da linha e coluna atual e soma na string

    return msg_criptografada

def cifra_transposicao_descriptografar(msg: str, key: int) -> str:
    """
    descriptografa a cifra de transposição
    """
    key = int(key)
    
    #Adiciona espaço em branco na mensagem se faltar caractere para preencher a matriz
    while len(msg) % key != 0:
        msg+=' '

    #Calcular número de linhas
    num_linha = ceil(len(msg)/key)

    #Criar matriz vazia, precisa fazer isso pq aqui a gente preenche coluna por coluna
    matriz = [[] for _ in range(num_linha)]
    #Organizando mensagem na matriz
    num_msg = 0
    for _ in range(key): #Passando pelas colunas
        for linha in range(num_linha): #Passando pelas linhas
            matriz[linha].append(msg[num_msg]) #Adiciona um caractere da mensagem na linha
            num_msg += 1 #Passa pro próximo caractere da mensagem

    #Organizando a matriz na mensagem, linha a linha
    msg_descriptografada = ""
    for l in range(num_linha):
        for c in range(key):
            msg_descriptografada += matriz[l][c]
            

    return msg_descriptografada.strip() #Remove aqueles espaços adicionados anteriormente


if __name__ == "__main__":
    msg = cifra_transposicao("Hello, World!", 5)
    print(f"[{msg}]")
    msg_desc = cifra_transposicao_descriptografar(msg, 5)
    print(f"[{msg_desc}]")