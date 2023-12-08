import tkinter as tk
from tkinter import *
import os,time,re
import pyautogui
import numpy 
import sounddevice as sd
import subprocess
import keyboard
root = tk.Tk()
#Window settings
root.title("AUTOTRK")
#Window settings-(f"{int(root.winfo_screenwidth())}x{int(root.winfo_screenheight())}" give me the exact size of the screen)
window_h= int(root.winfo_screenheight())
window_w= int(root.winfo_screenmmwidth())
root.geometry(f"{int(60/100*int(root.winfo_screenwidth()))}x{int(50/100*root.winfo_screenheight())}")
root.config(bg="lightblue")
#create new file button
#the new file function apparition
def new_file_entry():
    if new_file_name.winfo_ismapped():
        new_file_name.place_forget()
        new_file_name_button.place_forget()
        dlt_file_name_button.place_forget()
        scroll_bar.place_forget()
        scroll_bar_content.place_forget()
    else:
        new_file_name.place(y=int(4/100*window_h),x=0,width=int(10/100*window_w),height=int(2/100*window_h))
        dlt_file_name_button.place(y=int(4/100*window_h),x=int(10/100*window_w),width=int(5/100*window_w),height=int(2/100*window_h))
        new_file_name_button.place(y=int(4/100*window_h),x=int(15/100*window_w),width=int(5/100*window_w),height=int(2/100*window_h))
        scroll_bar.place(x=int(15/100*window_w),y=int(6/100*window_h),width=int(5/100*window_w),height=int(10/100*window_h))
        scroll_bar_content.place(x=0,y=int(6/100*window_h),height=int(10/100*window_h),width=int(15/100*window_w))
#function for building the file
def add_file():
#this part of the function checks for an element on scrol_bar_content
    if new_file_name.get() in scroll_bar_content.get(0,tk.END):
         return -1
    scroll_bar_content.insert(END,new_file_name.get())
    file_name = new_file_name.get()
#this part of the function is creating the file and writing on it #NEWFILE w+ represents the write+ access to the file
    file = os.path.join(f"{os.path.dirname(os.path.abspath(__file__))}/prjfiles/{file_name}.py")
    with open(file,"w+") as f:
        f.write("import pyautogui,time,keyboard \n")
        for i in range(1,5):f.write("\n")

#this function deletes a specific file
def dlt_file():
    file_name = new_file_name.get()
    content = scroll_bar_content.get(0, tk.END)

    if file_name in content:
#remove the file from the prjfiles dir
        os.remove(f"{os.path.dirname(os.path.abspath(__file__))}/prjfiles/{file_name}.py")

#remove the file name from the ListBox
        index = content.index(file_name)
        scroll_bar_content.delete(index)

#scroll bar setings(it is just to help you what files you have on the prj folder)
scroll_bar = Scrollbar(root)
scroll_bar_content =Listbox(root,yscrollcommand=scroll_bar.set)
for x in os.listdir(f"{os.path.dirname(os.path.abspath(__file__))}/prjfiles"):
    scroll_bar_content.insert(END,x.replace(".py",""))

file_add_btn = tk.Button(root,background="grey",relief="solid",text="new file",command=new_file_entry,borderwidth=1)
file_add_btn_width,file_add_btn_height=int(20/100*window_w),int(4/100*window_h)
file_add_btn.place(width=file_add_btn_width,height=file_add_btn_height,x=0,y=0)
new_file_name=tk.Entry(root)
new_file_name_button=tk.Button(root,text="=>",command=add_file)
dlt_file_name_button=tk.Button(root,text="=X",command=dlt_file)
#the mouse cords button
#this function makes a sound 
def beep():
    frecvence,duration,rate=500,1.0,44100
    t = numpy.linspace(0, duration, int(rate * duration), endpoint=False)
    signal = 0.5 * numpy.sin(2.0 * numpy.pi * frecvence * t)

    sd.play(signal, samplerate=rate)
    sd.wait()
#this function makes the settings of the configuration appear
def cords_info():
    if cords_location.winfo_ismapped():
        cords_location.place_forget()
        cords_time.place_forget()
        find_cords_button.place_forget()
    else:
        cords_location.place(x=file_add_btn_width,height=int(2/100*window_h),y=int(4/100*window_h),width=int(12/100*window_w))
        cords_time.place(x=file_add_btn_width+int(12/100*window_w),height=int(2/100*window_h),y=int(4/100*window_h),width=int(4/100*window_w))
        find_cords_button.place(x=file_add_btn_width+int(16/100*window_w),height=int(2/100*window_h),y=int(4/100*window_h),width=int(4/100*window_w))
