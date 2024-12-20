import tkinter as tk
import math

tela = tk.Tk() #criação da tela
tela.title("Calculadora") #Título da tela
tela.geometry("400x400") #tamanho da tela

#Exibir números
campo_numeros = tk.Entry(tela, font= ("verdanda",20), justify="right")
campo_numeros.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def adicionar_numero(numero):
    campo_numeros.insert(tk.END,numero)

def limpar():
    campo_numeros.delete(0,tk.END) #limpar tela

def apagar_um():                        #apagar apenas um caractere
    texto_atual = campo_numeros.get()
    campo_numeros.delete(0,tk.END)
    campo_numeros.insert(0,texto_atual[:-1])

#fazer calculos
def calcular():
    try:
        resultado = eval(campo_numeros.get()) #calcula as operações
        campo_numeros.delete (0,tk.END)   #limpa tela
        campo_numeros.insert(tk.END, str(resultado)) #resultado das operações
    except:
        campo_numeros.delete(0, tk.END)
        campo_numeros.insert(tk.END, "ERRO")  # mensagem quando operação estiver errada

#calcular raiz quadrada
def raiz_quadrada():
    try:
        numero = float(campo_numeros.get())
        resultado = math.sqrt(numero)
        campo_numeros.delete(0,tk.END)
        campo_numeros.insert(tk.END, str(resultado))
    except:
        campo_numeros.delete(0, tk.END)
        campo_numeros.insert(tk.END, "Erro")

#calcula potência
def potencia():
        campo_numeros.insert(tk.END,"**")

def porcentagem():
    try:
        numero = float(campo_numeros.get())
        resultado = numero/100
        campo_numeros.delete(0,tk.END,)
        campo_numeros.insert(tk.END,str(resultado))
    except:
        campo_numeros.delete(0, tk.END, )
        campo_numeros.insert(tk.END, "ERRO")


botoes = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2),
                ("0", 5, 1),
]

for texto, linha, coluna in botoes:
    tk.Button(tela, text=texto, font=("verdanda",18), command=lambda t=texto: adicionar_numero(t)).grid(row=linha, column=coluna, padx=5, pady=5)

#botões das operações

opereaçoes = [
    ("⌫",1,0),("%",1,1), ("√",1,2),("^",1,3), ("*",2,3), ("/",3,3), ("+",4,3), ("-",5,3),("C",5,0),("=",5,2)
]

for texto, linha, coluna in opereaçoes:
    if texto == "=":
        tk.Button(tela, text=texto, font=("verdana", 18), command=calcular).grid(row=linha, column=coluna, padx=5,pady=5)
    elif texto == "C":
        tk.Button(tela, text=texto, font=("verdana", 18), command=limpar).grid(row=linha, column=coluna, padx=5, pady=5)
    elif texto == "⌫":
        tk.Button(tela, text=texto, font=("verdana", 18), command=apagar_um).grid(row=linha, column=coluna, padx=5, pady=5)
    elif texto == "√":
        tk.Button(tela, text=texto, font=("verdana", 18), command=raiz_quadrada).grid(row=linha, column=coluna, padx=5, pady=5)
    elif texto == "^":
        tk.Button(tela, text=texto, font=("verdana", 18), command=potencia).grid(row=linha, column=coluna, padx=5, pady=5)
    elif texto == "%":
        tk.Button(tela, text=texto, font=("verdana", 18), command=porcentagem).grid(row=linha, column=coluna, padx=5, pady=5)
    else:
        tk.Button(tela, text=texto, font=("verdana", 18), command=lambda t=texto: adicionar_numero(t)).grid(row=linha, column=coluna, padx=5, pady=5)

tela.mainloop() #monstrar janela