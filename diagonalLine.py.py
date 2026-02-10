from PIL import  Image,ImageDraw

img = Image.new('RGB',(100,100),'blue')
draw = ImageDraw.Draw(img)

aboveLine = [0] * 100
aboveLine[int(len(aboveLine)/2)] = 1

print(aboveLine)

# Create a checkboard first line
for j in range(100) :
    newLine = [0] * 100
    for i in range(1,50) :
        if (aboveLine[i-1] == 0 ) and  (aboveLine[i] == 0) and (aboveLine[i+1] == 1) or (aboveLine[i-1] == 1 ) and  (aboveLine[i] == 0) and (aboveLine[i+1] == 0) :
            # // draw black
            draw.point((i,j), fill='green')
            newLine[i] = 1
        else :
           # draw white
           draw.point((i,j), fill='blue')
           newLine[i] = 0
        # Here we rendering the currentLine
        
       # if aboveLine[i] % 2 == 0 :
       #     draw.point((i,j), fill='black')
       #     newLine[i] = 1
       # else :
       #     draw.point((i,j), fill='white')
       #     newLine[i] = 0
    for i in range(50,99) :
        if (aboveLine[i-1] == 1 ) and  (aboveLine[i] == 0) and (aboveLine[i+1] == 0) or (aboveLine[i-1] == 0 ) and  (aboveLine[i] == 0) and (aboveLine[i+1] == 1) :
            # // draw black
            draw.point((i,j), fill='green')
            newLine[i] = 1
        else :
           # draw white
           draw.point((i,j), fill='blue')
           newLine[i] = 0
        # Here we rendering the currentLine
        
       # if aboveLine[i] % 2 == 0 :
       #     draw.point((i,j), fill='black')
       #     newLine[i] = 1
       # else :
       #     draw.point((i,j), fill='white')
       #     newLine[i] = 0
    aboveLine = newLine
   
aboveLine = [0] * 100
aboveLine[50] = 1

print(aboveLine)
 #btm right
 
for j in range(1,50) :
    newLine = [0] * 100
    for i in range(50,99) :
        if (aboveLine[i-1] == 0 ) and  (aboveLine[i] == 0) and (aboveLine[i+1] == 1) or (aboveLine[i-1] == 1 ) and  (aboveLine[i] == 0) and (aboveLine[i+1] == 0) :
            # // draw black
            draw.point((i,j), fill='red')
            newLine[i] = 1
        else :
           # draw white
           draw.point((i,j), fill='yellow')
           newLine[i] = 0
        # Here we rendering the currentLine
        
       # if aboveLine[i] % 2 == 0 :
       #     draw.point((i,j), fill='black')
       #     newLine[i] = 1
       # else :
       #     draw.point((i,j), fill='white')
       #     newLine[i] = 0
    aboveLine = newLine   
aboveLine = [0] * 100
aboveLine[99] = 1

print(aboveLine)
 #btm left
for j in range(50,99) :
    newLine = [0] * 100
    for i in range(50,99) :
        if (aboveLine[i-1] == 1 ) and  (aboveLine[i] == 0) and (aboveLine[i+1] == 0) or (aboveLine[i-1] == 0 ) and  (aboveLine[i] == 0) and (aboveLine[i+1] == 1) :
            # // draw black
            draw.point((i,j), fill='red')
            newLine[i] = 1
        else :
           # draw white
           draw.point((i,j), fill='yellow')
           newLine[i] = 0
        # Here we rendering the currentLine
        
       # if aboveLine[i] % 2 == 0 :
       #     draw.point((i,j), fill='black')
       #     newLine[i] = 1
       # else :
       #     draw.point((i,j), fill='white')
       #     newLine[i] = 0
    aboveLine = newLine
    
img.show()