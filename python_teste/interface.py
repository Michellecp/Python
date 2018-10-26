from tkinter import *
import random
import time
import datetime

root = Tk()
root.geometry('1350x750+0+0')
root.title('SISTEMA DE VENDAS')
root.configure(background= 'gray')

# ===============Declarando variaveis===============
C1=StringVar()
C2=StringVar()
C3=StringVar()
C4=StringVar()
C5=StringVar()
C6=StringVar()
C7=StringVar()
C8=StringVar()
C9=StringVar()

B1=StringVar()
B2=StringVar()
B3=StringVar()
B4=StringVar()
B5=StringVar()
B6=StringVar()
B7=StringVar()
B8=StringVar()
B9=StringVar()

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()

C1.set('0')
C2.set('0')
C3.set('0')
C4.set('0')
C5.set('0')
C6.set('0')
C7.set('0')
C8.set('0')
C9.set('0')

B1.set('0')
B2.set('0')
B3.set('0')
B4.set('0')
B5.set('0')
B6.set('0')
B7.set('0')
B8.set('0')
B9.set('0')

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
var13.set("0")
var14.set("0")
var15.set("0")
var16.set("0")
var17.set("0")
var18.set("0")

#VARIAVEIS DO RODAPÉ
dataordem= StringVar()
Recibo = StringVar()
Impostos = StringVar()
Subtotal = StringVar()
Total = StringVar()
TotalBolo = StringVar()
TotalBebidas = StringVar()
taxaservicos = StringVar()

#Criando os metodo dos botões
#Criando código do Botão sair

def iExit():
    root.destroy()
    return
#Criando código do Botão Limpar

def Limpar():
    dataordem.set('')
    txtrecibo.delete('1.0',END)
    Impostos.set('')
    Subtotal.set('')
    Total.set('')
    TotalBolo.set('')
    TotalBebidas.set('')
    taxaservicos.set('')

    C1.set('0')
    C2.set('0')
    C3.set('0')
    C4.set('0')
    C5.set('0')
    C6.set('0')
    C7.set('0')
    C8.set('0')
    C9.set('0')

    B1.set('0')
    B2.set('0')
    B3.set('0')
    B4.set('0')
    B5.set('0')
    B6.set('0')
    B7.set('0')
    B8.set('0')
    B9.set('0')

    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")
    var17.set("0")
    var18.set("0")

    txtLatte.configure(state=DISABLED)
    txtLatte_Gelado.configure(state=DISABLED)
    txtEspresso.configure(state=DISABLED)
    txtIced_Latte.configure(state=DISABLED)
    txtCafe_Cortado.configure(state=DISABLED)
    txtCafe_Leite.configure(state=DISABLED)
    txtCafe_Preto.configure(state=DISABLED)
    txtCafe_creme.configure(state=DISABLED)
    txtCapuccino.configure(state=DISABLED)
    txtBolo_Cafe.configure(state=DISABLED)
    txtBolo_Cenoura.configure(state=DISABLED)
    txtBolo_Milho.configure(state=DISABLED)
    txtBolo_Banana.configure(state=DISABLED)
    txtBolo_Morango.configure(state=DISABLED)
    txtBolo_Limao.configure(state=DISABLED)
    txtTorta_Limao.configure(state=DISABLED)
    txtBolo_Chocolate.configure(state=DISABLED)
    txtTorta.configure(state=DISABLED)

Impostos = StringVar()
Subtotal.set('')
Total.set('')
TotalBolo.set('')
TotalBebidas.set('')

