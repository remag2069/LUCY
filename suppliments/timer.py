from tkinter import *
from tkinter import font
import datetime as d
import time
from suppliments import voice_pa as v

# # print('set time:')
# k=input('set time : ')
# # k='20:00'
# if k=='':
#     k='23:59'

# v.hi()
def alarm(k='23:59'):
    window=Tk()
    def dom():
        window.wm_attributes("-topmost", 1)
    def sub():
        window.wm_attributes("-topmost", 0)
    h=font.Font(family='Helvetica', size=47, weight='bold')
    menubar = Menu(window)
    t_color=Menu(menubar,tearoff=0)
    t_color.add_command(label='dominate',command=dom)
    t_color.add_command(label='subordinate',command=sub)

    menubar.add_cascade(label="superiority", menu=t_color)
    # f.add_command(label="text colours", command=toggle_color_m)
    # filemenu.add_command(label="New", command=donothing)


    window.config(menu=menubar)
    # window.configure(title='DOOMSDAY')
    # window.iconphoto(False, '.\\suppliments\\timer.png')
    window.title('DOOMS-DAY CLOCK')
    l=Label(window,text='bye',font=h)
    l.grid()
    # c=Canvas(window,width=330,height=600)
    # c.grid()
    # c.create_oval(3,100,310,400)
    # c.create_oval(10,100,210,300)
    def run():
        c=d.datetime.now()
        t=str(c)
        t=t[11:]
        # print(int(t[3:5]))
        # m=str(int(k[3:5])-int(t[3:5]))
        h_i=int(k[:2])-int(t[:2])
        m_i=int(k[3:5])-int(t[3:5])
        s_i= - float(t[6:10])
        # print(s_i)
        if m_i<0:
            h_i=h_i-1
            m_i=60+m_i
        if h_i<10:
            h='0'+str(h_i)
        else:
            h=str(h_i)
        if s_i<0:
            m_i=m_i-1
            s_i=60+s_i
        if int(m_i/10)==0:
            m='0'+str(m_i)
        else:
            m=str(m_i)
        if int(s_i/10)==0:
            s='0'+str(s_i)
        else:
            s=str(s_i)

        # # m=str(int(k[3:5])-int(t[3:5]))
        # s=(60-float(t[6:]))
        # f=int(s)
        
        # s=str(s)
        # # if (((float(s)*100%1000)%100)%10)==0:
        # #     if int(f/10)==0:
        # #         s='0'+s
        # #         print('hi')
        # #     s=s[:4]
        # #     s=s+'0'
        # # else:
        # if int(f/10)==0:
        #     s='0'+s
        # # 
        # s=s[:5] 
        t=h+':'+m+':'+s[:4]
        l.configure(text=t,bg='#437779',fg='#00F6FF')
        # print(t)
        if t[:11]=='00:00:00.1':
            while True:
                v.hi()
            # exit()
        return t
    i=0
    p_c_i=0
    while True:
        # global p_c_i
        if i==0:
            p_c=run()
            i=i+1
        t=run()
        # p_c_i=int(p_c[:2])+int(p_c[3:5])/60+float(p_c[6:])/3600
        # t_c_i=int(t[:2])+int(t[3:5])/60+float(t[6:])/3600
        window.update()
        time.sleep(0.1)

