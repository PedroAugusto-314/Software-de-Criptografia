from random import randint
from Criptografia import cifras

CIFRAS = {
    0: cifras.cifra_cesar, 
    1: cifras.cifra_transposicao, 
    }

def gerar_chave(etapas: int= 4) -> str:
    """
    Gera uma chave de 16 números aleatórios
    """
    #Gerar lista com 16 números aleatórios de 1 a 9
    key_num = [randint(1,9) for _ in range(etapas*2)]
    
    #Transforma a lista em uma string única    
    key_str = "".join(str(num) for num in key_num )
    
    return key_str

def separar_chave(key) -> str:
    """
    Separa a chave em 8 grupos de 2 caracteres cada, os 8 passos da criptografia
    """
    #Separa a chave em uma lista de 2 em 2 caracteres
    chave_sep = [key[i:i+2] for i in range(0,16,2)]

    return chave_sep

def criptografar(msg: str, key: str, reverse : bool = False) -> str: 
    """
    Criptografa ou descriptografa a mensagem
    """
    chave_separada: list = separar_chave(key) #Separando a chave em grupos, etapas
    
    if reverse: chave_separada.reverse() #Inverte a chave se for descriptografar

    for grupo in chave_separada: #Passando por cada grupo da chave, cada etapa de criptografia
        if grupo:
            opcao, key = int(grupo[0]), int(grupo[1]) #separando a parte da chave
            #escolhendo a função com base no dicionario
            cifra = CIFRAS.get(opcao%2) #1 se for impar, 0 se for par
            #executando a cifra escolhida com os respectivos parametros
            msg = cifra(msg, key, reverse)

    return msg
