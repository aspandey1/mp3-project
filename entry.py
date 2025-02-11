import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from audio import get_info

# select_mp3_button action
def select_mp3():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file_path:
        mp3_file_info = get_info(file_path)
        welcome_frame.pack_forget()
        show_main_frame(mp3_file_info)

def show_main_frame(mp3_info):

    file_name_label = tk.Label(main_frame, text=mp3_info["file_name"], font=("Arial", 15, "bold"))

    title_text = tk.Label(main_frame, text="TITLE", font=("Arial", 10, "bold"))
    title_entry = tk.Entry(main_frame, width=25)
    title_entry.insert(0, mp3_info["title"])

    artist_text = tk.Label(main_frame, text="ARTIST", font=("Arial", 10, "bold"))
    artist_entry = tk.Entry(main_frame, width=25)
    artist_entry.insert(0, mp3_info["artist"])

    year_text = tk.Label(main_frame, text="YEAR", font=("Arial", 10, "bold"))
    year_entry = tk.Entry(main_frame, width=25)
    year_entry.insert(0, mp3_info["year"])

    album_text = tk.Label(main_frame, text="ALBUM", font=("Arial", 10, "bold"))
    album_entry = tk.Entry(main_frame, width=25)
    album_entry.insert(0, mp3_info["album"])

    art_img = Image.open(mp3_info["art_path"])
    art_img = art_img.resize((170, 170))  # Resize for display
    art_img_tk = ImageTk.PhotoImage(art_img)

    notes_label = tk.Label(main_frame, justify="left", text="Notes:\n    Default for title is null\n    Default for artist is null\n    Default for year is 0000\n    Default for album is null")

    # Store reference to prevent garbage collection
    art_label = tk.Label(main_frame, image=art_img_tk)
    art_label.image = art_img_tk  # Keep reference
    art_label.grid(row=1, column=0, rowspan=4, pady=8, padx=20)

    file_name_label.grid(row = 0, column=0, columnspan=3, pady=25)
    
    title_text.grid(row = 1, column=1, sticky="E", pady=8, padx=10)
    title_entry.grid(row = 1, column = 2, sticky = "W", pady = 8, padx=10)

    artist_text.grid(row = 2, column=1, sticky="E", pady=8, padx=10)
    artist_entry.grid(row = 2, column = 2, sticky = "W", pady = 8, padx=10)

    year_text.grid(row = 3, column=1, sticky="E", pady=8, padx=10)
    year_entry.grid(row = 3, column = 2, sticky = "W", pady = 8, padx=10)

    album_text.grid(row = 4, column=1, sticky="E", pady=8, padx=10)
    album_entry.grid(row = 4, column = 2, sticky = "W", pady = 8, padx=10)

    notes_label.grid(row = 5, column=0, columnspan=2, sticky="W", padx=10)

    main_frame.pack()


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
select_mp3_button = tk.Button(welcome_frame, text="BROWSE", command=select_mp3)
select_mp3_button.pack(pady=20)

main_frame = tk.Frame(root)

root.mainloop()