#this function is finding the cords
def find_cords():
    time.sleep(int(cords_time.get()))
    beep()
    x, y = pyautogui.position() 
    cords_location.delete(0,tk.END)
    cords_location.insert(0,f"x={x} y={y}")  

cords_button=tk.Button(root,background="grey",relief="solid",borderwidth=1,text="cords",command=cords_info)
cords_button.place(x=file_add_btn_width,height=file_add_btn_height,width=file_add_btn_width,y=0)
cords_location=tk.Entry(root,background="white")
cords_time=tk.Entry(root)
find_cords_button = tk.Button(root,text="=>",command=find_cords,background="white",relief="solid")
#run file 
def run_file_info():
    if select_run_file.winfo_ismapped():
        select_run_file.place_forget()
        select_run_buttom.place_forget()
    else:
        select_run_file.place(x=2*file_add_btn_width,height=int(2/100*window_h),y=int(4/100*window_h),width=int(17/100*window_w))
        select_run_buttom.place(x=2*file_add_btn_width+int(17/100*window_w),height=int(2/100*window_h),y=int(4/100*window_h),width=int(3/100*window_w))
#this function is running the file that you edit
def run_file():
    subprocess.run(["python3",f"{os.path.dirname(os.path.abspath(__file__))}prjfiles/{select_run_file.get()}.py"])
run_button = tk.Button(root,text = "run",command=run_file_info,background="grey",relief="solid",borderwidth=1)
run_button.place(x=2*file_add_btn_width,height=file_add_btn_height,width=file_add_btn_width,y=0)
select_run_file=tk.Entry(root,relief="solid",background="white")
select_run_buttom= tk.Button(root,relief="solid",background="white",text=">",command=run_file)
#select the file 
def open_file_info():
    if select_open_file.winfo_ismapped():
        select_open_button.place_forget()
        select_open_file.place_forget()
    else:
        select_open_file.place(x=3*file_add_btn_width,height=int(2/100*window_h),y=int(4/100*window_h),width=int(17/100*window_w))
        select_open_button.place(x=3*file_add_btn_width+int(17/100*window_w),height=int(2/100*window_h),y=int(4/100*window_h),width=int(3/100*window_w))
def part(line):
    right_click = rf'{re.escape(" pyautogui.rightClick(")}\s*(\S+)'
    left_click = rf'{re.escape(" pyautogui.click(")}\s*(\S+)'
    sleep_loc = rf'{re.escape(" time.sleep(")}\s*(\S+)'
    write_loc = rf'{re.escape(" pyautogui.write(")}\s*(\S+)'
    cords_loc = rf'{re.escape(" pyautogui.moveTo(")}\s*(\S+)\s*,\s*(\S+)\s*\)'

    hotkey_pattern = re.compile(re.escape("pyautogui.hotkey(['") + r'([^\]]+)\s*]\s*\)')

    if re.search(right_click, line):
        return str(f"right click")
    elif re.search(left_click, line):
        return str(f"left click")
    elif re.search(sleep_loc, line):
        return str(f"sleep {re.search(sleep_loc, line).group(1)} sec")
    elif re.search(write_loc, line):
        return str(f"write {re.search(write_loc, line).group(1)}")
    elif re.search(cords_loc, line):
        cords_unpack = re.search(cords_loc, line)
        x_cords, y_cords = cords_unpack.group(1), cords_unpack.group(2)
        return str(f"the cords are {x_cords} {y_cords}")
    elif (hotkey_match := hotkey_pattern.search(line)):
        keys = hotkey_match.group(1).replace("'", "").split(', ')
        return f"You pressed keys: {', '.join(keys)}"
    else:
        return None

def open_it():
    global path, i,line
    path = f"{os.path.dirname(os.path.abspath(__file__))}/prjfiles/{select_open_file.get()}.py"
    i = 5
    with open(path, 'r') as file:
        lines = file.readlines()
        scroll_bar_file_content.delete(0, tk.END)  # Clear the existing content
        for line in lines:
           scroll_bar_file_content.insert(tk.END, part(line))