#Criando o Botão Recibo
def custoItem():

    Item1=float(C1.get())
    Item2=float(C2.get())
    Item3=float(C3.get())
    Item4=float(C4.get())
    Item5=float(C5.get())
    Item6=float(C6.get())
    Item7=float(C7.get())
    Item8=float(C8.get())

    Item9  = float(B1.get())
    Item10 = float(B2.get())
    Item11 = float(B3.get())
    Item12 = float(B4.get())
    Item13 = float(B5.get())
    Item14 = float(B6.get())
    Item15 = float(B7.get())
    Item16 = float(B8.get())

    PrecoComida = (Item1 * 1.20)+(Item2 * 1.99)+(Item3 * 2.05)+(Item4 * 2.10)+(Item5 * 1.99)+(Item6 * 2.99)+\
                  (Item7 * 1.99)+(Item8 * 1.99)
    PrecoBebida = (Item9 * 1.20) + (Item10 * 1.99) + (Item11 * 2.05) + (Item12 * 2.10) + (Item13 * 1.99) + (Item14 * 2.99) + \
                  (Item15 * 1.99) + (Item16 * 1.99)

    ComidaPreco='$',str('%.2f'%(PrecoComida))
    Bebidapreco='$', str('%.2f'%(PrecoBebida))
    TotalBolo.set(ComidaPreco)
    TotalBebidas.set(Bebidapreco)
    SC='$', str('%.2f'%(0.10))
    taxaservicos.set(SC)

    SubtotalItens='$', str('%.2f'%(PrecoBebida+PrecoComida+0.10))
    Subtotal.set(SubtotalItens)

    Taxa='$',str('%.2f'%((PrecoComida+PrecoBebida+0.10)*0.15))
    Impostos.set(Taxa)

    Tt =((PrecoBebida+PrecoComida+0.10)*0.15)
    TC='$', str('%.2f'%(PrecoComida+PrecoBebida+1.60+Tt))
    Total.set(TC)


#criando os metodos para os Checkbox
def chkLatte():
    if(var1.get() == 1):
        txtLatte.configure(state=NORMAL)
        C1.set('')
    elif(var1.get() == 0):
        txtLatte.configure(state=DISABLED)
        C1.set('0')

def chkLatte_Gelado():
    if(var2.get() == 1):
        txtLatte_Gelado.configure(state=NORMAL)
        C2.set('')
    elif(var2.get() == 0):
        txtLatte_Gelado.configure(state=DISABLED)
        C2.set('0')

def chkEspresso():
    if(var3.get() == 1):
        txtEspresso.configure(state=NORMAL)
        C3.set('')
    elif(var3.get() == 0):
        txtEspresso.configure(state=DISABLED)
        C3.set('0')

def chkIced_Latte():
    if(var4.get() == 1):
        txtIced_Latte.configure(state=NORMAL)
        C4.set('')
    elif(var4.get() == 0):
        txtIced_Latte.configure(state=DISABLED)
        C4.set('0')

def chkCafe_Cortado():
    if(var5.get() == 1):
        txtCafe_Cortado.configure(state=NORMAL)
        C5.set('')
    elif(var5.get() == 0):
        txtCafe_Cortado.configure(state=DISABLED)
        C5.set('0')

def chkCafe_Leite():
    if(var6.get() == 1):
        txtCafe_Leite.configure(state=NORMAL)
        C6.set('')
    elif(var6.get() == 0):
        txtCafe_Leite.configure(state=DISABLED)
        C6.set('0')

def chkCafe_Preto():
    if(var7.get() == 1):
        txtCafe_Preto.configure(state=NORMAL)
        C7.set('')
    elif(var7.get() == 0):
        txtCafe_Preto.configure(state=DISABLED)
        C6.set('0')

def chkCafe_Creme():
    if(var8.get() == 1):
        txtCafe_creme.configure(state=NORMAL)
        C8.set('')
    elif(var8.get() == 0):
        txtCafe_creme.configure(state=DISABLED)
        C8.set('0')

def chkCapucciono():
    if(var9.get() == 1):
        txtCapuccino.configure(state=NORMAL)
        C9.set('')
    elif(var9.get() == 0):
        txtCapuccino.configure(state=DISABLED)
        C9.set('0')

def chkBolo_Cafe():
    if(var10.get() == 1):
        txtBolo_Cafe.configure(state=NORMAL)
        B1.set('')
    elif(var10.get() == 0):
        txtBolo_Cafe.configure(state=DISABLED)
        B1.set('0')

