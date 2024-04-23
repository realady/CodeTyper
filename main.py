import pyperclip
import pyautogui
import time
import tkinter as tk
from tkinter import ttk

def autotype_clipboard():
    time.sleep(5)
    clipboard_text = pyperclip.paste().split("\n")

    for line in clipboard_text:
        for char in line:
            pyautogui.write(char)
            if char in ["[", '"', "'", "("]:
                pyautogui.press("delete")
        
        pyautogui.press(["enter", "home"])

def on_start():
    autotype_clipboard()

def create_ui():
    root = tk.Tk()
    root.title("Autotyper")
    root.geometry("500x350")  # Increase the window size
    root.attributes("-topmost", True)  # Make the window always on top

    header_frame = tk.Frame(root, bg="#e74c3c")
    header_frame.pack(fill="x", pady=20)

    header_label = tk.Label(header_frame, text="CodeTyper", font=("Helvetica", 20, "bold"), foreground="white", background="#e74c3c")
    header_label.pack()

    instructions_frame = tk.Frame(root)
    instructions_frame.pack(pady=20, padx=30)  # Increase padding

    instructions_label = tk.Label(instructions_frame, text="Instructions:", font=("Helvetica", 14), anchor="center")
    instructions_label.pack()

    instructions = [
        "1. Copy the text you want to type.",
        "2. Click the 'Start' button.",
        "3. Place the cursor where you want to type the text.",
        "4. The program will type the copied text with correct indentation."
    ]

    for instruction in instructions:
        instruction_label = tk.Label(instructions_frame, text=instruction, font=("Helvetica", 12), anchor="center")
        instruction_label.pack()

    start_button = ttk.Button(root, text="Start", command=on_start)
    start_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
