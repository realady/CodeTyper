# CodeTyper 🖥️

CodeTyper is a Python script that automatically types the text copied to the clipboard with correct indentation. It is useful for quickly typing out code snippets or other text without having to manually type each character.

## Features ✨

- Automatically types text copied to the clipboard
- Maintains correct indentation


## Prerequisites 🛠️

Before using CodeTyper, ensure you have the following dependencies installed:

- [Python 3.x](https://www.python.org/downloads/) 🐍
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/install.html) ⌨️
- [Pyperclip](https://pypi.org/project/pyperclip/) 📋

You can install the required Python packages using pip:

```bash
pip install pyautogui pyperclip
```

## Usage 🚀

# ⚠️ DON'T INTERRUPT THE PROGRAM WHILE IT IS TYPING ⚠️

### With GUI 🖥️

1. Clone the repository:

    ```bash
    git clone https://github.com/not-adarsh/codingAutotyper
    ```

2. Navigate to the project directory:

    ```bash
    cd codingAutotyper
    ```

3. Run the `main.py` script:

    ```bash
    python main.py
    ```

4. Copy the text you want to type.

5. The program will automatically type the copied text with correct indentation.

### Without GUI 🚫

If you prefer not to use the graphical interface, you can use the following Python script:

```python
import pyperclip
import pyautogui
import time

def autotype_clipboard():
    time.sleep(5)
    clipboard_text = pyperclip.paste().split("\n")

    for line in clipboard_text:
        for char in line:
            pyautogui.write(char)
            if char in ["[", '"', "'", "("]:
                pyautogui.press("delete")
        
        pyautogui.press(["enter", "home"])

if __name__ == "__main__":
    autotype_clipboard()
```

1. Clone the repository:

    ```bash
    git clone https://github.com/not-adarsh/codingAutotyper
    ```

2. Navigate to the project directory:

    ```bash
    cd codingAutotyper
    ```

3. Run the `noGUImain.py` script:

    ```bash
    python noGUImain.py
    ```

3. Run the script.
   
4. Copy the text you want to type.

5. The program will automatically type the copied text with correct indentation.

## Credits 🙌

The original script was conceived and developed by our college seniors. They created the non-GUI version of the script, which served as the foundation for this project. I built upon their work by developing a wrapper GUI to enhance usability and accessibility. Their contribution laid the groundwork for the functionality of the Autotyper project, and I am grateful for their pioneering efforts.



## Contributing 🤝

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.


Feel free to adjust the content as needed.
``` 
Let me know if you need anything else! 👍
```