def chkBolo_cenoura():
    if(var11.get() == 1):
        txtBolo_Cenoura.configure(state=NORMAL)
        B2.set('')
    elif(var11.get() == 0):
        txtBolo_Cenoura.configure(state=DISABLED)
        B2.set('0')

def chkBolo_milho():
    if(var12.get() == 1):
        txtBolo_Milho.configure(state=NORMAL)
        B3.set('')
    elif(var12.get() == 0):
        txtBolo_Milho.configure(state=DISABLED)
        B3.set('0')

def chkBolo_banana():
    if(var13.get() == 1):
        txtBolo_Banana.configure(state=NORMAL)
        B4.set('')
    elif(var13.get() == 0):
        txtBolo_Banana.configure(state=DISABLED)
        B4.set('0')

def chkBolo_morango():
    if(var14.get() == 1):
        txtBolo_Morango.configure(state=NORMAL)
        B5.set('')
    elif(var14.get() == 0):
        txtBolo_Morango.configure(state=DISABLED)
        B5.set('0')

def chkBolo_limao():
    if(var15.get() == 1):
        txtBolo_Limao.configure(state=NORMAL)
        B6.set('')
    elif(var15.get() == 0):
        txtBolo_Limao.configure(state=DISABLED)
        B6.set('0')

def chkTorta_limao():
    if(var16.get() == 1):
        txtTorta_Limao.configure(state=NORMAL)
        B7.set('')
    elif(var16.get() == 0):
        txtTorta_Limao.configure(state=DISABLED)
        B7.set('0')

def chkBolo_chocolate():
    if(var17.get() == 1):
        txtBolo_Chocolate.configure(state=NORMAL)
        B8.set('')
    elif(var17.get() == 0):
        txtBolo_Chocolate.configure(state=DISABLED)
        B8.set('0')

def chkTorta():
    if(var18.get() == 1):
        txtTorta.configure(state=NORMAL)
        B9.set('')
    elif(var18.get() == 0):
        txtTorta.configure(state=DISABLED)
        B9.set('0')

# ===============Frames do Primarios===============
Tops = Frame(root, width=1350, height=100,bd=9,relief='raise')
Tops.pack(side=TOP)

framef1 = Frame(root,width=900,height=650, bd=8, relief='raise')
framef1.pack(side=LEFT)

framef2 = Frame(root,width=440,height=250, bg='black',bd=8,relief='raise')
framef2.pack(side=RIGHT)

#============Frames da Secundarios===============
frameft2 = Frame(framef2, width=440, height=450, bd=2, relief='raise')
frameft2.pack(side=TOP)

framefb2 = Frame(framef2,width=440,height=250, bd=2,relief='raise')
framefb2.pack(side=BOTTOM)

framef1a = Frame(framef1,width=900,height=300, bd=2,relief='raise')
framef1a.pack(side=TOP)

framef2a = Frame(framef1,width=900,height=320, bd=2,relief='raise')
framef2a.pack(side=BOTTOM)

framef1aa = Frame(framef1a,width=450,height=300, bd=2,relief='raise')
framef1aa.pack(side=LEFT)

framef1ab = Frame(framef1a,width=450,height=330, bd=2,relief='raise')
framef1ab.pack(side=RIGHT)

# ===============Criando Frames do Rodapé===============

framef2aa = Frame(framef2a,width=450,height=800, bd=2,relief='raise')
framef2aa.pack(side=LEFT)

framef2ab = Frame(framef2a,width=450,height=800, bd=2,relief='raise')
framef2ab.pack(side=RIGHT)

frameRODAPE = Frame(framef2a,width=211,height=190, bd=0,relief='raise')
frameRODAPE.pack(side=BOTTOM)

# ===============Trocando a cor do Frame da Esquerda===============

framef1.configure(background= 'gray')

# ===============incluindo Label do Cabeçalho com titulo===============

lblInfo=Label(Tops, font=('arial',50,'bold'),text='SISTEMA DE CAFETERIA', bd=8, width=32)
lblInfo.grid(row=0, column=0)

