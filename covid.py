from tkinter import *
from tkinter import ttk
import requests
import json
from PIL import Image
import string
co0 = "#000000​"  # black
co1 = "#cc1d4e​"  # red
co2 = "#feffff​"  # white
co3 = "#0074eb​"  # blue
co4 = "#435e5a​"  # #435e5a​
co5 = "#59b356​"  # green
co6 = "#d9d9d9​"  # grey

janela = Tk()

janela.resizable(width=False, height=False)
janela.geometry('900x360')
janela.title('tabela covid19')
janela.configure(bg='#d9d9d9')

Pais = ["Angola", "Argentina", "Brazil", "India", "Portugal", "USA", "France", "Spain", "Global"]

reponse = requests.get("https://covid19.mathdro.id/api")
info = reponse
info = json.loads(info.text)
confirmados = info["confirmed"]["value"]
recuperado = info["recovered"]["value"]
mortos = info["deaths"]["value"]
print(confirmados, mortos, recuperado)
paises = Frame(janela, width='830', height='50', bg='#d9d9d9', relief='flat')
paises.grid(row=2, column=0, columnspan=3, sticky="N", padx=0)

label = Label(paises, text='Escolha um pais', width='13', height='2',
             relief='flat', font=("Ivy 15 bold"), anchor='center', bg='#d9d9d9',
             pady=2, padx=0)
label.grid(row=0, column=0, pady=5, padx=15, sticky='NSEW')

combo = ttk.Combobox(paises, width=15, font=("Ivy 8 bold"))
combo["value"]=(Pais)
combo.grid(row=0, column=1, padx='11', pady=15)

def primeiro_frame():
    nome_do_projeto = Frame(janela, width='830', height='50', bg='white', relief='flat')
    nome_do_projeto.grid(row=0, column=0, columnspan=3, sticky="NSEW", padx=0)
    label = Label(nome_do_projeto, text='CONVID-19', width='45', height='2', bg='white', padx='2',
                  relief='flat', anchor='center', font=("Helvetica 25 bold"),)
    label.grid(row=0, column=0, pady=2, )
    return label

################## Chamando a IPA ####################
def casos_covid():
    global label_confir
    numeros_casos = Frame(janela, width='250', height='100', bg='white', )
    numeros_casos.grid(row=1, column=0, sticky='NW', pady=3, padx=7)

    label_casos = Label(numeros_casos, text='Casos Confirmado', width='15', height='1',
                  relief='flat', font=("Courie 20 bold"), anchor='center', fg='black',bg='white',
                  pady=5, padx=0)

    label_casos.grid(row=0, column=0, pady=2, padx=3)

    label_confir = Label(numeros_casos, text=confirmados, width='12', height='1',
                  relief='flat', font=("Courie 25 bold"), anchor='center', fg='black', bg='white',
                  pady=2, padx=0)

    label_confir.grid(row=1, column=0, pady=2,)

    label_data = Label(numeros_casos, text="quarta 1 de julh de 2020", width='19', height='1',
                   relief='flat', font=("Courie 13 bold"), anchor='nw', fg='black', bg='white',
                  pady=2, padx=0)

    label_data.grid(row=2, column=0, pady=2,)
    label_text = Label(numeros_casos, text='Total de casos de covid', width='30', height='1',
                   relief='flat', font=("Courie 10 bold"), anchor='center', fg='black', bg='white',
                  pady=2, padx=0)

    label_text.grid(row=3, column=0, pady=2,)
    label_linha = Label(numeros_casos, text='', width='2', height='1',
                  relief='flat', font=("Courie 5 bold"), anchor='center', bg='blue',
                  pady=2, padx=0)

    label_linha.grid(row=4, column=0, pady=0, padx=0, sticky='NSEW')

    # return label, label_confir

