from tkinter import *
from pytube import *
from PIL import Image
import os
#pytube debe instalarse el pytube3 luego el pytube normal, lo hice con sudo su

root = Tk()
root.resizable(False,False)
root.title("Youtube Downloader")

frame = Frame(root)
frame.pack()

def downloadVideo(textfield):
    try:
        url = textfield.get()
        yt = YouTube(url)
        stream = yt.streams.first()
        print(stream)
        stream.download(os.path.dirname(os.path.abspath(__file__)))
    except Exception as e:
        print(e.args)

image = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)),"yt.png"))
image = image.subsample(3)
imageYt = Label(frame, image=image)
imageYt.grid(row=0,column=0,padx=20,pady=20)

urlField = Entry(frame, relief="sunken", width=40)
urlField.grid(row=1,column=0,pady=20,padx=20)

buttonDownload = Button(frame,width=10,height=2, text="Download", bg="orange", command=lambda:downloadVideo(urlField))
buttonDownload.grid(row=2,column=0,pady=20)


root.mainloop()