#CRIANDO OS RADIOS BUTTON PARA O CAFE
Latte= Checkbutton(framef1aa,text='Latte \t', variable=var1, onvalue=1, offvalue=0,width=13,
                   font=('arial', 18,'bold'), command=chkLatte).grid(row=0, sticky=W)
Latte_Gelado= Checkbutton(framef1aa,text='Latte_Gelado \t', variable=var2, onvalue=1, offvalue=0,width=20,
                   font=('arial', 18,'bold'), command=chkLatte_Gelado).grid(row=1, sticky=W)
Espresso= Checkbutton(framef1aa,text='Espresso \t', variable=var3, onvalue=1, offvalue=0,width=20,
                   font=('arial', 18,'bold'), command=chkEspresso).grid(row=2, sticky=W)
Iced_Latte= Checkbutton(framef1aa,text='Iced_Latte \t', variable=var4, onvalue=1, offvalue=0,width=20,
                   font=('arial', 18,'bold'), command=chkIced_Latte).grid(row=3, sticky=W)
Cafe_Cortado= Checkbutton(framef1aa,text='Cafe_Cortado \t', variable=var5, onvalue=1, offvalue=0,width=20,
                   font=('arial', 18,'bold'),command=chkCafe_Cortado).grid(row=4, sticky=W)
Cafe_Leite= Checkbutton(framef1aa,text='Café_Leite \t', variable=var6, onvalue=1, offvalue=0,width=20,
                   font=('arial', 18,'bold'),command=chkCafe_Leite).grid(row=5, sticky=W)
Cafe_Preto= Checkbutton(framef1aa,text='Cafe_Preto \t', variable=var7, onvalue=1, offvalue=0,width=20,
                   font=('arial', 18,'bold'),command=chkCafe_Preto).grid(row=6, sticky=W)
Cafe_creme= Checkbutton(framef1aa,text='Cafe_creme \t', variable=var8, onvalue=1, offvalue=0,width=20,
                   font=('arial', 18,'bold'),command=chkCafe_Creme).grid(row=7, sticky=W)
Capucciono= Checkbutton(framef1aa,text='Capucciono \t', variable=var9, onvalue=1, offvalue=0,width=20,
                   font=('arial', 18,'bold'),command=chkCapucciono).grid(row=8, sticky=W)

#CRIANDO OS RADIOS BUTTON PARA OS BOLOS
Bolo_Cafe= Checkbutton(framef1ab,text='Bolo_Cafe \t', variable=var10, onvalue=1, offvalue=0,width=20,
                   font=('arial', 18,'bold'), command=chkBolo_Cafe).grid(row=0, sticky=W)
Bolo_Cenoura= Checkbutton(framef1ab,text='Bolo_Cenoura \t', variable=var11, onvalue=1, offvalue=0, width=20,
                   font=('arial', 18,'bold'), command=chkBolo_cenoura).grid(row=1, sticky=W)
Bolo_Milho= Checkbutton(framef1ab,text='Bolo_Milho \t', variable=var12, onvalue=1, offvalue=0,width=20,
                   font=('arial', 18,'bold'), command=chkBolo_milho).grid(row=2, sticky=W)
Bolo_Banana= Checkbutton(framef1ab,text='Bolo_Banana \t', variable=var13, onvalue=1, offvalue=0,width=20,
                   font=('arial', 18,'bold'),command=chkBolo_banana).grid(row=3, sticky=W)
Bolo_Morango= Checkbutton(framef1ab,text='Bolo_Morango \t', variable=var14, onvalue=1, offvalue=0,width=20,
                   font=('arial', 18,'bold'), command=chkBolo_morango).grid(row=4, sticky=W)
Bolo_Limao= Checkbutton(framef1ab,text='Bolo_Limao \t', variable=var15, onvalue=1, offvalue=0,width=20,
                   font=('arial', 18,'bold'),command=chkBolo_limao).grid(row=5, sticky=W)
