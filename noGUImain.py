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