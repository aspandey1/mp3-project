import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from audio import get_info
from main_frame import show_main_frame

# select_mp3_button action
def select_mp3():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file_path:
        mp3_file_info = get_info(file_path)
        welcome_frame.pack_forget()
        show_main_frame(main_frame, mp3_file_info)

# root
root = tk.Tk()
root.geometry("600x400")
root.title("MP3 Editor")

# welcome frame
welcome_frame = tk.Frame(root)
welcome_frame.pack()

# open image
img = Image.open("images/icon.png")
img = img.resize((200,200))
img_tk = ImageTk.PhotoImage(img)

# display image
icon = tk.Label(welcome_frame, image=img_tk)
icon.pack(pady=30)

# welcome text
welcome_label = tk.Label(welcome_frame, text="SELECT MP3 FILE", font=("helvetica 20 bold"))
welcome_label.pack()

# button
select_mp3_button = tk.Button(welcome_frame, text="BROWSE", font=("Arial", 10, "bold"), command=select_mp3)
select_mp3_button.pack(pady=20)

# for next frame
main_frame = tk.Frame(root)

root.mainloop()