#            scroll_bar_file_content.insert(tk.END, str(line))
open_file = tk.Button(root,relief="solid",background="grey",borderwidth=1,command=open_file_info,text="open")
open_file.place(x=3*file_add_btn_width,height=int(4/100*window_h),y=0,width=int(20/100*window_w))
select_open_file = tk.Entry(root)
select_open_button = tk.Button(root,text=">",command=open_it)
#content box
scroll_bar_file = Scrollbar(root)
scroll_bar_file.place(x=59/100*int(root.winfo_screenwidth()),width=1/100*int(root.winfo_screenwidth()),height=int(50/100*window_h))
scroll_bar_file_content=Listbox(root,yscrollcommand=scroll_bar_file)
scroll_bar_file_content.place(x=21/100*int(root.winfo_screenwidth()),width=38/100*int(root.winfo_screenwidth()),height=50/100*int(root.winfo_screenheight()))
#file functions add
#cursor move function
#this function builds the script 
def cursor_muve_function():
    global i,path
#read the number of lines
    with open(path , 'r') as file:
        lines = file.readlines()
#    while len(lines) < 5:
#building the space for the loop settings
#     lines.append('\n')
    lines[len(lines)-1]= f" pyautogui.moveTo(x={(click_setings_X.get())}, y={click_setings_Y.get()}) \n"
    i+=1
    lines.append('\n')
#apply 
    with open(path , 'w+') as file:
        file.writelines(lines)
click_setings_X_inf= tk.Label(root,relief="flat",background="lightblue",text="x=")
click_setings_X_inf.place(y=int(16/100*int(root.winfo_screenheight())),width=1/100*int(root.winfo_screenwidth()),x=0,height=int(2/100*int(root.winfo_screenheight())))
click_setings_X = tk.Entry(root,relief="solid")
click_setings_X.place(x=1/100*int(root.winfo_screenwidth()),width=2/100*int(root.winfo_screenwidth()),height=int(2/100*int(root.winfo_screenheight())),y=int(16/100*int(root.winfo_screenheight())))
click_setings_Y_inf = tk.Label(root,relief="flat",background="lightblue",text="y=")
click_setings_Y_inf.place(x=3/100*int(root.winfo_screenwidth()),width=1/100*int(root.winfo_screenwidth()),y=15.8/100*int(root.winfo_screenheight()),height=2/100*int(root.winfo_screenheight()))
click_setings_Y = tk.Entry(root,relief="solid")
click_setings_Y.place(x=4/100*int(root.winfo_screenwidth()),width=2/100*int(root.winfo_screenwidth()),height=int(2/100*int(root.winfo_screenheight())),y=int(16/100*int(root.winfo_screenheight())))
what_clic_do_inf = tk.Label(root,text="go",relief="flat",background="lightblue")
what_clic_do_inf.place(x=6/100*int(root.winfo_screenwidth()),width=2/100*int(root.winfo_screenwidth()),height=int(2/100*int(root.winfo_screenheight())),y=int(16/100*int(root.winfo_screenheight())))
clic_ad_start = tk.Button(root,text="=>",relief="solid",command=cursor_muve_function)
clic_ad_start.place(x=8/100*int(root.winfo_screenwidth()),width=2/100*int(root.winfo_screenwidth()),height=int(2/100*int(root.winfo_screenheight())),y=int(16/100*int(root.winfo_screenheight())))
#write functions add
def cursor_write_function():
    global i,path
#read the number of lines
    with open(path , 'r') as file:
        lines = file.readlines()
    lines[len(lines)-1]= f" pyautogui.write(\"{write_inp.get()}\" ) \n"
    i+=1
    lines.append('\n')
#apply 
    with open(path , 'w+') as file:
        file.writelines(lines)
write_inf = tk.Label(root ,text ="write",relief="flat",background="lightblue")
write_inf.place(y=int(18/100*int(root.winfo_screenheight())),width=2/100*int(root.winfo_screenwidth()),x=0,height=int(2/100*int(root.winfo_screenheight())))
write_inp = tk.Entry(root ,relief="solid",background="white")
write_inp.place(y=int(18/100*int(root.winfo_screenheight())),width=6/100*int(root.winfo_screenwidth()),x=2/100*int(root.winfo_screenwidth()),height=int(2/100*int(root.winfo_screenheight())))
write_ad_start = tk.Button(root,text="=>",relief="solid",command=cursor_write_function)
write_ad_start.place(x=8/100*int(root.winfo_screenwidth()),width=2/100*int(root.winfo_screenwidth()),height=int(2/100*int(root.winfo_screenheight())),y=int(18/100*int(root.winfo_screenheight())))
#sleep functions add
def cursor_sleep_function():
    global i,path
#read the number of lines
    with open(path , 'r') as file:
        lines = file.readlines()
    lines[len(lines)-1]= f" time.sleep({sleep_inp.get()} ) \n"
    i+=1
    lines.append('\n')
#apply 
    with open(path , 'w+') as file:
        file.writelines(lines)
