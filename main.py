from tkinter import *
from tkinter import filedialog
from tkinter import Tk
from PIL import Image, ImageDraw, ImageFont



def add_watermark():
    watermark = watermark_entry.get()
    window.withdraw()
    root = Tk()
    root.withdraw()
    opened_image = Image.open(filedialog.askopenfilename(initialdir="/Users/user/Desktop", title="Select an Image:"))
    image_width, image_height = opened_image.size
    draw = ImageDraw.Draw(opened_image)
    font_size = int(image_width / 8)
    font = ImageFont.truetype('arial.ttf', font_size)
    x, y = int(image_width / 2), float(image_height / 1.2)
    draw.text((x, y), watermark, font=font, fill="#FFF", anchor="ms")
    opened_image.show()



window = Tk()
window.title("Watermark Manager")
window.config(padx=70, pady=70)


watermark_label = Label(text="Watermark:")
watermark_label.grid(row=0, column=0)

watermark_entry = Entry(width=65)
watermark_entry.grid(row=0, column=1)
watermark_entry.focus()


add_button = Button(text="Add", width=15, command=add_watermark)
add_button.grid(row=1, column=1)


window.mainloop()






