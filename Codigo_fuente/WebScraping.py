from bs4 import BeautifulSoup
from urllib.request import urlopen
import tkinter as tk
from  tkinter import ttk

def ventana(lista):
    """
        Crea la interfaz grafica junto con varios widgets
        :param class dict lista: un dictionario con los nombres de las paginas y su respectivas url.
        """
    lista_direcciones = [x for x in lista]
    print(lista_direcciones)
    ventana= tk.Tk()
    print(type(ventana))
    ventana.title("WebScrapping")
    ventana.geometry('600x400')
    etiqueta= tk.Label(ventana, text="Escoja el producto de interes : ", font=('Adobe Fan Heiti Std B',13))
    etiqueta.place(x= 30, y=30)
    productos= ttk.Combobox()
    productos = ttk.Combobox(ventana)
    productos['values'] = lista_direcciones
    productos.current()
    productos.place(x=280, y=30)
    boton= tk.Button(ventana, text="Buscar", command= lambda:imprimir_datos(lista[productos.get()], ventana),
                    font=('Adobe Fan Heiti Std B',9), bg="purple",
                    fg="white")
    boton.place(x= 430, y=28)
    ventana.mainloop()
def tabla(diccionario, ventana):
    """Crea un tabla con el widget treeview de tkinter en donde se colocaran los datos extraidos de la web
       :param class dict diccionario:  un diccionario con los nombres de las paginas y su respectivas url
       :param class tkinter.Tk ventana: es la ventana donde se colocaran los datos
        """
    tree = ttk.Treeview(ventana, columns=('Nombre', 'Precio'))

    tree.heading('#0', text='#')
    tree.heading('#1', text='|  Producto  |')
    tree.heading('#2', text='|   Precio  |')

    tree.column('#0', width= 50, stretch=tk.YES)
    tree.column('#1', width= 280,  stretch=tk.YES)
    tree.column('#2',  width= 110, stretch=tk.YES)

    tree.place(x=90, y=100)
    cont=1
    for producto in diccionario:
        tree.insert('', 'end', text=f"{cont}",
                    values=(producto, diccionario[producto]))
        cont+=1
def imprimir_datos(url, ventana):
    """
    busca los datos en la web de la opcion que el usuario haya escogido

    :param class str url: es la url de donde se sacaran los datos
    :param class tkinter.Tk ventana: es la ventana donde se colocaran los datos
    :return: None
    """
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    texto = soup.get_text()
    lineas = [linea for linea in texto.split('\n') if linea != '']
    precios={}
    for x in range(len(lineas)):
        if lineas[ x]=="0" and lineas[x+1]=="0":
            precios[lineas[x+2]]=lineas[x+5]
            continue
        if "%" in lineas[x] and "$" in lineas[x+1]:
            precios[lineas[x+2]]=lineas[x+6]
    tabla(precios, ventana)
    print(len(precios))
def direcciones():
    """
    Provee toda la información de las urls para que se pueda hacer el raspado web

    """
    todos={'Endulzantes':"https://www.tiendasmetro.co/supermercado/despensa/azucar-endulzantes-y-panelas/500?PS=18",
    'Avenas':"https://www.tiendasmetro.co/supermercado/despensa/avenas/500?PS=18",
    'Harinas':"https://www.tiendasmetro.co/supermercado/despensa/harinas/500?PS=18",
    'Chocolates y cafés':"https://www.tiendasmetro.co/supermercado/despensa/chocolate-y-cafe/500?PS=44",
    'Cereales':"https://www.tiendasmetro.co/supermercado/despensa/cereales-y-granolas/500?PS=18",
    'Pastas':"https://www.tiendasmetro.co/supermercado/despensa/pastas/500?PS=44",
    'Arroz y granos':"https://www.tiendasmetro.co/supermercado/despensa/arroz-y-granos/500?PS=44"}

    ventana(todos)

def main():
    """
    Inicia el programa
        """
    direcciones()

main()