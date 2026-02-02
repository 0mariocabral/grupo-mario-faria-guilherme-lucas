import tkinter as tk #importa biblioteca tkinter para graficos
from tkinter import messagebox #importar modulo do tkinter para caixas de dialogo

def exibir_mensagem(): #funcao que pega o texto digitado no Entry chamado entrada_nome
    nome = entrada_nome.get()
    if nome.strip() != "": #garante que o usuario nao digitou so espacos
        messagebox.showinfo("Mensagem", f"Olá, {nome}! Seja bem-vinda(o)!") #se tiver nome mostra uma janela de informacao com a saudacao
    else:
        messagebox.showwarning("Atenção", "Por favor, digite seu nome.") #se estiver vazio mostra um aviso pedindo o nome

# iniciar
app = tk.Tk()

# titulo
app.title("Janela que pede nome e mostra mensagem")

#digite seu nome
label_nome = tk.Label(app, text="Digite seu nome:")
label_nome.grid(row=0, column=0, padx=10, pady=10)

# entrada de texto
entrada_nome = tk.Entry(app)
entrada_nome.grid(row=0, column=1, padx=10, pady=10)

# botao para exibir a mensagem
botao = tk.Button(app, text="Exibir mensagem", command=exibir_mensagem)
botao.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# tamanho da janela
app.geometry("800x600")

#cor de fundo em hexadecimal
app.config(bg="#FF0000")

# loop repete a tela varias vezes
app.mainloop()