sleep_inf = tk.Label(root ,text ="sleep",relief="flat",background="lightblue")
sleep_inf.place(y=int(20/100*int(root.winfo_screenheight())),width=2/100*int(root.winfo_screenwidth()),x=0,height=int(2/100*int(root.winfo_screenheight())))
sleep_inp = tk.Entry(root ,relief="solid",background="white")
sleep_inp.place(y=int(20/100*int(root.winfo_screenheight())),width=6/100*int(root.winfo_screenwidth()),x=2/100*int(root.winfo_screenwidth()),height=int(2/100*int(root.winfo_screenheight())))
sleep_ad_start = tk.Button(root,text="=>",relief="solid",command= cursor_sleep_function)
sleep_ad_start.place(x=8/100*int(root.winfo_screenwidth()),width=2/100*int(root.winfo_screenwidth()),height=int(2/100*int(root.winfo_screenheight())),y=int(20/100*int(root.winfo_screenheight())))
#press keys 
def cursor_presss_function():
    global i,path
#read the number of lines
    with open(path , 'r') as file:
        lines = file.readlines()
    lines[len(lines)-1]= f" pyautogui.hotkey({keys} ) \n"
    i+=1
    lines.append('\n')
#apply 
    with open(path , 'w+') as file:
        file.writelines(lines)
    keys.clear()    
#this function os pushing into the array the keys 
keys= []
def ad_keys():
    global keys,b
    keys.append(f"{press_inp.get()}")
press_inf = tk.Label(root ,text ="press",relief="flat",background="lightblue")
press_inf.place(y=int(22/100*int(root.winfo_screenheight())),width=2/100*int(root.winfo_screenwidth()),x=0,height=int(2/100*int(root.winfo_screenheight())))
press_inp = tk.Entry(root ,relief="solid",background="white")
press_inp.place(y=int(22/100*int(root.winfo_screenheight())),width=4/100*int(root.winfo_screenwidth()),x=2/100*int(root.winfo_screenwidth()),height=int(2/100*int(root.winfo_screenheight())))
ad_key_button = tk.Button(root,text="+",command=ad_keys,relief="solid")
ad_key_button.place(x=6/100*int(root.winfo_screenwidth()),width=2/100*int(root.winfo_screenwidth()),height=int(2/100*int(root.winfo_screenheight())),y=int(22/100*int(root.winfo_screenheight())))
press_ad_start = tk.Button(root,text="=>",relief="solid",command=cursor_presss_function)
press_ad_start.place(x=8/100*int(root.winfo_screenwidth()),width=2/100*int(root.winfo_screenwidth()),height=int(2/100*int(root.winfo_screenheight())),y=int(22/100*int(root.winfo_screenheight())))
#clic
def right_clic_conf():
    global i,path
    with open(path , 'r') as file:
        lines = file.readlines()
    lines[len(lines)-1]= f" pyautogui.rightClick() \n "
    i+=1
    lines.append('\n')
    with open(path , 'w+') as file:
        file.writelines(lines)
def left_clic_conf():
    global i,path
    with open(path , 'r') as file:
        lines = file.readlines()
    lines[len(lines)-1]= f" pyautogui.click() \n "
    i+=1
    lines.append('\n')
    with open(path , 'w+') as file:
        file.writelines(lines)
left_clic = tk.Button(root,text="left",relief="solid",background="grey",command=left_clic_conf)
left_clic.place(x=0,y=24/100*int(root.winfo_screenheight()),height=2/100*int(root.winfo_screenheight()),width=5/100*int(root.winfo_screenwidth()))
right_clic = tk.Button(root,text="right",relief="solid",background="grey",command=right_clic_conf)
right_clic.place(x=5/100*int(root.winfo_screenwidth()),y=24/100*int(root.winfo_screenheight()),height=2/100*int(root.winfo_screenheight()),width=5/100*int(root.winfo_screenwidth()))
#loop settings
#this function is building the way the script will run sending the chek box you choose 
def loop_setings_apply():
    global i ,path
    if (var1.get() == 1 and var2.get() == 0) and var3.get() == 0:

     with open(path , 'r') as file:
        lines = file.readlines()
     lines[3]=f"while True: \n"
     lines[2] = "time_start = time.time()\n"
     lines[int(len(lines))+1]=f" if time.time() - time_start >= {time_setings_value.get()} : break "
     lines.append('\n')
     with open(path , 'w+') as file:
        file.writelines(lines)
    elif (var1.get() == 0 and var2.get() == 1) and var3.get() == 0:
     with open(path , 'r') as file:
        lines = file.readlines()
     lines[3]= f"while True:\n"
     lines[int(len(lines))+1]=f" if keyboard.is_pressed(\'{key_setings_value.get()}\'): break "
     lines.append('\n')
     with open(path , 'w+') as file:
        file.writelines(lines)
    elif (var1.get() == 0 and var2.get() == 0) and var3.get() == 1:
     with open(path , 'r') as file:
        lines = file.readlines()
     lines[2] = f"i = 0 \n"
     lines[3]= f"while i <= {xtimes_setings_value.get()}:\n"
     lines[int(len(lines) -1)]=f" i+=1 "
     lines.append('\n')
     with open(path , 'w+') as file:
        file.writelines(lines)


