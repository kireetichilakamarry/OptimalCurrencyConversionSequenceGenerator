import customtkinter
import tkinter

customtkinter.set_appearance_mode('dark')  # Set dark mode
customtkinter.set_default_color_theme('dark-blue')  # Set color theme

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Test")

# Frame to contain other widgets
frame = customtkinter.CTkFrame(master=root, fg_color="#2a2d2e")  # Darker than the default to ensure contrast
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Label with contrasting text color
label = customtkinter.CTkLabel(master=frame, text="Login System", text_color="white")
label.pack(pady=12, padx=10)

# Entries for username and password
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username", fg_color="#434547", text_color="white")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show='*', fg_color="#434547", text_color="white")
entry2.pack(pady=12, padx=10)

# Login button with contrasting text and background color
button = customtkinter.CTkButton(master=frame, text="Login", command=login, fg_color="#0052cc", text_color="white")
button.pack(pady=12, padx=10)

# Checkbox for "Remember Me" option
checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me", text_color="white")
checkbox.pack(pady=12, padx=10)

root.mainloop()
