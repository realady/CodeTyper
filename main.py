import pyautogui
import pyperclip
import time
import tkinter as tk
from tkinter import ttk
import threading
import keyboard

class AccurateCodeAutoTyper:
    def __init__(self, master):
        self.master = master
        master.title("Code Tantra Auto Typer")
        master.geometry("350x450")  # Adjusted window size
        master.configure(bg="#1c1c1c")

        # Remove window decorations
        master.overrideredirect(True)
        # Keep the window always on top
        master.wm_attributes("-topmost", True)

        self.running = False
        self.paused = False
        self.clipboard_text = []
        self.current_index = 0  # Track where we left off in clipboard text

        self.create_widgets()

        # Bind mouse events for dragging
        self.master.bind("<Button-1>", self.on_start_drag)
        self.master.bind("<B1-Motion>", self.on_drag)

        # Set up global hotkeys
        keyboard.add_hotkey('f6', self.toggle_typing)
        keyboard.add_hotkey('f7', self.toggle_pause)
        keyboard.add_hotkey('esc', self.stop_typing)
        keyboard.add_hotkey('ctrl+shift+x', self.exit_program)
        keyboard.add_hotkey('ctrl+shift+m', self.toggle_hide)

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#1c1c1c")
        style.configure("TButton", background="#282828", foreground="#ffffff", font=("Arial", 10))
        style.configure("TLabel", background="#1c1c1c", foreground="#ffffff", font=("Arial", 10))
        style.configure("TLabelFrame", background="#1c1c1c", foreground="#ffffff")

        # Title and Subheading
        title_label = ttk.Label(self.master, text="Auto Typer", font=("Arial", 14, "bold"), foreground="#00ff00")
        title_label.pack(pady=(10, 5))

        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Buttons
        self.start_button = ttk.Button(main_frame, text="Start Typing (F6)", command=self.toggle_typing)
        self.start_button.pack(fill=tk.X, pady=(5, 5))

        self.pause_button = ttk.Button(main_frame, text="Pause/Resume Typing (F7)", command=self.toggle_pause)
        self.pause_button.pack(fill=tk.X, pady=(5, 5))

        # Status Label
        self.status_label = ttk.Label(main_frame, text="Status: Idle", font=('Arial', 10, 'bold'))
        self.status_label.pack(pady=(5, 10))

        # Countdown Timer Visualizer
        self.timer_label = ttk.Label(main_frame, text="", font=('Arial', 12), foreground="#ffcc00")
        self.timer_label.pack(pady=(5, 10))

        # Instructions
        ttk.Label(main_frame, text="Instructions:", font=("Arial", 12, "bold"), foreground="#ffffff").pack(pady=(5, 5))

        # Instructions Text
        self.instructions_text = tk.Text(main_frame, height=14, wrap=tk.WORD, background="#1c1c1c", foreground="#f0f0f0",
                                         font=("Arial", 9), bd=0, padx=5, pady=5)
        self.instructions_text.pack(fill=tk.BOTH, expand=True, pady=(5, 10))
        self.add_instructions()

        ttk.Label(main_frame, text="F6: Start/Stop Typing | F7: Pause/Resume | Esc: Stop | Ctrl+Shift+X: Exit | Ctrl+Shift+M: Hide/Unhide",
                  font=("Arial", 8), foreground="#ffffff").pack(pady=(5, 5))

    def add_instructions(self):
        self.instructions_text.insert(tk.END, "Imporatant Stuff!\n", "header")
        self.instructions_text.insert(tk.END, "\nHow to use:\n", "subheader")
        self.instructions_text.insert(tk.END, "- Press ", "normal")
        self.instructions_text.insert(tk.END, "F6 ", "key")
        self.instructions_text.insert(tk.END, "to start or stop typing.\n", "normal")
        self.instructions_text.insert(tk.END, "- Press ", "normal")
        self.instructions_text.insert(tk.END, "F7 ", "key")
        self.instructions_text.insert(tk.END, "to pause or resume typing.\n", "normal")
        self.instructions_text.insert(tk.END, "- Press ", "normal")
        self.instructions_text.insert(tk.END, "Esc ", "key")
        self.instructions_text.insert(tk.END, "to stop typing.\n", "normal")
        self.instructions_text.insert(tk.END, "- Press ", "normal")
        self.instructions_text.insert(tk.END, "Ctrl+Shift+X ", "key")
        self.instructions_text.insert(tk.END, "to exit the program.\n", "normal")
        self.instructions_text.insert(tk.END, "- Press ", "normal")
        self.instructions_text.insert(tk.END, "Ctrl+Shift+M ", "key")
        self.instructions_text.insert(tk.END, "to hide or unhide the program.\n", "normal")

        # Configure text tags for formatting
        self.instructions_text.tag_configure("header", font=("Arial", 12, "bold"), foreground="#00ff00")
        self.instructions_text.tag_configure("subheader", font=("Arial", 10, "bold"), foreground="#ffcc00")
        self.instructions_text.tag_configure("normal", font=("Arial", 9), foreground="#f0f0f0")
        self.instructions_text.tag_configure("key", font=("Arial", 9, "bold"), foreground="#00ccff")

        self.instructions_text.config(state=tk.DISABLED)  # Make it read-only

    def countdown(self, duration):
        for i in range(duration, 0, -1):
            if not self.running:
                break
            self.timer_label.config(text=f"Starting in {i}...")
            time.sleep(1)
        self.timer_label.config(text="")

    def autotype_clipboard(self):
        if not self.clipboard_text:
            self.clipboard_text = pyperclip.paste().split("\n")

        for i in range(self.current_index, len(self.clipboard_text)):
            if not self.running or self.paused:
                break
            line = self.clipboard_text[i]
            pyautogui.write(line, interval=0.005)  # Reduced interval for faster typing
            for char in line:
                if char in ["[", '"', "'", "("]:
                    pyautogui.press("delete")
            pyautogui.press("enter")
            pyautogui.press("home")
            self.current_index = i + 1  # Update current index

    def toggle_typing(self):
        if not self.running:
            self.running = True
            self.paused = False
            self.start_button.config(text="Stop Typing (F6)")
            self.status_label.config(text="Status: Typing", foreground="#00ff00")
            threading.Thread(target=self.delayed_start, daemon=True).start()
        else:
            self.stop_typing()

    def delayed_start(self):
        self.countdown(5)
        self.autotype_clipboard()

    def toggle_pause(self):
        if self.running:
            self.paused = not self.paused
            if self.paused:
                self.status_label.config(text="Status: Paused", foreground="#ffcc00")
            else:
                self.status_label.config(text="Status: Typing", foreground="#00ff00")
                threading.Thread(target=self.delayed_resume, daemon=True).start()

    def delayed_resume(self):
        self.countdown(5)
        self.autotype_clipboard()

    def stop_typing(self):
        self.running = False
        self.paused = False
        self.current_index = 0  # Reset typing point
        self.clipboard_text = []  # Clear clipboard text
        self.start_button.config(text="Start Typing (F6)")
        self.status_label.config(text="Status: Stopped", foreground="#ff0000")

    def exit_program(self):
        self.master.destroy()

    def toggle_hide(self):
        if self.master.state() == "normal":
            self.master.withdraw()
        else:
            self.master.deiconify()

    def on_start_drag(self, event):
        self.x = event.x
        self.y = event.y

    def on_drag(self, event):
        dx = event.x - self.x
        dy = event.y - self.y
        new_x = self.master.winfo_x() + dx
        new_y = self.master.winfo_y() + dy
        self.master.geometry(f'+{new_x}+{new_y}')

if __name__ == "__main__":
    root = tk.Tk()
    app = AccurateCodeAutoTyper(root)
    root.mainloop()
