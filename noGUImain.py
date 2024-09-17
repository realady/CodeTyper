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
