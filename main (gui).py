import win32api, win32con
import time
from os import listdir

from tkinter import *   

def get_cords():
    global x
    global y
    x,y = win32api.GetCursorPos()

def new_project():

    global f_name
    global l

    l=[]

    new_project=Toplevel()
    new_project.geometry("370x140")
    new_project.resizable(0,0)

    label=Label(new_project,text="Enter the name of the new project",font=('arial','16','bold')).pack(pady=10)

    f_name=Entry(new_project,width=20,font=('arial','14'))
    f_name.pack(ipady=2)

    button=Button(new_project,text="Create project",font=('arial','14','bold'),borderwidth=4,padx=25,command=lambda:[make_project(),new_project.destroy()]).pack(pady=10)

def make_project():

    global t
    global f_name

    make_project=Toplevel()
    make_project.geometry("600x300")
    make_project.resizable(0,0)

    label=Label(make_project,text="Input the seconds of delay required before the click.\nThen click on {Record click} button\nAfter clicking, place your mouse on the position\nyou want the bot to click at\nThe click will be recorded within 5 seconds of clicking the button",font=('arial','14')).pack(pady=5)

    label=Label(make_project,text="Delay :",font=('arial','16','bold')).pack()
    t=Entry(make_project,width=10,font=('arial','14'))
    t.pack(ipady=2)

    f_name=f_name.get()
    f_name=f_name+'.txt'

    button=Button(make_project,text="Record click",font=('arial','14','bold'),borderwidth=4,padx=25,command=record_click).pack(pady=8)
    button=Button(make_project,text="Close and save the project",font=('arial','14','bold'),borderwidth=4,padx=20,command=lambda:[make_project.destroy(),write_click()]).pack()

def record_click():

    global t
    global l

    t1=t.get()
    t.delete(0, "end")
    
    flag=0

    try:
        t2=int(t1)
        if t2<0:
            flag=1
    except:
        flag=1
    
    if flag==0:
        time.sleep(5)
        get_cords()
        l=l+[str(t1)+','+str(x)+','+str(y)+'\n']  
        record_click=Toplevel()    
        record_click.geometry("300x90")
        record_click.resizable(0,0)
        label=Label(record_click,text="Click added successfully !!",font=('arial','16','bold')).pack(pady=4)
    else:
        record_click=Toplevel()    
        record_click.geometry("300x90")
        record_click.resizable(0,0)
        label=Label(record_click,text="Enter a valid value for time !!",font=('arial','16','bold')).pack(pady=4)

    button=Button(record_click,text="Close window",font=('arial','14','bold'),borderwidth=4,padx=30,command=record_click.destroy).pack()

def write_click():

    global f_name
    global l

    f=open(f'{f_name}','a')
    f.writelines(l)
    f.close()

    write_click=Toplevel()    
    write_click.geometry("320x90")
    write_click.resizable(0,0)
    
    label=Label(write_click,text="Project created successfully !!",font=('arial','16','bold')).pack(pady=4)

    button=Button(write_click,text="Close window",font=('arial','14','bold'),borderwidth=4,padx=30,command=write_click.destroy).pack()

def projects():

    global b
    
    a=listdir()
    b=[]

    for i in a:
        j=i.split('.')
        if j[-1]=='txt':
            b+=[j[0]]

def edit_project():

    global f_name

    f_name=''

    projects()

    edit_project=Toplevel()
    edit_project.geometry(f"400x{(len(b)+1)*50}")
    edit_project.resizable(0,0)
    label=Label(edit_project,text="Choose the project you want to edit",font=('arial','16','bold')).pack(pady=4)

    count=0
    for f_name in b:
        count+=1
        if count%2==0:
            spacing=0
        else:
            spacing=4
        button=Button(edit_project,text=f'{f_name}',font=('arial','14','bold'),borderwidth=4,padx=25,command=lambda:[edit_clickss(),edit_project.destroy()]).pack(pady=spacing)