var1,var2,var3 =tk.IntVar(),tk.IntVar(),tk.IntVar()
infos_text = (
    "If you want to set a timer, check the timer box and\n "
    "enter the time in seconds in the right box next to the time.\n"
    "If you want the loop to continue until you press a key, check\n "
    "the custom box and enter the desired key in the right box.\n"
    "If you want the script to repeat for x times, check the box with x times\n "
    "and enter the desired number in the right box."
)
infos = tk.Label(root,relief="flat",text=infos_text,wraplength=20/100*int(root.winfo_screenwidth()))
infos.place(y=int(26/100*int(root.winfo_screenheight())),width=21/100*int(root.winfo_screenwidth()),x=0,height=int(13/100*int(root.winfo_screenheight())))
time_setings=tk.Checkbutton(root,text="timer",onvalue=1,offvalue=0,variable=var1,background="lightblue",relief="flat")
time_setings.place(y=int(39/100*int(root.winfo_screenheight())),width=5/100*int(root.winfo_screenwidth()),x=0,height=int(2/100*int(root.winfo_screenheight())))
time_setings_value=tk.Entry(root,relief="solid",background="white")
time_setings_value.place(y=int(39/100*int(root.winfo_screenheight())),width=5/100*int(root.winfo_screenwidth()),x=5/100*int(root.winfo_screenwidth()),height=int(2/100*int(root.winfo_screenheight())))
key_setings=tk.Checkbutton(root,text="custom",onvalue=1,offvalue=0,variable=var2,background="lightblue",relief="flat")
key_setings.place(y=int(41/100*int(root.winfo_screenheight())),width=5/100*int(root.winfo_screenwidth()),x=0,height=int(2/100*int(root.winfo_screenheight())))
key_setings_value=tk.Entry(root,relief="solid",background="white")
key_setings_value.place(y=int(41/100*int(root.winfo_screenheight())),width=5/100*int(root.winfo_screenwidth()),x=5/100*int(root.winfo_screenwidth()),height=int(2/100*int(root.winfo_screenheight())))
xtimes_setings=tk.Checkbutton(root,text="x times",onvalue=1,offvalue=0,variable=var3,background="lightblue",relief="flat")
xtimes_setings.place(y=int(43/100*int(root.winfo_screenheight())),width=5/100*int(root.winfo_screenwidth()),x=0,height=int(2/100*int(root.winfo_screenheight())))
xtimes_setings_value=tk.Entry(root,relief="solid",background="white")
xtimes_setings_value.place(y=int(43/100*int(root.winfo_screenheight())),width=5/100*int(root.winfo_screenwidth()),x=5/100*int(root.winfo_screenwidth()),height=int(2/100*int(root.winfo_screenheight())))
#apply button
apply_loop_button = tk.Button(root,text="apply",relief="solid",command=loop_setings_apply)
apply_loop_button.place(y=int(39/100*int(root.winfo_screenheight())),width=5/100*int(root.winfo_screenwidth()),x=10/100*int(root.winfo_screenwidth()),height=int(6/100*int(root.winfo_screenheight())))
#delete function
def delete():
    global path
    line_to_delete = int(line_dlt.get())+ 4
    
    with open(path, 'r') as file:
        lines = file.readlines()

    with open(path, 'w') as file:
        for number, line in enumerate(lines, start=1):
            if number != line_to_delete:
                file.write(line)

delete_button = tk.Button(root,text="DLT",command=delete,background="grey")
delete_button.place(y=int(45/100*int(root.winfo_screenheight())),width=5/100*int(root.winfo_screenwidth()),x=0,height=int(2/100*int(root.winfo_screenheight())))
line_dlt=tk.Entry(root,relief="solid",background="white")
line_dlt.place(y=int(45/100*int(root.winfo_screenheight())),width=5/100*int(root.winfo_screenwidth()),x=5/100*int(root.winfo_screenwidth()),height=int(2/100*int(root.winfo_screenheight())))
root.mainloop()

