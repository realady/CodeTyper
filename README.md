# CodeTyper 🖥️

CodeTyper is a Python script that automatically types text copied to the clipboard with correct indentation. It is ideal for quickly typing out code snippets or other text without manual input.

## Features ✨

- Automatically types text copied to the clipboard
- Maintains correct indentation

## Prerequisites 🛠️

Before using CodeTyper, ensure you have the following dependencies installed:

- [Python 3.x](https://www.python.org/downloads/) 🐍
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/install.html) ⌨️
- [Pyperclip](https://pypi.org/project/pyperclip/) 📋
- [keyboard](https://keyboard.readthedocs.io/en/latest/) (for GUI version)

You can install the required Python packages using pip:

```bash
pip install pyautogui pyperclip keyboard
```

## Usage 🚀

### With GUI 🖥️

1. Clone the repository:

    ```bash
    git clone https://github.com/not-adarsh/CodeTyper
    ```

2. Navigate to the project directory:

    ```bash
    cd CodeTyper
    ```

3. Run the `main.py` script:

    ```bash
    python main.py
    ```

4. The GUI will open. Copy the text you want to type.

5. Use the GUI controls to start/stop typing, pause/resume, or hide/unhide the window.

**Keyboard Shortcuts:**

- `F6`: Start/Stop Typing
- `F7`: Pause/Resume Typing
- `Esc`: Stop Typing
- `Ctrl+Shift+X`: Exit Program
- `Ctrl+Shift+M`: Hide/Unhide the Program

### Without GUI 🚫

If you prefer not to use the graphical interface, you can use the non-GUI script:

```python
import pyperclip
import pyautogui
import time

def autotype_clipboard():
    time.sleep(2)  # Reduced delay before starting
    clipboard_text = pyperclip.paste().split("\n")

    for line in clipboard_text:
        pyautogui.write(line, interval=0.005)  # Reduced interval for faster typing
        for char in line:
            if char in ["[", '"', "'", "("]:
                pyautogui.press("delete")
        pyautogui.press("enter")
        pyautogui.press("home")

if __name__ == "__main__":
    autotype_clipboard()
```

1. Clone the repository:

    ```bash
    git clone https://github.com/not-adarsh/CodeTyper
    ```

2. Navigate to the project directory:

    ```bash
    cd CodeTyper
    ```

3. Run the `noGUImain.py` script:

    ```bash
    python noGUImain.py
    ```

4. Copy the text you want to type.

5. The program will automatically type the copied text with correct indentation.

## Credits 🙌

The original script was conceived and developed by our college seniors, who created the non-GUI version. Their work served as the foundation for this project. I built upon their efforts by developing a GUI to enhance usability and accessibility. Their pioneering contributions laid the groundwork for CodeTyper, and I am grateful for their support.

## Contributing 🤝

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