def edit_clickss():

    global f_name
    global contents
    global edit_clicks

    test=f_name.split('.')
    
    if test[-1]!='txt':
        f_name+='.txt'
    
    contents=[] 
    count=0

    f=open(f'{f_name}','r')
    contents=f.readlines()
    f.close()

    edit_clicks=Toplevel()
    edit_clicks.geometry(f"330x{215+(len(contents)*35)}")
    edit_clicks.resizable(0,0)

    label=Label(edit_clicks,text=f"Following is the list of clicks\nalready added in the file\n[{f_name}] :",font=('arial','16','bold')).pack(pady=4)    
    label=Label(edit_clicks,text='Position%5sCoordinates    Delay',font=('arial','16','bold')).pack()

    for i in contents:

        count+=1

        if count%2==0:
            spacing=0
        else:
            spacing=4

        j=i.split(',')
        k=j[-1].split('\n')

        label=Label(edit_clicks,text=f'{count}            ({j[1]},{k[0]})              {j[0]}',font=('arial','14')).pack(pady=2)

    spacing_add=0
    spacing_delete=0
    if count%2==0:
        spacing_add=4
    else:
        spacing_add=2
        spacing_delete=2

    button=Button(edit_clicks,text="Add a click",font=('arial','14','bold'),borderwidth=4,padx=25,command=add_click).pack(pady=spacing_add)
    button=Button(edit_clicks,text="Delete a click",font=('arial','14','bold'),borderwidth=4,padx=27,command=delete_click).pack(pady=spacing_delete)

def add_click():

    global t
    global p
    global edit_clicks

    add_click=Toplevel()
    add_click.geometry("560x380")
    add_click.resizable(0,0)

    label=Label(add_click,text="Input the seconds of delay required before the click\nand the position you want the click to be added at\nThen click on {Record click} button\nAfter clicking, place your mouse on the position\nyou want the bot to click at\nThe click will be recorded within 5 seconds of clicking the button",font=('arial','14')).pack(pady=5)

    label=Label(add_click,text="Delay :",font=('arial','16','bold')).pack()
    t=Entry(add_click,width=10,font=('arial','14'))
    t.pack(ipady=2)

    label=Label(add_click,text="Position :",font=('arial','16','bold')).pack()
    p=Entry(add_click,width=10,font=('arial','14'))
    p.pack(ipady=2)

    button=Button(add_click,text="Record click",font=('arial','14','bold'),borderwidth=4,padx=25,command=lambda:[record_added_click(),edit_clicks.destroy(),edit_clickss()]).pack(pady=4)
    button=Button(add_click,text="CLose window",font=('arial','14','bold'),borderwidth=4,padx=25,command=add_click.destroy).pack()

def record_added_click():

    global t
    global p
    global contents
    global f_name

    t1=t.get()
    t.delete(0, "end")

    p1=p.get()
    p.delete(0, "end")

    flag=0

    try:
        t2=int(t1)
        if t2<0:
            flag=1
    except:
        flag=1
    
    try:
        p2=int(p1)
        if p2<0:
            flag=1
    except:
        flag=2

    if flag==0:
        time.sleep(5)
        get_cords()

        if int(p1)==1:
            contents=[str(t1)+','+str(x)+','+str(y)+'\n']+contents
        else:
            contents+=[0]
            for i in range (len(contents)):
                nv=-1-i
                contents[nv]=contents[nv-1]
                if len(contents)-i==int(p1):
                    break
            contents[int(p1)-1]=str(t1)+','+str(x)+','+str(y)+'\n'
        
        record_added_click=Toplevel()    
        record_added_click.geometry("300x90")
        record_added_click.resizable(0,0)
        label=Label(record_added_click,text="Click added successfully !!",font=('arial','16','bold')).pack(pady=4)

        f=open(f'{f_name}','w')
        f.writelines(contents)
        f.close()

    elif flag==1:
        record_added_click=Toplevel()    
        record_added_click.geometry("300x90")
        record_added_click.resizable(0,0)
        label=Label(record_added_click,text="Enter a valid value for time !!",font=('arial','16','bold')).pack(pady=4)

    elif flag==2:
        record_added_click=Toplevel()    
        record_added_click.geometry("340x90")
        record_added_click.resizable(0,0)
        label=Label(record_added_click,text="Enter a valid value for position !!",font=('arial','16','bold')).pack(pady=4)

    button=Button(record_added_click,text="Close window",font=('arial','14','bold'),borderwidth=4,padx=30,command=record_added_click.destroy).pack()

