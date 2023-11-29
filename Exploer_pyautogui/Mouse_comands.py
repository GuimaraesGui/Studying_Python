import pyautogui
import pymsgbox

pymsgbox.alert('O programa mostra a posicição do mouse na tela.', 'Mouse_Position', 'Posição') #Cria uma msgbox com até três mensagens. (Mensagem, Titulo, Botao)

"""
> Right justify
str(x).rjust(width, fillchar)

str(x) = converte o objeto X para String.
.rjust(width, fillchar) = Insere valores a direita.
        width = Char que ficarão a direita.
        fillchar(opcional) = Preenche o espaço a esquerda  
"""

x, y = pyautogui.position()
positionStr = "X: " + str(x).rjust(4) + "Y: " + str(y).rjust(4)
print(positionStr)

"""
Segunda forma de imprimir a posição do cursor..

x, y = pyautogui.position()
##positionStr = "X: " + str(x).rjust(4) + "Y: " + str(y).rjust(4)
print("X: ", x, "Y: ", y)
"""

##pyautogui.moveTo(0,0, 0.5) #Desloca o cursor para um ponto específico (X, Y, Velocidade)