def mortes_covid():
    global label_numero
    numeros_mortos = Frame(janela, width='250', height='100', bg='white', )
    numeros_mortos.grid(row=1, column=1, sticky='NW', pady=3, padx=3)

    label_mortos = Label(numeros_mortos, text='Mortes', width='15', height='1',
                  bg='white', relief='flat', font=("Courie 20 bold"), anchor='center', fg='black',
                  pady=5, padx=0)
    label_mortos.grid(row=0, column=0, pady=2, padx=7)

    label_numero = Label(numeros_mortos, text=mortos, width='12', height='1',
                  bg='white', relief='flat', font=("Courie 25 bold"), anchor='center', fg='black',
                  pady=2, padx=0)
    label_numero.grid(row=1, column=0, pady=2,)
    label_data = Label(numeros_mortos, text="quarta 1 de julh de 2020", width='20', height='1',
                  relief='flat', font=("Courie 13 bold"), anchor='center', fg='black', bg='white',
                  pady=2, padx=0)
    label_data.grid(row=2, column=0, pady=2, )
    label_text = Label(numeros_mortos, text='Total de mortes de covid', width='30', height='1',
                  relief='flat', font=("Courie 10 bold"), anchor='center', fg='black', bg='white',
                  pady=2, padx=0)
    label_text.grid(row=3, column=0, pady=2, )

    label_linha = Label(numeros_mortos, text='', width='1', height='1',
                  relief='flat', font=("Courie 5 bold"), anchor='center', bg='black',
                  pady=2, padx=0)
    label_linha.grid(row=4, column=0, pady=0, padx=0, sticky='NSEW')
    # return label,label_mortos

def recuperados_covid():
    global label_numero_recu
    recuperados = Frame(janela, width='250', height='100', bg='white', )
    recuperados.grid(row=1, column=2, sticky='NW', pady=3, padx=3)

    label_recuperados = Label(recuperados, text="recuperados", width='14', height='1',
                  bg='white', relief='flat', font=("Courie 20 bold"), anchor='center', fg='black',
                  pady=2, padx=0)
    label_recuperados.grid(row=0, column=0, pady=2, padx=7)

    label_numero_recu = Label(recuperados, text=recuperado, width='12', height='1',
                  bg='white', relief='flat', font=("Courie 25 bold"), anchor='center', fg='black',
                  pady=2, padx=0)
    label_numero_recu.grid(row=1, column=0, pady=2, )

    label_data = Label(recuperados, text="quarta 1 de julh de 2020", width='19', height='1',
                  relief='flat', font=("Courie 13 bold"), anchor='nw', fg='black', bg='white',
                  pady=2, padx=0)
    label_data.grid(row=2, column=0, pady=2, )

    label_text = Label(recuperados, text='Total de recuperados de covid', width='30', height='1',
                  relief='flat', font=("Courie 10 bold"), anchor='center', fg='black', bg='white',
                  pady=2, padx=0)
    label_text.grid(row=3, column=0, pady=2, )

    label_linha= Label(recuperados, text='', width='1', height='1',
                  relief='flat', font=("Courie 5 bold"), anchor='nw', bg='green',
                  pady=2, padx=0)
    label_linha.grid(row=4, column=0, pady=0, padx=0, sticky='NSEW')
    # return label, label_recuperados

def sla(eventObject):
    global confirmados, recuperado, data, mortos
    if combo.get() == "Global":
        reponse = requests.get("https://covid19.mathdro.id/api")
        info = reponse
        info = json.loads(info.text)
        confirmados = info['confirmed']["value"]
        recuperado = info["recovered"]["value"]
        mortos = info["deaths"]["value"]
        data = info["lastUpdate"]
        label_confir.configure(text=confirmados)
        label_numero_recu.configure(text=recuperado)
        label_numero.configure(text=mortos)
    else:
        selecionado = combo.get()
        reponse = requests.get(f"https://covid19.mathdro.id/api/countries/{selecionado}")
        info = reponse
        info = json.loads(info.text)
        confirmados = info['confirmed']["value"]
        recuperado = info["recovered"]["value"]
        mortos = info["deaths"]["value"]

        label_confir.configure(text=confirmados)
        label_numero_recu.configure(text=recuperado)
        label_numero.configure(text=mortos)
        print(selecionado,mortos, recuperado, confirmados)


combo.bind("<<ComboboxSelected>>", sla)



primeiro_frame()
casos_covid()
mortes_covid()
recuperados_covid()
janela.mainloop()
