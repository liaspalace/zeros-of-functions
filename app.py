import tkinter as tk
from tkinter import scrolledtext, messagebox
import sys
import methods

# Esta classe pega qualquer print() do methods.py e joga na tela do Tkinter
class RedirecionadorPrint:
    def __init__(self, widget_texto):
        self.widget_texto = widget_texto

    def write(self, texto):
        self.widget_texto.insert(tk.END, texto)
        self.widget_texto.see(tk.END) # Rola a tela para baixo automaticamente

    def flush(self):
        pass

def executar_calculo():
    try:
        funcao_str = entry_funcao.get().replace("^", "**") 
        a = float(entry_a.get())
        b = float(entry_b.get())
        erro_max = float(entry_erro.get())
        
        text_saida.delete(1.0, tk.END)
        text_saida.insert(tk.END, "Calculando...\n\n")
        
        # Chama a função original. Os prints vão aparecer na caixa de texto
        methods.bissecao(funcao_str, [a, b], erro_max)
        
    except Exception as e:
        messagebox.showerror("Erro de Cálculo", f"Verifique os dados inseridos.\nDetalhe: {e}")

# ==========================================
# CONSTRUÇÃO DA INTERFACE
# ==========================================
janela = tk.Tk()
janela.title("Calculadora - Método da Bisseção")
janela.geometry("550x650")
janela.configure(padx=20, pady=20)

tk.Label(janela, text="Trabalho de Zeros de Função", font=("Arial", 14, "bold")).pack(pady=(0, 15))

frame_inputs = tk.Frame(janela)
frame_inputs.pack(fill="x")

tk.Label(frame_inputs, text="Função f(x) (ex: x**3 - x + 5 ou x^3 - x + 5):").grid(row=0, column=0, sticky="w", pady=5)
entry_funcao = tk.Entry(frame_inputs, width=40)
entry_funcao.insert(0, "x**3 - x + 5")
entry_funcao.grid(row=0, column=1, pady=5, padx=5)

tk.Label(frame_inputs, text="Limite Inferior (a):").grid(row=1, column=0, sticky="w", pady=5)
entry_a = tk.Entry(frame_inputs, width=15)
entry_a.insert(0, "-2")
entry_a.grid(row=1, column=1, sticky="w", pady=5, padx=5)

tk.Label(frame_inputs, text="Limite Superior (b):").grid(row=2, column=0, sticky="w", pady=5)
entry_b = tk.Entry(frame_inputs, width=15)
entry_b.insert(0, "-1")
entry_b.grid(row=2, column=1, sticky="w", pady=5, padx=5)

tk.Label(frame_inputs, text="Erro Máximo:").grid(row=3, column=0, sticky="w", pady=5)
entry_erro = tk.Entry(frame_inputs, width=15)
entry_erro.insert(0, "0.04")
entry_erro.grid(row=3, column=1, sticky="w", pady=5, padx=5)

btn_calcular = tk.Button(janela, text="Calcular Raiz", command=executar_calculo, bg="#28a745", fg="white", font=("Arial", 11, "bold"), pady=5)
btn_calcular.pack(fill="x", pady=20)

tk.Label(janela, text="Passo a passo:").pack(anchor="w")
text_saida = scrolledtext.ScrolledText(janela, width=60, height=18, font=("Consolas", 10))
text_saida.pack(fill="both", expand=True)

# Ativa o redirecionamento dos prints para a caixa de texto
sys.stdout = RedirecionadorPrint(text_saida)

janela.mainloop()