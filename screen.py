import mss
import cv2
import pytesseract
import numpy as np

def get_screen_text():
    frame = capture_screen()
    screen_text = extract_text(frame)
    return screen_text

def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # 0 = all monitors, 1 = primary
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)  # raw image
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img

def extract_text(img):
    text = pytesseract.image_to_string(img)
    return text

# Example usage
# frame = capture_screen()
# screen_text = extract_text(frame)
# print(screen_text)
