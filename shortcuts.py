import pyautogui,time,keyboard, cv2
from PIL import Image
from PIL import ImageGrab
from pyscreeze import ImageNotFoundException

def arrow():
    #Para APA()
    for y in range(0, 3):
        pyautogui.hotkey("down")
def APA():
    print("Alt + Z ---> Formato APA")
    #Formato APA
    time.sleep(1)
    pyautogui.click(button='right')
    pyautogui.hotkey("ctrl", "e")
    pyautogui.hotkey("alt", "o")
    pyautogui.hotkey("alt", "f", "u")
    pyautogui.typewrite("Times New Roman")
    pyautogui.press("enter")
    pyautogui.hotkey("alt", "o")
    pyautogui.hotkey("alt", "t", "a")
    pyautogui.typewrite("12")
    pyautogui.press("enter")
    pyautogui.hotkey("alt", "o")
    pyautogui.hotkey("alt", "e", "s")
    arrow()
    pyautogui.press("enter")
def study():
    print("Alt + W ---> Work Environment")
    #Youtube y Slader
    time.sleep(1)
    pyautogui.hotkey("win", "1")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "t")
    time.sleep(1)
    pyautogui.moveTo(1767,500)
    pyautogui.click(button='right')
    pyautogui.hotkey("ctrl", "l")
    pyautogui.typewrite("www.youtube.com")
    pyautogui.press("enter")
    pyautogui.hotkey("ctrl", "t")
    pyautogui.typewrite("https://www.slader.com/textbook/9781111827069-differential-equations-with-boundary-value-problems-eighth-edition/")
    pyautogui.press("enter")
    #Libro de Cálculo
    time.sleep(1)
    pyautogui.press("win")
    pyautogui.typewrite("Ecuaciones")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "2")
def mousep():
    time.sleep(1)
    x = pyautogui.position()
    print(x)
def phisics():
    print("Alt + F ---> Physic Work")
    time.sleep(1)
    pyautogui.press("win")
    pyautogui.typewrite("SERWAY 7ma. Ed. VOL 2")
    try:
        s_cortana = pyautogui.locateOnScreen(r"<<Path to image>>")
        pyautogui.press("enter")
        time.sleep(1)
    except ImageNotFoundException:
            print("El libro no se encuentra...")
    pyautogui.press("win")
    pyautogui.typewrite("Raymond Serway, John Jewett - Physics for Scientists")
    try:
        s_cortana = pyautogui.locateCenterOnScreen(r"<<Path to image>>")
        pyautogui.press("enter")
    except ImageNotFoundException:
            print("No se encontró el Solucionario...")
def vb():    
    print("Alt + V ---> VirtualBox")
    try:
        s_desktop = pyautogui.locateOnScreen(r"<<Path to image>>", grayscale = True, confidence = .7)
        time.sleep(1)
        pyautogui.hotkey("win", "6")
        time.sleep(2)
    except ImageNotFoundException as imgne:
            print(imgne)
            print("No se pudo econtrar el ícono en la pantalla")
    try:
        s_vb1 = pyautogui.locateOnScreen(r"<<Path to image>>", grayscale = True, confidence= .7)
        s_vb2x, s_vb2y = pyautogui.locateCenterOnScreen(r"<<Path to image>>", grayscale = True, confidence= .7)
        pyautogui.click(s_vb2x, s_vb2y, button= "right")
    except ImageNotFoundException:
        print("Imagenes no encontradas en la pantalla") 
keyboard.add_hotkey('alt + z', lambda: APA())
keyboard.add_hotkey('alt + w', lambda: study())
keyboard.add_hotkey('alt + p', lambda: mousep())
keyboard.add_hotkey('alt + f', lambda: phisics())
keyboard.add_hotkey('alt + v', lambda: vb())
input('')