Torta_Limao= Checkbutton(framef1ab,text='Torta_Limao \t', variable=var16, onvalue=1, offvalue=0,width=20,
                   font=('arial', 18,'bold'), command=chkTorta_limao).grid(row=6, sticky=W)
Bolo_Chocolate= Checkbutton(framef1ab,text='Bolo_Chocolate \t', variable=var17, onvalue=1, offvalue=0,width=20,
                   font=('arial', 18,'bold'), command=chkBolo_chocolate).grid(row=7, sticky=W)
Torta= Checkbutton(framef1ab,text='Torta \t', variable=var18, onvalue=1, offvalue=0,width=13,
                   font=('arial', 18,'bold'), command=chkTorta).grid(row=8, sticky=W)

#Criando os campos de texto da Bebida

txtLatte = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,width=8,justify='left',textvariable=C1,state=DISABLED)
txtLatte.grid(row=0, column=1)

txtLatte_Gelado = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,width=8,justify='left', textvariable=C2,state=DISABLED)
txtLatte_Gelado.grid(row=1, column=1)

txtEspresso = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,width=8,justify='left',textvariable=C3,state=DISABLED)
txtEspresso.grid(row=2, column=1)

txtIced_Latte = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,width=8,justify='left', textvariable=C4,state=DISABLED)
txtIced_Latte.grid(row=3, column=1)

txtCafe_Cortado = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,width=8,justify='left',textvariable=C5,state=DISABLED)
txtCafe_Cortado.grid(row=4, column=1)

txtCafe_Leite = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,width=8,justify='left',textvariable=C6,state=DISABLED)
txtCafe_Leite.grid(row=5, column=1)

txtCafe_Preto = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,width=8,justify='left',textvariable=C7,state=DISABLED)
txtCafe_Preto.grid(row=6, column=1)

txtCafe_creme = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,width=8,justify='left',textvariable=C8,state=DISABLED)
txtCafe_creme.grid(row=7, column=1)

txtCapuccino = Entry(framef1aa, font=('arial', 16, 'bold'), bd=1,width=8,justify='left',textvariable=C9,state=DISABLED)
txtCapuccino.grid(row=8, column=1)

#Criando os campos de texto da Comida

txtBolo_Cafe = Entry(framef1ab, font=('arial', 16, 'bold'), bd=1,width=8,justify='left', textvariable=B1,state=DISABLED)
txtBolo_Cafe.grid(row=0, column=1)

txtBolo_Cenoura = Entry(framef1ab, font=('arial', 16, 'bold'), bd=1,width=8,justify='left',textvariable=B2,state=DISABLED)
txtBolo_Cenoura.grid(row=1, column=1)

txtBolo_Milho = Entry(framef1ab, font=('arial', 16, 'bold'), bd=1,width=8,justify='left',textvariable=B3,state=DISABLED)
txtBolo_Milho.grid(row=2, column=1)

txtBolo_Banana = Entry(framef1ab, font=('arial', 16, 'bold'), bd=1,width=8,justify='left',textvariable=B4,state=DISABLED)
txtBolo_Banana.grid(row=3, column=1)

txtBolo_Morango = Entry(framef1ab, font=('arial', 16, 'bold'), bd=1,width=8,justify='left',textvariable=B5,state=DISABLED)
txtBolo_Morango.grid(row=4, column=1)

txtBolo_Limao = Entry(framef1ab, font=('arial', 16, 'bold'), bd=1,width=8,justify='left',textvariable=B6,state=DISABLED)
txtBolo_Limao.grid(row=5, column=1)

txtTorta_Limao = Entry(framef1ab, font=('arial', 16, 'bold'), bd=1,width=8,justify='left',textvariable=B7,state=DISABLED)
txtTorta_Limao.grid(row=6, column=1)

txtBolo_Chocolate = Entry(framef1ab, font=('arial', 16, 'bold'), bd=1,width=8,justify='left',textvariable=B8,state=DISABLED)
txtBolo_Chocolate.grid(row=7, column=1)

