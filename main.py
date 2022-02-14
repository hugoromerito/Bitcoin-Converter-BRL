from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# -------------------- BIBLIOTECA DE SOLICITAÇÃO AO API --------------------
import requests
import json


""" ------------------------ SEJA BEM-VINDO E FIQUE A VONTADE --------------------------
---------------- ME CHAMO HUGO E TENHO OUTROS PROJETOS COMO ESSE NO MEU ----------------
-------------- PORTFÓLIO ONLINE NO GITHUB: https://github.com/hugoromerito ------------- """









# ------------- PALETA DE CORES ------------
color1 = "#6f9fbd"  # azul claro
color2 = "#000000"  # Preta
color3 = "#feffff"  # branca

bground = "#F5CE85"  # background laranja
bground2 = "#6e6e6e" # background cinza

# ------------- CRIA JANELA -------------
janela = Tk()
janela.title('')
janela.geometry('470x500')
janela.configure(bg=bground)

# ------------- DIVIDINDO A JANELA EM DOIS ---------------
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_cima = Frame(janela, width=520, height=100, bg=bground2, pady=0, padx=0, relief='flat')
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=520, height=450, bg=bground, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=2, column=0, sticky=NW)


# ------------- COLETA DE DADOS DO API HOSPEDADO -------------

def info():
    api_link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,BRL,THB,PAB,ETB,BOB,MXN,AOA'

    # ------------- HTTP requests -------------
    response = requests.get(api_link)

    # ------------- CONVERTE OS DADOS EM DICIONARIO -------------
    dados = response.json()

    # ------------- VALOR EM REAL BRL -------------
    valor_reais = float(dados['BRL'])
    valor_formatado_reais = "R$ {:,.3f}".format(valor_reais)
    l_p_reais['text'] = valor_formatado_reais

    # ------------- VALOR EM DOLAR AMERICANO -------------
    valor_usd = float(dados['USD'])
    valor_formatado_usd = "{:,.3f}".format(valor_usd)
    l_p_usd['text'] = 'USD : $ ' + valor_formatado_usd


    # ------------- VALOR EM EURO -------------
    valor_euro = float(dados['EUR'])
    valor_formatado_euro = "{:,.3f}".format(valor_euro)
    l_p_euro['text'] = 'EURO : € ' + valor_formatado_euro

    # ------------- VALOR EM KWANZA AOA -------------
    valor_kz = float(dados['AOA'])
    valor_formatado_kz = "{:,.3f}".format(valor_kz)
    l_p_kz['text'] = 'AOA : Kz ' + valor_formatado_kz

    #------------- VALOR EM BAHT TAILANDÊS -------------
    valor_thb = float(dados['THB'])
    valor_formatado_thb = "{:,.3f}".format(valor_thb)
    l_p_thb['text'] = 'THB : ฿ ' + valor_formatado_thb

    # ------------- VALOR EM BALBOA PANAMENHO -------------
    valor_pab = float(dados['PAB'])
    valor_formatado_pab = "{:,.3f}".format(valor_pab)
    l_p_pab['text'] = 'PAB : B/. ' + valor_formatado_pab

    # ------------- VALOR EM BIRR ETÍOPE -------------
    valor_etb = float(dados['ETB'])
    valor_formatado_etb = "{:,.3f}".format(valor_etb)
    l_p_etb['text'] = 'ETB : ብር ' + valor_formatado_etb

    # ------------- VALOR BOLIVIANO DA BOLÍVIA -------------
    valor_bob = float(dados['BOB'])
    valor_formatado_bob = "{:,.3f}".format(valor_bob)
    l_p_bob['text'] = 'BOB : Bs ' + valor_formatado_bob

    # ------------- VALOR PESO MEXICANO -------------
    valor_mxn = float(dados['MXN'])
    valor_formatado_mxn = "{:,.3f}".format(valor_mxn)
    l_p_mxn['text'] = 'MXN : $ ' + valor_formatado_mxn

    frame_baixo.after(1000, info)


# ------------- CONFIGURANDO SEÇÃO DE CIMA -------------
imagem = Image.open('img/logo-bit.png')
imagem = imagem.resize((60, 60), Image.ANTIALIAS)
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_cima, image=imagem, compound=LEFT, bg=bground2, relief=FLAT)
l_icon.place(x=20, y=16)

l_nome = Label(frame_cima, text='Bitcoin Converter', bg=bground2, fg=color3, relief=FLAT, anchor='center', font=('Ivy 20 bold'))
l_nome.place(x=90, y=30)

# ------------- CONFIGURANDO SEÇÃO DE BAIXO -------------
imagem2 = Image.open('img/student.png')
imagem2 = imagem2.resize((30, 30), Image.ANTIALIAS)
imagem2 = ImageTk.PhotoImage(imagem2)

l_icon = Label(frame_baixo, image=imagem2, compound=LEFT, bg=bground, relief=FLAT)
l_icon.place(x=140, y=380)

l_nome = Label(frame_baixo, text='Hugo Romerito', bg=bground, fg=color2, relief=FLAT, anchor='center', font=('Ivy 15'))
l_nome.place(x=180, y=383)

#------------- CONFIGURAÇÃO VISUAL DA SAIDA DOS RESULTADOS CONVERTIDOS -------------
l_p_reais = Label(frame_baixo, text='', bg=bground, fg=color2, relief=FLAT, anchor='center', font=('Arial 20'))
l_p_reais.place(x=140, y=30)

l_p_usd = Label(frame_baixo, text='', bg=bground, fg=color2, relief=FLAT, anchor='center', font=('Ivy 12'))
l_p_usd.place(x=150, y=95)

l_p_euro = Label(frame_baixo, text='', bg=bground, fg=color2, relief=FLAT, anchor='center', font=('Ivy 12'))
l_p_euro.place(x=150, y=125)

l_p_kz = Label(frame_baixo, text='', bg=bground, fg=color2, relief=FLAT, anchor='center', font=('Ivy 12'))
l_p_kz.place(x=150, y=155)

l_p_thb = Label(frame_baixo, text='', bg=bground, fg=color2, relief=FLAT, anchor='center', font=('Ivy 12'))
l_p_thb.place(x=150, y=185)

l_p_pab = Label(frame_baixo, text='', bg=bground, fg=color2, relief=FLAT, anchor='center', font=('Ivy 12'))
l_p_pab.place(x=150, y=215)

l_p_etb = Label(frame_baixo, text='', bg=bground, fg=color2, relief=FLAT, anchor='center', font=('Ivy 12'))
l_p_etb.place(x=150, y=245)

l_p_bob = Label(frame_baixo, text='', bg=bground, fg=color2, relief=FLAT, anchor='center', font=('Ivy 12'))
l_p_bob.place(x=150, y=275)

l_p_mxn = Label(frame_baixo, text='', bg=bground, fg=color2, relief=FLAT, anchor='center', font=('Ivy 12'))
l_p_mxn.place(x=150, y=305)

info()

janela.mainloop()
