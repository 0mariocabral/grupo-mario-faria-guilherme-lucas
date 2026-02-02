
import tkinter as tk
from tkinter import messagebox
def exibir_mensagem():
    nome = entry_nome.get()
    if nome.strip() == "":
        messagebox.showwarning("Aviso", "Por favor, digite seu nome.")
    else:
        messagebox.showinfo(
            "Mensagem",
            f"Olá, {nome}! Seja bem-vinda(o)!"
        )
janela = tk.Tk()
janela.title("Boas-vindas")
janela.geometry("600x300")
janela.configure(bg="black")
label_nome = tk.Label(
    janela,
    text="Digite seu nome:",
    font=("Arial", 36),
    fg="red",
    bg="black"
)
label_nome.grid(row=0, column=0, padx=20, pady=20)
entry_nome = tk.Entry(
    janela,
    font=("Arial", 36),
    fg="black"
)
entry_nome.grid(row=0, column=1, padx=20, pady=20)
botao = tk.Button(
    janela,
    text="Exibir mensagem",
    font=("Arial", 30),
    fg="red",
    bg="black",
    command=exibir_mensagem
)
botao.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
janela.mainloop()