import pyautogui, sys
import pymsgbox

pymsgbox.confirm('Deseja rodar o programa?', 'mouse_position',['Sim_TEXT', 'Não_TEXT'], )

try:
    while True:
        x, y = pyautogui.position()
        position = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(position, end='')
        print('\b'*len(position), end='')
except: KeyboardInterrupt
print('\n')