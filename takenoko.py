# coding: utf-8
import math
from mcpi.minecraft import Minecraft


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


def fun1(x,y,z):
    # pythonは戻り値にreturnが必要な模様
    #return x**2+y**2+z**2-1
    return 2*z+math.exp(-z-4)+math.exp(-8*z-48)-8+math.sqrt(1/8+math.pow(x,2)+math.pow(y,2)+2*math.pow(math.pow(x,2)+math.pow(y,2),2))-(1/(1+math.exp(-16*z-72)))*max(1/(1+math.exp(8*(z+x)))+1.0/(1+math.exp(8*(z+x+3)))+1/2,1/(1+math.exp(8*(z-x)))+1.0/(1+math.exp(8*(z-x+3)))) 

print("start")
mc = Minecraft.create()
grass=2
wool=35
print(fun1(0.1,0.2,0.3))
size=45
omin=-5
omax=5
step = ((omax-omin)*float(1)/size+omin)-((omax-omin)*float(0)/size+omin)
print("step = ")
print(step)
px, py, pz = mc.player.getPos()

for l in range(0,size):
    for m in range(0,size):
        for n in range(0,size):
            x = (omax-omin)*float(n)/size+omin
            y = (omax-omin)*float(m)/size+omin
            z = (omax-omin)*float(l)/size+omin
            #print('%e,%e,%e' % (x,y,z))
            p1=fun1(x,y,z)
            p2=fun1(x+step,y,z)
            p3=fun1(x-step,y,z)
            p4=fun1(x,y+step,z)	
            p5=fun1(x,y-step,z)
            p6=fun1(x,y,z+step)
            p7=fun1(x,y,z-step)
	    
            if ((not isFill(p2,p3,p4,p5,p6,p7)) and p1<=0):
                #print('%d,%d,%d' % (n,m,l))
                if z>-3:
                    mc.setBlock(px+n,py+l,pz+m,wool,15)
                else:
                    mc.setBlock(px+n,py+l,pz+m,wool,12)

mc.postToChat("Takenoko done!")                
print('end')
