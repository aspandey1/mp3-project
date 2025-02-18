import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def show_main_frame(main_frame, mp3_info):

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

    notes_label = tk.Label(main_frame, justify="left", text="Notes:", font=("Arial", 10, "bold"))
    bullet1_label = tk.Label(main_frame, justify="left", text=" * Enter desired information above")
    bullet2_label = tk.Label(main_frame, justify="left", text=" * Fill in any missing information")
    bullet3_label = tk.Label(main_frame, justify="left", text=" * Year must be a numeric value")

    next_button = tk.Button(main_frame, text="NEXT", font=("Arial", 10, "bold"), command=lambda: submit_form(title_entry.get(), artist_entry.get(), year_entry.get(), album_entry.get()))

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

    notes_label.grid(row = 5, column=0, columnspan=3, sticky="W", padx=(20, 0), pady=5)
    bullet1_label.grid(row = 6, column=0, columnspan=3, sticky="W", padx=(20, 0), pady=2)
    bullet2_label.grid(row = 7, column=0, columnspan=3, sticky="W", padx=(20, 0), pady=2)
    bullet3_label.grid(row = 8, column=0, columnspan=3, sticky="W", padx=(20, 0), pady=2)

    next_button.grid(row=8, column=2, sticky="SE", padx=(0, 10))

    main_frame.pack()

def submit_form(user_title, user_artist, user_year, user_album):
    # Check for missing fields and show specific error messages
    if not user_title.strip():
        messagebox.showerror("Error", "Title field cannot be empty!")
        return

    if not user_artist.strip():
        messagebox.showerror("Error", "Artist field cannot be empty!")
        return

    if not user_year.strip():
        messagebox.showerror("Error", "Year field cannot be empty!")
        return

    if not user_album.strip():
        messagebox.showerror("Error", "Album field cannot be empty!")
        return

    # Ensure year is numeric and exactly 4 digits
    if not user_year.isdigit():
        messagebox.showerror("Error", "Year must be a numeric value!")
        return

    return True  # All validations passed