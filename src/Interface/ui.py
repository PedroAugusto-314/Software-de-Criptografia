import customtkinter as ctk
from Criptografia import criptografia 

#Constantes
CIANO_CLARO = "#9ff3fc"
TRANSPARENTE = "transparent"
BRANCO = "white"
CIANO = "#1dcaf5"
TECLA_ENTER = "<Return>"
NORMAL = ctk.NORMAL
BLOQUEADO = ctk.DISABLED
FONTE_PADRAO = ("Roboto", 14)

#Inicializando a janela
janela = ctk.CTk()

#Configurações iniciais da janela
janela.geometry("500x300+500+250")
janela.title("APS 2024/2")
janela.resizable(False, False)
janela.iconbitmap(r"src\Drone.ico")

#Funções dos botões
def escolher_arquivo() -> str:
    """
    Escolhe um arquivo txt e coloca o quem tem dentro no campo da mensagem
    """
    arquivo = ctk.filedialog.askopenfilename(title="Escolher arquivo", filetypes=[("Arquivos de texto", "*.txt")])
    with open(arquivo, 'r') as arq:
        mensagem = arq.read()
    campo_mensagem.insert(ctk.END,mensagem)

#Para desmarcar os check box
def desmarcar_cript() -> None:
    check_criptografar.deselect()
def desmarcar_descript() -> None:
    check_descriptografar.deselect()

#Copiar textos dos campos de chave e resultado
def copiar_chave():
    janela.clipboard_clear()
    janela.clipboard_append(campo_chave.get())
def copiar_Resultado():
    janela.clipboard_clear()
    janela.clipboard_append(campo_resultado.get("1.0", ctk.END))


def criptografar(event=None) -> str:
    """
    Pega as informações dos campos, criptografa a mensagem e mostra o resultado
    """
    mensagem = campo_mensagem.get("1.0", ctk.END).replace('\n','')
    chave = campo_chave.get()
    if len(chave) < 2:
        chave = criptografia.gerar_chave()
        campo_chave.insert(0,chave)

    if check_criptografar.get():
        mensagem_criptografada = criptografia.criptografar(mensagem, chave)
    elif check_descriptografar:
        mensagem_criptografada = criptografia.criptografar(mensagem, chave, True)
    else:
        mensagem_criptografada = "Escolha se quer criptografar ou descriptografar"

    campo_resultado.configure(state=NORMAL)
    campo_resultado.delete("1.0",ctk.END)
    campo_resultado.insert(ctk.END, mensagem_criptografada)
    campo_resultado.configure(state=BLOQUEADO)

    
#Inicializando Widgets
#Texto
texto_principal = ctk.CTkLabel(master=janela,font=("Comic Sans MS", 21), 
                               text="Criptografar ou descriptografar a mensagem")
texto_principal.place(x=30,y=1)

#Frame principal
main_frame = ctk.CTkFrame(master=janela, width=450, height=250,fg_color=None, 
                          bg_color=TRANSPARENTE, border_color=CIANO_CLARO, border_width=2)
main_frame.place(x=25, y=35)

#Campo para escrever mensagem
ctk.CTkLabel(master=main_frame, text="Mensagem", font=FONTE_PADRAO).place(x=75,y=2)
campo_mensagem = ctk.CTkTextbox(master=main_frame, width=200, height=80, font=FONTE_PADRAO, 
                                border_color=CIANO, border_width=2)
campo_mensagem.place(x=20,y=30)

#Campo do resultado da criptografia
ctk.CTkLabel(master=main_frame, text="Resultado", font=FONTE_PADRAO).place(x=300,y=2)
campo_resultado = ctk.CTkTextbox(master=main_frame, width=200, height=80, font=FONTE_PADRAO, 
                                border_color=CIANO, border_width=2, state=BLOQUEADO)
campo_resultado.place(x=230,y=30)

#Campo para escrever a chave
campo_chave = ctk.CTkEntry(master=main_frame, width=200, placeholder_text="Chave...",
                              font=FONTE_PADRAO, border_color=CIANO, placeholder_text_color=CIANO_CLARO)
campo_chave.place(x=20,y=120)

#Check box criptografar
check_criptografar = ctk.CTkCheckBox(master=main_frame, text="Criptografar", font=FONTE_PADRAO, checkbox_width=15, 
                                     checkbox_height=15, corner_radius=200, border_width=2, command=desmarcar_descript)
check_criptografar.place(x=270,y=180)
check_criptografar.select()

#Check box descriptografar
check_descriptografar = ctk.CTkCheckBox(master=main_frame, text="Descriptografar", font=FONTE_PADRAO, checkbox_width=15, 
                                     checkbox_height=15, corner_radius=200, border_width=2, command=desmarcar_cript)
check_descriptografar.place(x=270,y=210)

#Botão escolher arquivo
botao_arquivo = ctk.CTkButton(master=main_frame, text="Arquivo txt", command=escolher_arquivo)
botao_arquivo.place(x=50,y=170)

#Botão iniciar que inicia a criptografia
botao_criptografar = ctk.CTkButton(master=main_frame,text="Criptografar", command=criptografar)
botao_criptografar.place(x=50,y=210)

#Botão que copia o resultado da criptografia
botao_copiar_mensagem = ctk.CTkButton(master=main_frame,text="Copiar resultado", command=copiar_Resultado, width=50)
botao_copiar_mensagem.place(x=230,y=120)

#Botão que copia a chave
botao_copiar_chave = ctk.CTkButton(master=main_frame,text="Copiar chave", command=copiar_chave, width=50)
botao_copiar_chave.place(x=345,y=120)

def main():
    janela.mainloop()