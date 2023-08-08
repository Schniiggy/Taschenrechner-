import tkinter as tk
from tkinter import ttk

#fenster
root = tk.Tk()
root.geometry("300x390")
root.title("Taschenrechner")
root.resizable(width=False,height=False)


feld_t = " "

#Ausgabe im Textfeld
def zum_feld(etw):
    global feld_t
    feld_t += str(etw)
    ausgabe.delete(1.0 , "end")
    ausgabe.insert(1.0 , feld_t)

#Berechnen
def calculate():
    global feld_t
    result=str(eval(feld_t))
    ausgabe.delete(1.0 , "end")
    ausgabe.insert(1.0 , result)

#Text im Textfeld löschen
def löschen():
    global feld_t
    feld_t = ""
    ausgabe.delete("1.0" , "end")


#Hier sind die Ganzen Buttons / Texte

ausgabe = tk.Text(root,width=35, height= 3, bg="#2e2e2e",fg="#ffffff")
ausgabe.grid( padx=10,pady=10, columnspan=10)

button1 = tk.Button(root, text="1", command=lambda: zum_feld(1),height=2,width=12, bg="#383838",fg="white" )
button1.grid(row=2,column=1, padx=2,pady=2)
button2 = tk.Button(root, text="2", command=lambda: zum_feld(2) ,height=2,width=12, bg="#383838",fg="white")
button2.grid(row=2,column=2, padx=2,pady=2)
button3 = tk.Button(root, text="3",  command=lambda: zum_feld(3),height=2,width=12, bg="#383838",fg="white")
button3.grid(row=2,column=3, padx=2,pady=2)
#Obere reie Fertig (1-3)

button4 = tk.Button(root, text="4",  command=lambda: zum_feld(4),height=2,width=12, bg="#383838",fg="white")
button4.grid(row=3,column=1, padx=2,pady=2)
button5 = tk.Button(root, text="5", command=lambda: zum_feld(5), height=2,width=12, bg="#383838",fg="white")
button5.grid(row=3,column=2, padx=2,pady=2)
button6 = tk.Button(root, text="6",  command=lambda: zum_feld(6),height=2,width=12, bg="#383838",fg="white")
button6.grid(row=3,column=3, padx=2,pady=2)
#Mittlere reihe fertig (4-6)

button7 = tk.Button(root, text="7",  command=lambda: zum_feld(7),height=2,width=12, bg="#383838",fg="white")
button7.grid(row=4,column=1, padx=2,pady=2)
button8 = tk.Button(root, text="8",  command=lambda: zum_feld(8),height=2,width=12, bg="#383838",fg="white")
button8.grid(row=4,column=2, padx=2,pady=2)
button9 = tk.Button(root, text="9", command=lambda: zum_feld(9), height=2,width=12, bg="#383838",fg="white")
button9.grid(row=4,column=3, padx=2,pady=2)
#untere reihe fertig (7-9)

buttonp = tk.Button(root, text="+",  command=lambda: zum_feld("+"),height=2,width=12, bg="#963e03",fg="white")
buttonp.grid(row=7,column=1, padx=2,pady=2)
button0 = tk.Button(root, text="0",  command=lambda: zum_feld(0),height=2,width=12, bg="#383838",fg="white")
button0.grid(row=5,column=2, padx=2,pady=2)
buttons = tk.Button(root, text="*",  command=lambda: zum_feld("*"),height=2,width=12, bg="#963e03",fg="white")
buttons.grid(row=7,column=3, padx=2,pady=2)
#0,+,* gemacht

buttong = tk.Button(root, text="/",  command=lambda: zum_feld("/"),height=2,width=12, bg="#963e03",fg="white")
buttong.grid(row=6,column=1, padx=2,pady=2)
buttonm = tk.Button(root, text="-", command=lambda: zum_feld("-"), height=2,width=12, bg="#963e03",fg="white")
buttonm.grid(row=6,column=2, padx=2,pady=2)
buttoni = tk.Button(root, text="=", command=lambda: calculate(), height=2,width=12, bg="#963e03",fg="white")
buttoni.grid(row=6,column=3, padx=2,pady=2)

quitb = tk.Button(root, text="Ende",height=2,width=12, bg="#8a1c1c",fg="white",command=root.destroy)
quitb.grid(row=8,column=2,pady=2)

loeschen = tk.Button(root, text="Löschen", height=2,width=12, bg="#8a1c1c",fg="white", command=lambda: löschen())
loeschen.grid(row=7,column=2,pady=2)

buttonkr= tk.Button(root, text="(",  command=lambda: zum_feld("("),height=2,width=12, bg="#963e03",fg="white")
buttonkr.grid(row=5,column=1, padx=2,pady=2)

buttonkr = tk.Button(root, text=")",  command=lambda: zum_feld(")"),height=2,width=12, bg="#963e03",fg="white")
buttonkr.grid(row=5,column=3, padx=2,pady=2)



#Hintergrund in Schwarz gemacht
root.configure(bg= "#171717")

root.mainloop()
