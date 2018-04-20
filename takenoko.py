# coding: utf-8

import tkinter
import math
import ast
from mcpi.minecraft import Minecraft
from mcpi import block


takenoko=True

def preset1():
    global takenoko
    takenoko=True
    t.delete('1.0',tkinter.END)
    t.insert('1.0',"2*z+math.exp(-z-4)+math.exp(-8*z-48)-8+math.sqrt(1/8+math.pow(x,2)+math.pow(y,2)+2*math.pow(math.pow(x,2)+math.pow(y,2),2))-(1/(1+math.exp(-16*z-72)))*max(1/(1+math.exp(8*(z+x)))+1.0/(1+math.exp(8*(z+x+3)))+1/2,1/(1+math.exp(8*(z-x)))+1.0/(1+math.exp(8*(z-x+3))))")

    entry1.delete(0, tkinter.END)
    entry1.insert(0,"-5")
    entry2.delete(0,tkinter.END)
    entry2.insert(0,"5")

    entry3.delete(0,tkinter.END)
    entry3.insert(0,"-5")
    entry4.delete(0,tkinter.END)
    entry4.insert(0,"5")

    entry5.delete(0,tkinter.END)
    entry5.insert(0,"-5")
    entry6.delete(0,tkinter.END)
    entry6.insert(0,"5")

def preset2():
    global takenoko
    takenoko=False
    print(takenoko)
    t.delete('1.0',tkinter.END)
    t.insert('1.0',"x**2+y**2+z**2-1")

    entry1.delete(0, tkinter.END)
    entry1.insert(0,"-1")
    entry2.delete(0,tkinter.END)
    entry2.insert(0,"1")

    entry3.delete(0,tkinter.END)
    entry3.insert(0,"-1")
    entry4.delete(0,tkinter.END)
    entry4.insert(0,"1")

    entry5.delete(0,tkinter.END)
    entry5.insert(0,"-1")
    entry6.delete(0,tkinter.END)
    entry6.insert(0,"1")

def preset3():
    global takenoko
    takenoko=False
    t.delete('1.0',tkinter.END)
    t.insert('1.0',"x**2*y**2+y**2*z**2+z**2*x**2+x*y*z")

    entry1.delete(0, tkinter.END)
    entry1.insert(0,"-0.5")
    entry2.delete(0,tkinter.END)
    entry2.insert(0,"0.5")

    entry3.delete(0,tkinter.END)
    entry3.insert(0,"-0.5")
    entry4.delete(0,tkinter.END)
    entry4.insert(0,"0.5")

    entry5.delete(0,tkinter.END)
    entry5.insert(0,"-0.5")
    entry6.delete(0,tkinter.END)
    entry6.insert(0,"0.5")

def cancelFunc():
    root.quit()

def isFill(pt1,pt2,pt3,pt4,pt5,pt6):
    if pt1 > 0:
        return False

    if pt2 > 0:
        return False

    if pt3 > 0:
        return False
	
    if pt4 > 0:
        return False

    if pt5 > 0:
        return False

    if pt6 > 0:
        return False

    return True

def myfunc1():
    formula = t.get('1.0','end')

    try:
        tree = ast.parse("def func1(x,y,z): "+"  return "+formula,mode='exec')
    
    except (RuntimeError, TypeError, NameError, SyntaxError):
        return
    
    valid = all(isinstance(node, whitelist) for node in ast.walk(tree))
    if valid:
        xmin = float(entry1.get())
        xmax = float(entry2.get())
        ymin = float(entry3.get())
        ymax = float(entry4.get())
        zmin = float(entry5.get())
        zmax = float(entry6.get())

        size=45
        
        xstep = ((xmax-xmin)*float(1)/size+xmin)-((xmax-xmin)*float(0)/size+xmin)
        ystep = ((ymax-ymin)*float(1)/size+ymin)-((ymax-ymin)*float(0)/size+ymin)
        zstep = ((zmax-zmin)*float(1)/size+zmin)-((zmax-zmin)*float(0)/size+zmin)
        #print('%f,%f,%f' % (xstep,ystep,zstep))
        binFormula = compile(tree, filename='', mode='exec')
        exec(binFormula,globals())
        px, py, pz = mc.player.getPos()

        for l in range(0,size):
            for m in range(0,size):
                for n in range(0,size):
                    x = (xmax-xmin)*float(n)/size+xmin
                    y = (ymax-ymin)*float(m)/size+ymin
                    z = (zmax-zmin)*float(l)/size+zmin
                    p1=func1(x,y,z)
                    p2=func1(x+xstep,y,z)
                    p3=func1(x-xstep,y,z)
                    p4=func1(x,y+ystep,z)	
                    p5=func1(x,y-ystep,z)
                    p6=func1(x,y,z+zstep)
                    p7=func1(x,y,z-zstep)
	    
                    if ((not isFill(p2,p3,p4,p5,p6,p7)) and p1<=0):
                        print('%d,%d,%d,%s' % (n,m,l,takenoko))
                        if (takenoko):
                            if z>-3: 
                                mc.setBlock(px+n,py+l,pz+m,wool,15)
                            else:
                                mc.setBlock(px+n,py+l,pz+m,wool,12)
                        else:
                            print("takenoko=false")
                            mc.setBlock(px+n,py+l,pz+m,block.DIAMOND_BLOCK)

