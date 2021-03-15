from tkinter import *

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

def primeiro_frame():
    nome_do_projeto = Frame(janela, width='830', height='50', bg='white', relief='flat')
    nome_do_projeto.grid(row=0, column=0, columnspan=3, sticky="NSEW", padx=0)
    label = Label(nome_do_projeto, text='CONVID-19', width='45', height='2', bg='white', padx='3',
                  relief='flat', anchor='center', font=("Helvetica 25 bold"),)
    label.grid(row=0, column=0, pady=2)
    return label

def casos_covid():
    numeros_casos = Frame(janela, width='250', height='100', bg='white', )
    numeros_casos.grid(row=1, column=0, sticky='NW', pady=3, padx=7)

    label = Label(numeros_casos, text='Casos Confirmado', width='15', height='1',
                  relief='flat', font=("Courie 20 bold"), anchor='center', fg='black',bg='white',
                  pady=5, padx=0)
    label.grid(row=0, column=0, pady=2, padx=13)
    label = Label(numeros_casos, text='222222', width='12', height='1',
                  relief='flat', font=("Courie 25 bold"), anchor='center', fg='black', bg='white',
                  pady=2, padx=0)
    label.grid(row=1, column=0, pady=2,)
    label = Label(numeros_casos, text='data ativa 23/02/2001', width='17', height='1',
                   relief='flat', font=("Courie 17 bold"), anchor='center', fg='black',bg='white',
                  pady=2, padx=0)
    label.grid(row=2, column=0, pady=2,)
    label = Label(numeros_casos, text='Total de casos de covid', width='30', height='1',
                   relief='flat', font=("Courie 10 bold"), anchor='center', fg='black', bg='white',
                  pady=2, padx=0)
    label.grid(row=3, column=0, pady=2,)
    label = Label(numeros_casos, text='', width='2', height='1',
                  relief='flat', font=("Courie 5 bold"), anchor='center', bg='blue',
                  pady=2, padx=0)
    label.grid(row=4, column=0, pady=0, padx=0, sticky='NSEW')

    return label
def mortes_covid():
    numeros_mortos = Frame(janela, width='250', height='100', bg='white', )
    numeros_mortos.grid(row=1, column=1, sticky='NW', pady=3, padx=3)

    label = Label(numeros_mortos, text='Mortes', width='15', height='1',
                  bg='white', relief='flat', font=("Courie 20 bold"), anchor='center', fg='black',
                  pady=5, padx=0)
    label.grid(row=0, column=0, pady=2, padx=7)

    label = Label(numeros_mortos, text='555555', width='12', height='1',
                  bg='white', relief='flat', font=("Courie 25 bold"), anchor='center', fg='black',
                  pady=2, padx=0)
    label.grid(row=1, column=0, pady=2,)
    label = Label(numeros_mortos, text='data ativa 23/02/2001', width='17', height='1',
                  relief='flat', font=("Courie 17 bold"), anchor='center', fg='black', bg='white',
                  pady=2, padx=0)
    label.grid(row=2, column=0, pady=2, )
    label = Label(numeros_mortos, text='Total de casos de covid', width='30', height='1',
                  relief='flat', font=("Courie 10 bold"), anchor='center', fg='black', bg='white',
                  pady=2, padx=0)
    label.grid(row=3, column=0, pady=2, )

    label = Label(numeros_mortos, text='', width='1', height='1',
                  relief='flat', font=("Courie 5 bold"), anchor='center', bg='black',
                  pady=2, padx=0)
    label.grid(row=4, column=0, pady=0, padx=0, sticky='NSEW')
    return label

def recuperados_covid():
    recuperados = Frame(janela, width='250', height='100', bg='white', )
    recuperados.grid(row=1, column=2, sticky='NW', pady=3, padx=3)

    label = Label(recuperados, text='Casos confirmado', width='15', height='1',
                  bg='white', relief='flat', font=("Courie 20 bold"), anchor='nw', fg='black',
                  pady=2, padx=0)
    label.grid(row=0, column=0, pady=2, padx=7)

    label = Label(recuperados, text='555555', width='12', height='1',
                  bg='white', relief='flat', font=("Courie 25 bold"), anchor='nw', fg='black',
                  pady=2, padx=0)
    label.grid(row=1, column=0, pady=2, )

    label = Label(recuperados, text='data ativa 23/02/2001', width='18', height='1',
                  relief='flat', font=("Courie 17 bold"), anchor='nw', fg='black', bg='white',
                  pady=2, padx=0)
    label.grid(row=2, column=0, pady=2, )

    label = Label(recuperados, text='Total de casos de covid', width='30', height='1',
                  relief='flat', font=("Courie 10 bold"), anchor='nw', fg='black', bg='white',
                  pady=2, padx=0)
    label.grid(row=3, column=0, pady=2, )

    label = Label(recuperados, text='', width='1', height='1',
                  relief='flat', font=("Courie 5 bold"), anchor='nw', bg='green',
                  pady=2, padx=0)
    label.grid(row=4, column=0, pady=0, padx=0, sticky='NSEW')
    return label
    return label


primeiro_frame()
casos_covid()
mortes_covid()
recuperados_covid()
janela.mainloop()
