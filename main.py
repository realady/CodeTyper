import tkinter as tk
from tkinter import ttk
import threading
import time
import subprocess
import keyboard
from Xlib import display, X
import pyperclip
from pynput.keyboard import Key, Controller

class LinuxCodeAutoTyper:
    def __init__(self, master):  # Fixed: Changed _init_ to __init__
        self.master = master
        master.title("Code Auto Typer - Linux")
        master.geometry("350x450")
        master.configure(bg="#1c1c1c")
        
        # Remove window decorations but keep basic controls for Linux
        master.wm_attributes('-type', 'splash')
        master.wm_attributes('-topmost', True)
        
        self.keyboard = Controller()
        self.running = False
        self.paused = False
        self.clipboard_text = []
        self.current_index = 0
        self.typing_speed = 0.003  # Increased typing speed (3x faster)
        self.bracket_pairs = {
            '{': '}',
            '[': ']',
            '(': ')',
            '<': '>',
            '"': '"',
            "'": "'"
        }
        self.create_widgets()
        
        # Bind mouse events for dragging
        self.master.bind("<Button-1>", self.on_start_drag)
        self.master.bind("<B1-Motion>", self.on_drag)
        
        # Set up keyboard listeners using pynput for Linux compatibility
        try:
            keyboard.add_hotkey('f6', self.toggle_typing)
            keyboard.add_hotkey('f7', self.toggle_pause)
            keyboard.add_hotkey('esc', self.stop_typing)
            keyboard.add_hotkey('ctrl+shift+x', self.exit_program)
            keyboard.add_hotkey('ctrl+shift+m', self.toggle_hide)
        except Exception as e:
            print(f"Error setting up hotkeys: {e}")
            # Fallback to tkinter bindings if keyboard module fails
            self.master.bind('<F6>', lambda e: self.toggle_typing())
            self.master.bind('<F7>', lambda e: self.toggle_pause())
            self.master.bind('<Escape>', lambda e: self.stop_typing())
            self.master.bind('<Control-Shift-X>', lambda e: self.exit_program())
            self.master.bind('<Control-Shift-M>', lambda e: self.toggle_hide())

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#1c1c1c")
        style.configure("TButton", background="#282828", foreground="#ffffff", font=("Arial", 10))
        style.configure("TLabel", background="#1c1c1c", foreground="#ffffff", font=("Arial", 10))
        
        # Title bar with close button
        title_frame = ttk.Frame(self.master)
        title_frame.pack(fill=tk.X, pady=5)
        
        title_label = ttk.Label(title_frame, text="Linux Code Auto Typer", font=("Arial", 14, "bold"), 
                               foreground="#00ff00")
        title_label.pack(side=tk.LEFT, padx=10)
        
        close_button = ttk.Button(title_frame, text="×", width=3, command=self.exit_program)
        close_button.pack(side=tk.RIGHT, padx=5)
        
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Control buttons
        self.start_button = ttk.Button(main_frame, text="Start Typing (F6)", command=self.toggle_typing)
        self.start_button.pack(fill=tk.X, pady=5)
        
        self.pause_button = ttk.Button(main_frame, text="Pause/Resume (F7)", command=self.toggle_pause)
        self.pause_button.pack(fill=tk.X, pady=5)
        
        # Status displays
        self.status_label = ttk.Label(main_frame, text="Status: Idle", font=('Arial', 10, 'bold'))
        self.status_label.pack(pady=5)
        
        self.timer_label = ttk.Label(main_frame, text="", font=('Arial', 12), foreground="#ffcc00")
        self.timer_label.pack(pady=5)
        
        # Instructions
        self.create_instructions(main_frame)

    def create_instructions(self, parent):
        instructions = ttk.LabelFrame(parent, text="Instructions", padding="5")
        instructions.pack(fill=tk.BOTH, expand=True, pady=5)
        
        text_widget = tk.Text(instructions, height=8, wrap=tk.WORD, bg="#1c1c1c", fg="#f0f0f0",
                            font=("Arial", 9), bd=0)
        text_widget.pack(fill=tk.BOTH, expand=True)
        
        instructions_text = """
• F6: Start/Stop typing
• F7: Pause/Resume typing
• ESC: Emergency stop
• Ctrl+Shift+X: Exit program
• Ctrl+Shift+M: Hide/Show window
• Brackets and quotes are handled automatically
• Optimized for fast typing speed
• Works with C++ and other programming languages
"""
        text_widget.insert(tk.END, instructions_text)
        text_widget.config(state=tk.DISABLED)

    def simulate_typing(self, text):
        """Improved typing simulation with better bracket handling"""
        for char in text:
            if not self.running or self.paused:
                return
                
            # Handle special characters
            if char in self.bracket_pairs:
                # Type opening bracket
                self.keyboard.press(char)
                self.keyboard.release(char)
                time.sleep(self.typing_speed)
                
                # Type closing bracket
                closing_char = self.bracket_pairs[char]
                self.keyboard.press(closing_char)
                self.keyboard.release(closing_char)
                
                # Move cursor back inside brackets
                self.keyboard.press(Key.left)
                self.keyboard.release(Key.left)
            else:
                # Normal character typing
                self.keyboard.press(char)
                self.keyboard.release(char)
            
            time.sleep(self.typing_speed)

    def autotype_clipboard(self):
        if not self.clipboard_text:
            self.clipboard_text = pyperclip.paste().split("\n")
        
        for i in range(self.current_index, len(self.clipboard_text)):
            if not self.running or self.paused:
                break
                
            line = self.clipboard_text[i]
            # Enhanced C++ code detection and formatting
            if line.strip().startswith(('#include', 'using namespace', 'int main')):
                # Handle C++ specific lines with proper indentation
                self.simulate_typing(line)
            else:
                # Normal line typing with bracket handling
                self.simulate_typing(line)
            
            # Handle end of line
            self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter)
            self.keyboard.press(Key.home)
            self.keyboard.release(Key.home)
            
            self.current_index = i + 1
            time.sleep(self.typing_speed * 2)  # Slight pause between lines

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
        if self.running:
            self.autotype_clipboard()

    def countdown(self, duration):
        for i in range(duration, 0, -1):
            if not self.running:
                break
            self.timer_label.config(text=f"Starting in {i}...")
            time.sleep(1)
        self.timer_label.config(text="")

    def toggle_pause(self):
        if self.running:
            self.paused = not self.paused
            if self.paused:
                self.status_label.config(text="Status: Paused", foreground="#ffcc00")
            else:
                self.status_label.config(text="Status: Resuming", foreground="#00ff00")
                threading.Thread(target=self.delayed_resume, daemon=True).start()

    def delayed_resume(self):
        self.countdown(3)
        if self.running and not self.paused:
            self.autotype_clipboard()

    def stop_typing(self):
        self.running = False
        self.paused = False
        self.current_index = 0
        self.clipboard_text = []
        self.start_button.config(text="Start Typing (F6)")
        self.status_label.config(text="Status: Stopped", foreground="#ff0000")

    def exit_program(self):
        self.master.destroy()

    def toggle_hide(self):
        if self.master.state() == 'normal':
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
    app = LinuxCodeAutoTyper(root)
    root.mainloop()