host="localhost"
mc = Minecraft.create(host)
wool=35

takenoko=True

root = tkinter.Tk()
root.title("done")

topFrame = tkinter.Frame(root)
bottomFrame = tkinter.Frame(root)
topFrame.pack()
bottomFrame.pack(side=tkinter.BOTTOM,fill=tkinter.X)

t = tkinter.Text(topFrame, height=5, width=90)
t.insert(tkinter.END, "2*z+math.exp(-z-4)+math.exp(-8*z-48)-8+math.sqrt(1/8+math.pow(x,2)+math.pow(y,2)+2*math.pow(math.pow(x,2)+math.pow(y,2),2))-(1/(1+math.exp(-16*z-72)))*max(1/(1+math.exp(8*(z+x)))+1.0/(1+math.exp(8*(z+x+3)))+1/2,1/(1+math.exp(8*(z-x)))+1.0/(1+math.exp(8*(z-x+3))))")

label1 = tkinter.Label(topFrame, text="formula")
label1.pack(side=tkinter.LEFT)
t.pack(side=tkinter.RIGHT)

entry1=tkinter.Entry(bottomFrame)
entry1.insert(tkinter.END,"-5.0")
entry2=tkinter.Entry(bottomFrame)
entry2.insert(tkinter.END,"5.0")

entry3=tkinter.Entry(bottomFrame)
entry3.insert(tkinter.END,"-5.0")
entry4=tkinter.Entry(bottomFrame)
entry4.insert(tkinter.END,"5.0")

entry5=tkinter.Entry(bottomFrame)
entry5.insert(tkinter.END,"-5.0")
entry6=tkinter.Entry(bottomFrame)
entry6.insert(tkinter.END,"5.0")

label2 = tkinter.Label(bottomFrame, text="xmin")
label3 = tkinter.Label(bottomFrame, text="xmax")
label4 = tkinter.Label(bottomFrame, text="ymin")
label5 = tkinter.Label(bottomFrame, text="ymax")
label6 = tkinter.Label(bottomFrame, text="zmin")
label7 = tkinter.Label(bottomFrame, text="zmax")

label2.grid(row=0)
label3.grid(row=0,column=2)

label4.grid(row=1)
label5.grid(row=1,column=2)

label6.grid(row=2)
label7.grid(row=2,column=2)

entry1.grid(row=0,column=1)
entry2.grid(row=0,column=3)

entry3.grid(row=1,column=1)
entry4.grid(row=1,column=3)

entry5.grid(row=2,column=1)
entry6.grid(row=2,column=3)

whitelist = (ast.Expression, ast.Call, ast.Name, ast.Load,
             ast.BinOp, ast.UnaryOp, ast.operator, ast.unaryop, ast.cmpop,
             ast.Num,ast.Add,ast.Sub,ast.Mult,ast.Div,ast.Attribute,
             ast.Module,ast.FunctionDef,ast.arguments,ast.Return,ast.arg
            )

pbtn1 = tkinter.Button(bottomFrame, text="preset 1",
    command=preset1)
pbtn2 = tkinter.Button(bottomFrame, text="preset 2",
    command=preset2)
pbtn3 = tkinter.Button(bottomFrame, text="preset 3",
    command=preset3)

pbtn1.grid(row=3,column=0)
pbtn2.grid(row=3,column=1)
pbtn3.grid(row=3,column=2)

button1=tkinter.Button(bottomFrame,text="Plot",
    command=myfunc1)
button2=tkinter.Button(bottomFrame,text="Quit",
    command=cancelFunc)

button1.grid(row=5,column=4)
button2.grid(row=5,column=5)

root.geometry("700x200")

root.mainloop()