def delete_click():

    global p
    global edit_clicks

    delete_click=Toplevel()
    delete_click.geometry("400x180")
    delete_click.resizable(0,0)

    label=Label(delete_click, text="Input the position of click\nyou want to delete",font=('arial','16')).pack()    

    label=Label(delete_click,text="Position :",font=('arial','16','bold')).pack()
    p=Entry(delete_click,width=10,font=('arial','14'))
    p.pack(ipady=2)

    button=Button(delete_click,text="Delete click",font=('arial','14','bold'),borderwidth=4,padx=25,command=lambda:[deleting_click(),edit_clicks.destroy(),edit_clickss()]).pack(pady=6)

def deleting_click():

    global f_name
    global contents

    p1=p.get()
    p.delete(0, "end")

    flag=0
    
    try:
        p2=int(p1)
    except:
        flag=1

    if flag==0:

        del contents[p2-1]

        f=open(f'{f_name}','w')
        f.writelines(contents)
        f.close()

        deleting_click=Toplevel()    
        deleting_click.geometry("300x90")
        deleting_click.resizable(0,0)
        label=Label(deleting_click,text="Click deleted successfully !!",font=('arial','16','bold')).pack(pady=4)

    elif flag==1:
        deleting_click=Toplevel()    
        deleting_click.geometry("340x90")
        deleting_click.resizable(0,0)
        label=Label(deleting_click,text="Enter a valid value for position !!",font=('arial','16','bold')).pack(pady=4)

    button=Button(deleting_click,text="Close window",font=('arial','14','bold'),borderwidth=4,padx=30,command=deleting_click.destroy).pack()

def run_project():

    global f_name

    f_name=''

    projects()

    run_project=Toplevel()
    run_project.geometry(f"400x{(len(b)+1)*50}")
    run_project.resizable(0,0)

    label=Label(run_project,text="Choose the project you want to edit",font=('arial','16','bold')).pack(pady=4)

    count=0
    for f_name in b:
        count+=1
        if count%2==0:
            spacing=0
        else:
            spacing=4

        button=Button(run_project,text=f'{f_name}',font=('arial','14','bold'),borderwidth=4,padx=25,command=lambda:[running_project(),run_project.destroy()]).pack(pady=spacing)

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def mousePos(cord):
    win32api.SetCursorPos((cord[0], cord[1]))

def running_project():

    global f_name

    f_name+='.txt'
    f=open(f'{f_name}','r')
    l=f.readlines()
    f.close()
    for i in l:
        j=i.split(',')
        y=j[2].split('\n')
        t=int(j[0])
        x=int(j[1])
        y=int(y[0])
        time.sleep(t)
        mousePos((x, y))
        leftClick()

main_menu = Tk()
main_menu.resizable(0,0)
main_menu.geometry("240x290")
main_menu.title("")

label=Label(main_menu, text="Auto Clicker",font=('arial','20','bold','underline')).pack(pady=10)

button=Button(main_menu,text="Create Project",font=('arial','14','bold'),borderwidth=5,padx=0,command=new_project).pack(pady=0)
button=Button(main_menu,text="Edit Project",font=('arial','14','bold'),borderwidth=5,padx=13,command=edit_project).pack(pady=10)
button=Button(main_menu,text="Run Project",font=('arial','14','bold'),borderwidth=5,padx=13,command=run_project).pack(pady=0)
button=Button(main_menu,text="Close window",font=('arial','14','bold'),borderwidth=5,padx=3,command=main_menu.destroy).pack(pady=10)

main_menu.mainloop()