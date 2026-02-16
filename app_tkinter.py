import tkinter as tk


def exibir_mensagem() -> None:
    nome = entrada_nome.get().strip()
    if not nome:
        resultado.config(text="Digite seu nome para continuar.")
        return
    resultado.config(text=f"Olá, {nome}! Teste realizado com sucesso ✅")


janela = tk.Tk()
janela.title("App de Teste")
janela.geometry("320x180")
janela.resizable(False, False)

rotulo = tk.Label(janela, text="Digite seu nome:", font=("Arial", 12))
rotulo.pack(pady=(20, 8))

entrada_nome = tk.Entry(janela, width=28)
entrada_nome.pack()

botao = tk.Button(janela, text="Testar", command=exibir_mensagem)
botao.pack(pady=12)

resultado = tk.Label(janela, text="", font=("Arial", 10))
resultado.pack()

janela.mainloop()