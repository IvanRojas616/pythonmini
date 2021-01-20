from tkinter import *
from PIL import Image, ImageTk
import google_trans_new
import os
from google_trans_new import google_translator, LANGUAGES

root = Tk()

frameImage = Frame(root)
frameImage.pack()

def translate(obj, objTo, tolang):
    try:
        translator= google_translator()
        text = str(objTo.get("1.0",END))
        print(text)
        translation = translator.translate(text,lang_tgt=tolang)
        obj.delete(1.0,"end")
        obj.insert(1.0, translation)
    except Exception as e:
        print("Error!!!",e.args)
fileDir = os.path.dirname(os.path.abspath(__file__))
img = Image.open(os.path.join(fileDir,"traductor.png"))
out = img.resize((200, 200), Image.ANTIALIAS)#redimensionamos la imagen
imgFinal = ImageTk.PhotoImage(out)#luego usamos ImageTk, para usarla en Tkinter
#recordar que no estamos usando el PhotoImage común sino el de Pillow
Label(frameImage,image=imgFinal).grid(row=0,column=0,columnspan=2)

frameTraductor = Frame(root)

entradaIdiomaObjetivo = Entry(frameTraductor,justify="center")
entradaIdiomaObjetivo.grid(row=0,column=0,pady=20,padx=20,columnspan=5)

textTo = Text(frameTraductor,width=50,height=20,wrap=WORD)
textTo.grid(row=1,column=1,pady=10)

textTradu = Text(frameTraductor,width=50,height=20,wrap=WORD)
textTradu.grid(row=1,column=3,pady=10)

scrollOne = Scrollbar(frameTraductor,command=textTo.yview,orient=VERTICAL,	
cursor="exchange")
scrollOne.grid(row=1, column=0, sticky="nsew")

scrollTwo = Scrollbar(frameTraductor,command=textTradu.yview,orient=VERTICAL,	
cursor="exchange")
scrollTwo.grid(row=1, column=4, sticky="nsew")

textTo.config(yscrollcommand=scrollOne.set)
textTradu.config(yscrollcommand=scrollTwo.set)

traductor = Button(frameTraductor, text="Go",padx=20)
traductor.config(command = lambda:translate(textTradu, textTo,entradaIdiomaObjetivo.get()))
traductor.grid(row=1,column=2)

if not os.path.isfile("countries.txt"):
    with open("countries.txt","w") as data:
        for k,v in LANGUAGES.items():
            data.write(k + '->' + v + '\n')
else:
    print("File exists")
frameTraductor.pack()

root.mainloop()
