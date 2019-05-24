from PIL import Image, ImageDraw
import turtle


width = 1920
height = 1920
colWht = (255,255,255)
colBlk = (0,0,0)

img = Image.new('RGB',(width,height), colWht)
drw = ImageDraw.Draw(img)

lineL = 5
width = 5
fill = 128

#Turn order vars
r = list('r')
l = list('l')

prevIt = r
newIt = prevIt

def inverse(strLs):
    arr = list(strLs)
    for i in range(0,len(arr)):
        if arr[i] == 'r':
            arr[i] = 'l'
        else:
            arr[i] = 'r'
    return arr

def drawFract(seq):
    for i in range(0,len(seq)):
        if seq[i] == 'r':
            turtle.right(90)
        else:
            turtle.left(90)
        turtle.forward(lineL)

order = int(input("Order of fractal: "))

for i in range(1 ,order):

    newIt = (prevIt) + (r)
    prevFlip = list(reversed(prevIt))
    prevFlip = inverse(prevFlip)

    newIt = (newIt) + (prevFlip)

    prevIt = newIt
print("Fractal Seq")
print(newIt)

turtle.ht()
turtle.setup(1000,1000)
turtle.speed(0)
turtle.color('black')
turtle.bgcolor('white')
turtle.forward(lineL)
drawFract(newIt)

pythImg = turtle.getscreen().getcanvas().postscript(file='outputname.eps')
img = Image.open('outputname' + '.eps')
img.save('dragFracts/outputname_'+str(order) + '.png', 'png')
img.show()








