import tkinter as tk
from tkinter import scrolledtext, messagebox
import sys
import methods
import numpy as np
import matplotlib.pyplot as plt

# Cores do Tema Olive & Beige unificado
BG_APP = "#8A9A5B"       # Verde oliva
BG_TEXT = "#FDF5E6"      # Bege claro unificado para leitura e inputs
FG_TEXT = "#111111"      # Quase preto
ACCENT_BTN = "#556B2F"   # Verde oliva escuro para o botão

class RedirecionadorPrint:
    def __init__(self, widget_texto):
        self.widget_texto = widget_texto
        self.widget_texto.config(bg=BG_TEXT, fg=FG_TEXT, insertbackground=FG_TEXT)
        
        self.widget_texto.tag_configure("normal", font=("Arial", 13))
        self.widget_texto.tag_configure("bloco", font=("Arial", 13, "bold"), foreground="#2E4015", spacing1=15)
        self.widget_texto.tag_configure("erro", font=("Arial", 13, "bold"), foreground="#8B0000")
        self.widget_texto.tag_configure("sucesso", font=("Arial", 13, "bold"), foreground="#006400")
        self.widget_texto.tag_configure("funcao", font=("Arial", 13), foreground="#00008B")

    def write(self, texto):
        # 1. Respeita as quebras de linha (enter) nativas do print() do Python
        if texto == '\n' or texto.strip() == "":
            self.widget_texto.insert(tk.END, texto, "normal")
            return

        # 2. Limpa os asteriscos antes de exibir na tela
        texto_limpo = texto.replace("***", "")

        # 3. Aplica o destaque correto baseado no conteúdo da frase
        if "Consideremos" in texto_limpo or "INICIANDO" in texto_limpo:
            self.widget_texto.insert(tk.END, texto_limpo, "bloco")
        elif "|e| <=" in texto_limpo:
            self.widget_texto.insert(tk.END, texto_limpo, "erro")
        elif "Logo, x0" in texto_limpo or "Assim," in texto_limpo or "x0 pertence" in texto_limpo or "Raiz exata" in texto_limpo:
            self.widget_texto.insert(tk.END, texto_limpo, "sucesso")
        elif "f(" in texto_limpo:
            self.widget_texto.insert(tk.END, texto_limpo, "funcao")
        else:
            self.widget_texto.insert(tk.END, texto_limpo, "normal")
            
        self.widget_texto.see(tk.END)

    def flush(self):
        pass

def executar_calculo():
    try:
        funcao_str = entry_funcao.get().replace("^", "**") 
        a = float(entry_a.get())
        b = float(entry_b.get())
        erro_max = float(entry_erro.get())
        
        text_saida.delete(1.0, tk.END)
        text_saida.insert(tk.END, ">> INICIANDO CÁLCULOS...\n\n", "bloco")
        
        raiz, erro = methods.bissecao(funcao_str, [a, b], erro_max)

        x = np.linspace(a, b, 200)
        y = [methods.calcular_resultado_da_funcao(funcao_str, xi) for xi in x]

        plt.plot(x, y)
        plt.scatter([raiz], [0], label=f"|e| ≤ {erro}")

        plt.annotate(
        f"x0 ≈ {raiz:.4f}",
        (raiz, 0),
        xytext=(10, 10),
        textcoords="offset points"
        )

        plt.axhline(0)

        plt.title("Raiz aproximada encontrada")
        plt.xlabel("x")
        plt.ylabel("f(x)")

        plt.show()        
        
    except ValueError:
        messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos com números válidos para calcular.")
    except Exception as e:
        messagebox.showerror("Erro de Cálculo", f"Verifique os dados inseridos.\nDetalhe: {e}")

# ==========================================
# INTERFACE GRÁFICA (Beige & Olive Mode)
# ==========================================
janela = tk.Tk()
janela.title("Calculadora - Método da Bisseção")
janela.geometry("650x800")
janela.configure(bg=BG_APP)

tk.Label(janela, text="Trabalho de Zeros de Função", font=("Arial", 18, "bold"), bg=BG_APP, fg="#FFFFFF").pack(pady=(20, 15))

# Bloco de inputs agora usa a mesma cor bege (BG_TEXT)
frame_inputs = tk.Frame(janela, bg=BG_TEXT, padx=20, pady=20, relief="raised", bd=2)
frame_inputs.pack(fill="x", padx=25, pady=5)

estilo_label = {"font": ("Arial", 12, "bold"), "bg": BG_TEXT, "fg": "#333333"}
estilo_entry = {"font": ("Arial", 13), "bg": "#FFFFFF", "fg": "#000000", "relief": "solid", "bd": 1}

# Exemplos movidos para a esquerda, dentro do texto indicativo
tk.Label(frame_inputs, text="Função f(x) (ex: x**3 - x + 5):", **estilo_label).grid(row=0, column=0, sticky="w", pady=8)
entry_funcao = tk.Entry(frame_inputs, width=25, **estilo_entry)
entry_funcao.grid(row=0, column=1, pady=8, padx=15)

tk.Label(frame_inputs, text="Limite Inferior a (ex: -2):", **estilo_label).grid(row=1, column=0, sticky="w", pady=8)
entry_a = tk.Entry(frame_inputs, width=15, **estilo_entry)
entry_a.grid(row=1, column=1, sticky="w", pady=8, padx=15)

tk.Label(frame_inputs, text="Limite Superior b (ex: -1):", **estilo_label).grid(row=2, column=0, sticky="w", pady=8)
entry_b = tk.Entry(frame_inputs, width=15, **estilo_entry)
entry_b.grid(row=2, column=1, sticky="w", pady=8, padx=15)

tk.Label(frame_inputs, text="Erro Máximo (ex: 0.04):", **estilo_label).grid(row=3, column=0, sticky="w", pady=8)
entry_erro = tk.Entry(frame_inputs, width=15, **estilo_entry)
entry_erro.grid(row=3, column=1, sticky="w", pady=8, padx=15)

btn_calcular = tk.Button(janela, text="EXECUTAR CÁLCULO", command=executar_calculo, bg=ACCENT_BTN, fg="#FFFFFF", font=("Arial", 13, "bold"), pady=8, relief="raised", bd=3, cursor="hand2", activebackground="#6B8E23", activeforeground="#FFFFFF")
btn_calcular.pack(fill="x", padx=25, pady=20)

tk.Label(janela, text="Histórico de Iterações:", font=("Arial", 12, "bold"), bg=BG_APP, fg="#FFFFFF").pack(anchor="w", padx=25)

text_saida = scrolledtext.ScrolledText(janela, width=60, height=18, relief="sunken", bd=2, padx=15, pady=15)
text_saida.pack(fill="both", expand=True, padx=25, pady=(5, 25))

sys.stdout = RedirecionadorPrint(text_saida)

janela.mainloop()