# projeto tkinter 

import tkinter as tk

def exibir_mensagem():
    nome = entrada.get()
    rotulo_mensagem.config(text=f"Olá, {nome}! Seja bem-vinda(o)!")
janela = tk.Tk()
janela.title("Boas-vindas")
rotulo = tk.Label(janela, text="Digite seu nome:")
rotulo.grid(row=0, column=0, padx=10, pady=10)
entrada = tk.Entry(janela)
entrada.grid(row=0, column=1, padx=10, pady=10)
botao = tk.Button(janela, text="Exibir mensagem", command=exibir_mensagem)
botao.grid(row=1, column=0, columnspan=2, pady=10)
rotulo_mensagem = tk.Label(janela, text="")
rotulo_mensagem.grid(row=2, column=0, columnspan=2, pady=10)
janela.mainloop()
 