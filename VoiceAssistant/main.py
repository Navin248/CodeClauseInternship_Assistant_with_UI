import tkinter as tk
from PIL import Image, ImageTk
from assistant import GetAI

# Create root window
root = tk.Tk()

# Set root window title and dimension
root.title("Robo: Your AI assistant")
root.geometry('500x400')

# Load and prepare background image
bg_image = Image.open("bg.jpg")  # Replace "background.png" with your image path
bg_image = bg_image.resize((500, 400) , Image.Resampling.BOX) # Example using BILINEAR filter
 # Resize to match window size (optional)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label for the background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)
# all widgets will be here
mic_string_var = tk.StringVar()

chatbox = tk.Text(root, bg="#ededed", fg="black", font=("Arial", 10),
               width=48, height=6, padx=10)
chatbox.config(state=tk.DISABLED)
chatbox.place(relx=0.5, rely=0.7, anchor='center')
 
# chatbox_scrollbar = Scrollbar(chatbox)
# chatbox_scrollbar.place(relheight=1.1, relx=0.99, rely=-0.05)

chatai = GetAI(root=root, status_text_var=mic_string_var, chatbox=chatbox)

# add mic button to the root window
mic_icon_image = Image.open("mic.png")
mic_icon_photo = ImageTk.PhotoImage(mic_icon_image)
mic_button = tk.Button(root, image=mic_icon_photo,
                    command=chatai.generateResponse, height=90, width=90,
                    borderwidth=0)
mic_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

# add a label to the root window
mic_string_var.set("Hi, click on the mic to speak")
status_label = tk.Label(root, textvariable=mic_string_var,
                     font=("Arial", 18))
status_label.place(relx=0.5, rely=0.45, anchor='center')


# Execute Tkinter
root.mainloop()
