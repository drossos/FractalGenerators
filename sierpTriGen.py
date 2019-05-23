from PIL import Image, ImageDraw

width = 1920
height = 1080
colWht = (255,255,255)
colBlk = (0,0,0)

img = Image.new('RGB',(1920,1080), colWht)
drw = ImageDraw.Draw(img)

step = 3
#init points
p1,p2,p3 = [20,height-20], [width/2, 20],[width-20,height-20]



#drw.polygon([(p1[0],p1[1]), (p2[0],p2[1]), (p3[0],p3[1])], fill=colWht)


#Takes in 3 points each with (x,y) components and colour
#Is called resursively
def drawTri(p1,p2,p3, col,step):
    if (step != 0):
        col = colWht
    else:
        col = colBlk

    drw.polygon([(p1[0],p1[1]), (p2[0],p2[1]), (p3[0],p3[1])], fill=col)

    step -= 1

    if (step >= 0):
        drawTri(p1, midPt(p1,p2) , midPt(p1,p3), col, step)
        drawTri(midPt(p1,p2), p2 , midPt(p2,p3), col, step)
        drawTri(midPt(p3,p2), midPt(p1,p3), p3, col, step)
    if (step < 0):
        return 0




def midPt(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2) #find midpoint


#degree of the fractal
step = 10
drawTri((p1[0],p1[1]), (p2[0],p2[1]), (p3[0],p3[1]),colWht, step)

#shows the image in new window
#can also enable so image saves in directory 
img.show()