import win32api, win32con
import time
from os import listdir

from tkinter import *   
from functools import partial

x_pad = 0
y_pad = 0

def projects():
    global b
    a=listdir()
    b=[]
    for i in a:
        j=i.split('.')
        if j[-1]=='txt':
            print(j[0])
            b+=[j[0]]

def project_contents(l,f_name_o):
    count=0
    print(f'Following is a list of clicks added in the project {f_name_o} :')
    print('-----------------------------------------------------------------')
    print('Position     Coordinates      Delay')
    print('-----------------------------------------------------------------')
    for i in l:
        i=i.split(',')
        j=i[2].split('\n')
        count+=1
        print(f'{count}            ({i[1]},{j[0]})           {i[0]}')
    print('-----------------------------------------------------------------')

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ("Click.")

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    global x
    global y
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (f'The recorded coordinates are {x},{y}')

while True:
    print('----------------------------------------')
    print('CHOICE    OPERATION')
    print('----------------------------------------')
    print('1         New Project')
    print('2         Edit an existing Project')
    print('3         Run an existing Project')
    print('4         Exit')
    print('----------------------------------------')
    c1=input('Enter your choice : ')
    print('----------------------------------------')
    flag1=0
    try:
        c1=int(c1)
    except:
        flag1=1
    if flag1==1:
        print('Enter a valid choice !!')
    elif c1==1:
        f_name=input('Enter the name of the project : ')
        print('----------------------------------------')
        f_name+='.txt'
        l=[]
        while True:
            print('----------------------------------------')
            print('CHOICE    OPERATION')
            print('----------------------------------------')
            print('1         Record a click')
            print('2         Stop and Save Project')
            print('----------------------------------------')
            c2=input('Enter your choice : ')
            print('----------------------------------------')
            flag2=0
            try:
                c2=int(c2)
            except:
                flag2=1
            if flag2==1:
                print('Enter a valid choice !!')
            elif c2==1:
                wait=input('Place your mouse at the position you want to record and press enter to record it')
                get_cords()
                try:
                    t=int(input('Enter the seconds of delay required before the click : '))
                except:
                    print('Enter a valid choice !!')
                print('-------------------------------------------------------------------------------------------------')
                c3=input(f'The mouse will click at ({x},{y}) after {t}. Enter 1 to save the click or 2 to discard : ')
                print('-------------------------------------------------------------------------------------------------')
                flag3=0
                try:
                    c3=int(c3)
                except:
                    flag3=1
                if flag3==1:
                    print('Enter a valid choice !!')
                elif c3==1:
                    l+=[str(t)+','+str(x)+','+str(y)+'\n']
                    print('Click added successfully !!')
                elif c3==2:
                    pass
                else:
                    print('Enter a valid choice !!')
            elif c2==2:
                break
            else:
                print('Enter a valid choice !!')
        f=open(f'{f_name}','a')
        f.writelines(l)
        f.close()

    elif c1==2:
        print('Following is a list of existing projects')
        print('-----------------------------------------------------------')
        projects()
        print('-----------------------------------------------------------')
        f_name=input('Enter the name of the project you want to edit : ')
        f_name_o=f_name
        if f_name in b:
            f_name+='.txt'
            f=open(f'{f_name}','r')
            l=f.readlines()
            f.close()
            while True:
                print('----------------------------------------')
                print('CHOICE    OPERATION')
                print('----------------------------------------')
                print('1         Add a click')
                print('2         Delete a click')
                print('3         Stop and Save Project')
                print('----------------------------------------')
                try:
                    c2=int(input('Enter your choice : '))
                    print('----------------------------------------')
                except:
                    print('Enter a valid choice !!')
        
                project_contents(l,f_name_o)

                if c2==1:
                    try:
                        n=int(input('Enter the position no. of the click : '))
                        if n!=1:
                            l+=[0]
                    except:
                        print('Enter a valid choice !!')
                    for i in range (len(l)):
                        nv=-1-i
                        if n==1:
                            break
                        l[nv]=l[nv-1]
                        if len(l)-i==n:
                            break
                    wait=input('Place your mouse at the position you want to record and press enter to record it')
                    get_cords()
                    try:
                        t=int(input('Enter the seconds of delay required before the click : '))
                    except:
                        print('Enter a valid choice !!')
                    try:
                        print('-------------------------------------------------------------------------------------------------')
                        c3=int(input(f'The mouse will click at ({x},{y}) after {t}. Enter 1 to save the click or 2 to discard : '))
                        print('-------------------------------------------------------------------------------------------------')
                    except:
                        print('Enter a valid choice !!')
                    if c3==1:
                        if n==1:
                            l=[str(t)+','+str(x)+','+str(y)+'\n']+l
                        else:
                            l[n-1]=str(t)+','+str(x)+','+str(y)+'\n'
                        f=open(f'{f_name}','w')
                        f.writelines(l)
                        f.close()
                        print('Click added successfully !!')
                    elif c3==2:
                        pass
                    else:
                        print('Enter a valid choice !!')
                
                elif c2==2:
                    f=open(f'{f_name}','r')
                    l=f.readlines()
                    f.close()
                    try:
                        delpos=int(input('Enter the position of click you want to delete : '))
                        del l[delpos-1]
                    except:
                        print('Enter a valid choice !!')
                    f=open(f'{f_name}','w')
                    f.writelines(l)
                    f.close()
                    print('Click deleted successfully')
                
                elif c2==3:
                    break
        else:
            print('Enter a valid name')           


    elif c1==3:
        print('Following is a list of existing projects')
        print('-----------------------------------------------------------')
        projects()
        print('-----------------------------------------------------------')
        f_name=input('Enter the name of the project you want to run : ')
        if f_name in b:
            f_name+='.txt'
            f=open(f'{f_name}','r')
            l=f.readlines()
            f.close()
            for i in l:
                j=i.split(',')
                print(j)
                y=j[2].split('\n')
                t=int(j[0])
                x=int(j[1])
                y=int(y[0])
                time.sleep(t)
                mousePos((x, y))
                leftClick()
        else:
            print('Enter a valid name')

    elif c1==4:
        print('Thanks for using the program')
        print('----------------------------------------')
        break
    else:
        print('Enter a valid choice !!')