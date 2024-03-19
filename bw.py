from PIL import Image
from pmas import pmas
with Image.open("hsv.jpg") as col:
    col.load()
with Image.open("bw.png") as bw:
    bw.load()
with Image.open("pic.jpeg") as pic:
    pic.load()

col = col.convert('RGB')
pic = pic.convert('RGB')
wcol, hcol = col.size
bw = bw.convert('RGB')
wbw, hbw = bw.size
wpic, hpic = pic.size
t = False
for wp in range(wpic):
    for hp in range(hpic):
        picpixel = pic.getpixel((wp, hp))
        if len(pmas[picpixel[0]][0]) != 0:
            id = pmas[picpixel[0]][2].index(max(pmas[picpixel[0]][2]))
            pic.putpixel((wp, hp), (pmas[picpixel[0]][0][id],
                                    pmas[picpixel[0]][1][id],
                                    pmas[picpixel[0]][2][id]))
        else:
            for w in range(wcol):
                for h in range(hcol):
                    if picpixel == bw.getpixel((w, h)):
                        color = col.getpixel((w, h))
                        pmas[picpixel[0]][0].append(color[0])
                        pmas[picpixel[0]][1].append(color[1])
                        pmas[picpixel[0]][2].append(color[2])
                        pic.putpixel((wp, hp), col.getpixel((w, h)))
                        t = True
                if t:
                    t = False
                else:
                    pmas[picpixel[0]].append(picpixel)
    print(int((wp/wpic)*100))
pic.show()
open("1.txt", "w").write(str(pmas))
