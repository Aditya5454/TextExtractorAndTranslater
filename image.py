import customtkinter # type: ignore
from PIL import Image
from tkinter import filedialog
import pytesseract as tess # type: ignore
tess.pytesseract.tesseract_cmd=r'C:\Users\Aditya\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

app = customtkinter.CTk()
app.geometry('600x450')
app.title('get text from image:')
 #creating frame---
frame=customtkinter.CTkFrame(app,corner_radius=20,border_color='#2596be',border_width=2)
frame.pack(padx=20,pady=20,fill='both')

text = customtkinter.CTkLabel(frame,text = "Extract text from image",font=('Ariel',20))
text.pack(pady=10)


#img = customtkinter.CTkImage(Image.open('C:\Users\Aditya\Downloads\img.png'), size=(42,42))

def openImage():
    progressbar.set(0)
    progress_text.configure(text='0%')
    filename = filedialog.askopenfilename()
    img = Image.open(filename)
    get_txt = tess.image_to_string(img)
    progressbar.start()
    progressbar.set(1)
    text_box.insert('0.0',get_txt)
    app.title(filename)
    progress_text.configure(text='100%')
    progressbar.stop()

btn = customtkinter.CTkButton(frame,text = 'Add Image',
                              text_color='#FFFFFF',
                              width = 200,
                              height= 30,
                              font = ('Arial',20),
                              command=openImage,
                              border_spacing=10
)
btn.pack(padx=20,pady=20)

#progress bar....
progressbar = customtkinter.CTkProgressBar(frame)
progressbar.pack(pady=20)
progressbar.set(0)


progress_text = customtkinter.CTkLabel(frame,text = "0%")
progress_text.place(x=350,y=144)

text_box = customtkinter.CTkTextbox(frame,font=('Arial',18),width=520,height=420)
text_box.pack(pady = 20)

app.mainloop()