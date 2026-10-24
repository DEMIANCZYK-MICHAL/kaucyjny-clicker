import tkinter as Tk
import random 
from PIL import Image, ImageTk

hajs = 0
iloscdodawania = 0.5
poziom = 0
root = Tk.Tk()
root.geometry("300x300")
root.title("Butelkowy CLICKER")
img = Image.open("kaucja.jpg")
img = img.resize((100,100))
foto = ImageTk.PhotoImage(img)


def upgrade():
    global iloscdodawania
    global ulepsz
    global info
    global hajs
    global poziom
    if poziom == 0:
        if hajs >= 35:
            hajs -= 35
            iloscdodawania = 1.0
            ulepsz.config(text="Ulepsz wartosc butelki (70zl)")
            info.config(text=f"ulepszono teraz zbierasz {iloscdodawania} zl \n za butelke nazwa ulepszenie: szklana butelka")
            poziom = 1

        else:
            info.config(text="masz za mało hajsu!")
    elif poziom == 1:
        if hajs >= 70:
            hajs -= 70
            iloscdodawania = 1.5
            ulepsz.config(text="ulepsz wartosc butelki (100zl)")
            info.config(text=f"ulepszono teraz zbierasz {iloscdodawania} zl \n za butelke, nazwa ulepszenia: Szklana butelka i normalna w JEDNYM!?")
            poziom = 2
        else:
            info.config(text="masz za mało hajsu!")
    elif poziom == 2:
        if hajs >= 100:
            hajs -= 100
            iloscdodawania = 2.0
            ulepsz.config(text="ulepsz wartosc butelki (500zl)")
            info.config(text=f"ulepszono teraz zbierasz {iloscdodawania} zl \n za butelke, nazwa ulepszenia: Szklana butelka i 2 normalne :)")
            poziom = 3
    elif poziom == 3:
        if hajs >= 500:
            hajs -= 500
            iloscdodawania = 2.5
            ulepsz.config(text="ulepsz wartosc butelki (700zl)")
            info.config(text=f"ulepszono teraz zbierasz {iloscdodawania} zl \n za butelke, nazwa ulepszenia: 2 szklane butelki i 1 normalna :)")
            poziom = 4
    elif poziom == 4:
        if hajs >= 700:
            hajs -= 700
            iloscdodawania = 3.0
            ulepsz.config(text=f"ulepsz wartosc butelki (1000zl)")
            info.config(text=f"Ulepszono teraz zbierasz {iloscdodawania} zl \n za butelke nazwa ulepszenia: 3 szklane")
            poziom = 5
    elif poziom == 5:
        if hajs >= 1000:
            hajs -= 1000
            iloscdodawania = 3.5
            ulepsz.config(text="Ulepsz wartosc butelki (1600zl)")
            info.config(text=f"Ulepszono teraz zbierasz {iloscdodawania} zl \n za butelke nazwa ulepszenia: 3 szklane I JEDNA NORMALNA")
            poziom = 6
    elif poziom == 6:
        if hajs >= 1600:
            hajs -= 1600
            ulepsz.config(text="Ulepsz Wartosc butelki (2000zl)")
            iloscdodawania = 4.5
            info.config(text=f"Ulepszono teraz zbierasz {iloscdodawania} zl \n za butelke nazwa ulepszenia: ktos tu oscamowal butelkomat!! \n 4.5zl za BUTELKE?!")
            poziom = 7
    elif poziom == 7:
        if hajs >= 2000:
            hajs -= 2000
            ulepsz.config(text="Ulepsz wartosc butelki (2300zl)")
            iloscdodawania = 5
            info.config(text=f"Ulepszono teraz zbierasz {iloscdodawania} zl \n za butelke nazwa ulepszenia: kierowniku poratuj 5zl hehe ")
            poziom = 8
    elif poziom == 8:
        if hajs >= 2300:
            hajs -= 2300
            ulepsz.config(text="Ulepsz wartosc butelki (2800zl)")
            iloscdodawania = 6.5
            info.config(text=f"Ulepszono teraz zbierasz {iloscdodawania} zl \n za butelke nazwa ulepszenia: kaucja kaucja kaucja kauuuuuuuuucjaaaaaaaa ")
            poziom = 9
    elif poziom == 9:
        if hajs >= 2800:
            hajs -= 2800
            ulepsz.config(text="Ulepsz wartosc butelki (3400zl)")
            iloscdodawania = 8.5
            info.config(text=f"Ulepszono teraz zbierasz {iloscdodawania} zl \n za butelke nazwa ulepszenia: prawie dyszka za butelke")
            poziom = 10
    elif poziom == 10:
        if hajs >= 3400:
            hajs -= 3400
            ulepsz.config(text="Ulepsz wartosc butelki (5000zl!!!)")
            iloscdodawania = 9.5
            info.config(text=f"Ulepszono teraz zbierasz {iloscdodawania} zl \n za butelke nazwa ulepszenia: co robi 9zl w portfelu? ledwo dycha!")
            poziom = 11
    elif poziom == 11:
        if hajs >= 5000:
            hajs -= 5000
            iloscdodawania = 10
            info.config(text=f"Ulepszono teraz zbierasz {iloscdodawania} zl \n za butelke nazwa ulepszenia: dycha!")
            ulepsz.config(text="Max ulepszenie", state="disabled")
            
        
            
            



        
            
        
            

            


def kliknieto():
    global hajs
    global text
    global kliknij
    global ulepsza
    global info
    randomik = random.randint(1,500)
    randomik2 = random.randint(1,500000)
    if hajs == 10000:
        kliknij.config(state="disabled")
        ulepsz.config(state="disabled")
        info.config(text="WYGRALES!!!!!!!!! CHCESZ WERSJE BEZ KONCA??????? WEJDZ NA GITHUBA MICHALDEMIANCZYK (TAM GDZIE POBRALES TEN CLICKER) \n I ZNAJDZ REPO POD NAZWA: KAUCYJNY CLICKER NO END \n I POBIERZ NAJNOWSZE WYDANIE!")
    if randomik == 250:
        hajs += 10.0
        info.config(text="BRAWO OTRZYMALES PERKE ZDOBYWASZ ZA TA BUTELKE 10ZL!!! ")
    if randomik2 == 450000:
        hajs += 1000.0
        info.config(text="brawo zdobyles perke 1000zl!!!! ")
    else:
    
        hajs += iloscdodawania
        
        text.config(text=f"{hajs} zl")

kliknij = Tk.Button(root,image=foto, command=kliknieto,activebackground="blue")
kliknij.pack(pady=40,padx=0)
text = Tk.Label(root,text=f"{hajs} zl")
text.pack(pady=0,padx=0)
ulepsz = Tk.Button(root,text="Ulepsz wartosc butelki  (35zl)",command=upgrade)
ulepsz.pack()
info = Tk.Label(root,text="")
info.pack(pady=50,padx=0)


root.mainloop()