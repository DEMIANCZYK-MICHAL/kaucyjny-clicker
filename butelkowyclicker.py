import tkinter as Tk
hajs = 0
iloscdodawania = 0.5
poziom = 0
root = Tk.Tk()
root.geometry("300x300")
root.title("Butelkowy CLICKER")


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
            ulepsz.config(text="max ulepszenie",state="disabled")
            info.config(text=f"ulepszono teraz zbierasz {iloscdodawania} zl \n za butelke, nazwa ulepszenia: 2 szklane butelki i 1 normalna :)")
            

        
            
        
            

            


def kliknieto():
    global hajs
    global text
    global kliknij
    global ulepsz
    if hajs == 10000:
        kliknij.config(state="disabled")
        ulepsz.config(state="disabled")
        info.config(text="WYGRALES!!!!!!!!! CHCESZ WERSJE BEZ KONCA??????? WEJDZ NA GITHUBA MICHALDEMIANCZYK (TAM GDZIE POBRALES TEN CLICKER) \n I ZNAJDZ REPO POD NAZWA: KAUCYJNY CLICKER NO END \n I POBIERZ NAJNOWSZE WYDANIE!")

    hajs += iloscdodawania
    print(hajs,"zl")
    text.config(text=f"{hajs} zl")
kliknij = Tk.Button(root,text="kaucja", command=kliknieto,activebackground="blue")
kliknij.pack(pady=40,padx=0)
text = Tk.Label(root,text=f"{hajs} zl")
text.pack(pady=0,padx=0)
ulepsz = Tk.Button(root,text="Ulepsz wartosc butelki  (35zl)",command=upgrade)
ulepsz.pack()
info = Tk.Label(root,text="")
info.pack(pady=50,padx=0)


root.mainloop()