txtTorta = Entry(framef1ab, font=('arial', 16, 'bold'), bd=1,width=8,justify='left',textvariable=B9,state=DISABLED)
txtTorta.grid(row=8, column=1)

#Campo Recibo

lblRecibo = Label(frameft2,font=('arial', 12, 'bold'),  text='Recibo do Cliente:', bd=2, anchor=W)
lblRecibo.grid(row=0, column=0, sticky=W)

txtrecibo=Text(frameft2,width=59, height=28,bg='white', bd=8, font=('arial', 10))
txtrecibo.grid(row=1,column=0)

#Criando os Campos do Rodapé  Frame da Direta

lblimpostos = Label(framef2ab,font=('arial', 12, 'bold'), text='Impostos:',  bd=2)
lblimpostos.grid(row=0, column=0, sticky=W)

txtimpostos = Entry(framef2ab,font=('arial', 12, 'bold'), bd=1, justify='left', textvariable=Impostos)
txtimpostos.grid(row=0,column=1)

lblsubtotal = Label(framef2ab,font=('arial', 12, 'bold'), text='Sub Total:', bd=2)
lblsubtotal.grid(row=1, column=0, sticky=W)

txtsubtotal = Entry(framef2ab,font=('arial', 12, 'bold'), bd=1, justify='left', textvariable=Subtotal)
txtsubtotal.grid(row=1,column=1)

lbltotal = Label(framef2ab,font=('arial', 12, 'bold'), text='Total:', bd=2)
lbltotal.grid(row=2, column=0, sticky=W)

txttotal = Entry(framef2ab,font=('arial', 12, 'bold'), bd=1, justify='left',textvariable=Total)
txttotal.grid(row=2,column=1)

#Criando os Campos do Rodapé  Frame da Esqueda

lblcustobebidas = Label(framef2aa,font=('arial', 12, 'bold'), text='Custo Bebidas:', bd=2)
lblcustobebidas.grid(row=0, column=0, sticky=W)

txtcustobebidas = Entry(framef2aa,font=('arial', 12, 'bold'), bd=1, justify='left',textvariable=TotalBebidas)
txtcustobebidas.grid(row=0,column=1)

lblcustobolos = Label(framef2aa,font=('arial', 12, 'bold'), text='Custo Bolos:', bd=2)
lblcustobolos.grid(row=1, column=0, sticky=W)

txtcustobolos = Entry(framef2aa,font=('arial', 12, 'bold'), bd=1, justify='left', textvariable=TotalBolo)
txtcustobolos.grid(row=1,column=1)

lbltaxasservicos = Label(framef2aa,font=('arial', 12, 'bold'), text='Taxas Serviços:', bd=2)
lbltaxasservicos.grid(row=2, column=0, sticky=W)

txtservicos = Entry(framef2aa,font=('arial', 12, 'bold'), bd=1, justify='left', textvariable=taxaservicos)
txtservicos.grid(row=2,column=1)

#trocando a cor de fundo dos frames

Tops.configure(background='gray')
framef1.configure(background='gray')
frameft2.configure(background='SkyBlue1')

#Campo dos Botoes

cmTotal = Button(framefb2,padx=16,pady=1,bd=4,bg='black',fg='white', font=('arial',12, 'bold'),width=5,
                 text='Total',command=custoItem).grid(row=0, column=0)
cmRecibo = Button(framefb2,padx=16,pady=1,bd=4,bg='black',fg='green', font=('arial',12, 'bold'),  width=5,
                 text='Recibo').grid(row=0, column=1)
cmLimpar = Button(framefb2,padx=16,pady=1,bd=4,bg='black',fg='yellow', font=('arial',12, 'bold'),width=5,
                 text='Limpar', command=Limpar).grid(row=0, column=2)
cmSair = Button(framefb2,padx=16,pady=1,bd=4,bg='black',fg='red', font=('arial',12, 'bold'),width=5,
                 text='Sair',command=iExit).grid(row=0, column=3)



root.mainloop()




