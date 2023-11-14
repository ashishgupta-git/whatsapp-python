from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import messagebox
from time import*

from numpy import angle
from pyautogui import *
from pywhatkit import *

class WhatsApp:
    def __init__(self,root):
        self.root=root
        self.root.title("WhatsMessage send")
        self.root.geometry("1366x760+0+0")

        self.mobile=StringVar()
        self.message=StringVar()
        self.times=IntVar()

        self.name1=IntVar()
        self.name2=IntVar()
        self.name3=IntVar()
        self.name4=IntVar()
        self.name5=IntVar()
        self.name6=IntVar()
        self.name7=IntVar()
        self.name8=IntVar()
        self.name9=IntVar()
        self.name10=IntVar()
        self.name11=IntVar()
        self.name12=IntVar()
        self.name13=IntVar()
        self.name14=IntVar()
        self.name15=IntVar()
        self.name16=IntVar()
        self.name17=IntVar()
        self.name18=IntVar()
        self.name19=IntVar()
        self.name20=IntVar()
        self.name21=IntVar()
        self.name22=IntVar()
        self.name23=IntVar()
        self.name24=IntVar()
        self.name25=IntVar()
        self.name26=IntVar()
        self.name27=IntVar()
        self.name28=IntVar()
        self.name29=IntVar()
        self.name30=IntVar()

        self.x=[]
        self.count=1
        self.ask=False

    

        

        img=Image.open("whatsAppMessageSend.png")
        img=img.resize((1366,760))
        self.photoimg=ImageTk.PhotoImage(img)
        lbl_img=Label(self.root,image=self.photoimg,borderwidth=0,bg="black")
        lbl_img.place(x=0,y=0,width=1366,height=760)


        frame=Frame(lbl_img,bg="white")
        frame.place(x=50,y=135,height=300,width=600)

        lblheader=Label(self.root,text="WHATSAPP MESSAGE SEND",bg="yellow",fg="green",font=('times new roman',30,'bold'))
        lblheader.place(x=50,y=90,width=600)

        lbl1=Label(frame,text="Enter mobile number : ",bg="white",fg="blue",font=('times new roman',20,'bold'))
        lbl1.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        entry1=ttk.Entry(frame, textvariable=self.mobile,font=('times new roman',20,'bold'),width=15)
        entry1.grid(row=0,column=1,pady=10,sticky=W)

        lbl2=Label(frame,text="Enter Message for send : ",bg="white",fg="blue",font=('times new roman',20,'bold'))
        lbl2.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        entry2=ttk.Entry(frame, textvariable=self.message,font=('times new roman',20,'bold'),width=15)
        entry2.grid(row=1,column=1,pady=10,sticky=W)

        lbl3=Label(frame,text="How many times send : ",bg="white",fg="blue",font=('times new roman',20,'bold'))
        lbl3.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        entry3=ttk.Entry(frame, textvariable=self.times,font=('times new roman',20,'bold'),width=15)
        entry3.grid(row=2,column=1,pady=10,sticky=W)


        btn=Button(frame,text="Submit",command=self.send,font=('times new roman',30,'bold'),bd=10,fg="white",bg="blue",cursor="hand2")
        btn.grid(row=3,columnspan=2,pady=20)


        lab_pk=Label(self.root,text="Created By Phool Chand Varun",fg="white",bg="lime",font=('times new roman',30,'bold')).place(y=435,x=50,width=600)

        # print(self.times.get())

        frame1=Frame(lbl_img,bg="white")
        frame1.place(x=700,y=135,height=450,width=600)

        lblheader1=Label(self.root,text="ADIT STUDENT ATTENDANCE ",bg="yellow",fg="green",font=('times new roman',30,'bold'))
        lblheader1.place(x=700,y=90,width=600)
        

        chk1=Checkbutton(frame1,bg="white",variable=self.name1,onvalue=1,offvalue=0).grid(row=0,column=0,padx=20,sticky=W)
        lbl1=Label(frame1,text="AADITYA SHARMA",font=("times new roman",10,"bold"),bg="white").grid(row=0,column=1,sticky=W)
        
        chk2=Checkbutton(frame1,bg="white",variable=self.name2,onvalue=1,offvalue=0).grid(row=0,column=2,padx=20,sticky=W)
        lbl2=Label(frame1,text="ABHIMANYU TIWARI",font=("times new roman",10,"bold"),bg="white").grid(row=0,column=3,sticky=W)

        chk3=Checkbutton(frame1,bg="white",variable=self.name3,onvalue=1,offvalue=0).grid(row=1,column=0,padx=20,sticky=W)
        lbl3=Label(frame1,text="ABHISHEK MISHRA",font=("times new roman",10,"bold"),bg="white").grid(row=1,column=1,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name4,onvalue=1,offvalue=0).grid(row=1,column=2,padx=20,sticky=W)
        lbl4=Label(frame1,text="ABHISHEK TIWARI",font=("times new roman",10,"bold"),bg="white").grid(row=1,column=3,sticky=W)

        chk1=Checkbutton(frame1,bg="white",variable=self.name5,onvalue=1,offvalue=0).grid(row=2,column=0,padx=20,sticky=W)
        lbl1=Label(frame1,text="AKASH GUPTA",font=("times new roman",10,"bold"),bg="white").grid(row=2,column=1,sticky=W)
        
        chk2=Checkbutton(frame1,bg="white",variable=self.name6,onvalue=1,offvalue=0).grid(row=2,column=2,padx=20,sticky=W)
        lbl2=Label(frame1,text="ANKIT KUMAR GAUTAM",font=("times new roman",10,"bold"),bg="white").grid(row=2,column=3,sticky=W)

        chk3=Checkbutton(frame1,bg="white",variable=self.name7,onvalue=1,offvalue=0).grid(row=3,column=0,padx=20,sticky=W)
        lbl3=Label(frame1,text="ANMOL VERMA",font=("times new roman",10,"bold"),bg="white").grid(row=3,column=1,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name8,onvalue=1,offvalue=0).grid(row=3,column=2,padx=20,sticky=W)
        lbl4=Label(frame1,text="ASTHA SACHAN",font=("times new roman",10,"bold"),bg="white").grid(row=3,column=3,sticky=W)
    
        chk3=Checkbutton(frame1,bg="white",variable=self.name9,onvalue=1,offvalue=0).grid(row=4,column=0,padx=20,sticky=W)
        lbl3=Label(frame1,text="DEEPAK KUMAR",font=("times new roman",10,"bold"),bg="white").grid(row=4,column=1,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name10,onvalue=1,offvalue=0).grid(row=4,column=2,padx=20,sticky=W)
        lbl4=Label(frame1,text="HARSH SHUKLA",font=("times new roman",10,"bold"),bg="white").grid(row=4,column=3,sticky=W)
    
        chk3=Checkbutton(frame1,bg="white",variable=self.name11,onvalue=1,offvalue=0).grid(row=5,column=0,padx=20,sticky=W)
        lbl3=Label(frame1,text="HIMANSHU DUBEY",font=("times new roman",10,"bold"),bg="white").grid(row=5,column=1,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name12,onvalue=1,offvalue=0).grid(row=5,column=2,padx=20,sticky=W)
        lbl4=Label(frame1,text="HIMANSHU RAJPUT",font=("times new roman",10,"bold"),bg="white").grid(row=5,column=3,sticky=W)

        chk3=Checkbutton(frame1,bg="white",variable=self.name13,onvalue=1,offvalue=0).grid(row=6,column=0,padx=20,sticky=W)
        lbl3=Label(frame1,text="MANOJ KUAMR",font=("times new roman",10,"bold"),bg="white").grid(row=6,column=1,sticky=W)
        chk4=Checkbutton(frame1,bg="white",variable=self.name14,onvalue=1,offvalue=0).grid(row=6,column=2,padx=20,sticky=W)
        lbl4=Label(frame1,text="PAWAN KUMAR",font=("times new roman",10,"bold"),bg="white").grid(row=6,column=3,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name15,onvalue=1,offvalue=0).grid(row=7,column=0,padx=20,sticky=W)
        lbl4=Label(frame1,text="PHOOL CHAND VARUN",font=("times new roman",10,"bold"),bg="white").grid(row=7,column=1,sticky=W)
    
        chk3=Checkbutton(frame1,bg="white",variable=self.name16,onvalue=1,offvalue=0).grid(row=7,column=2,padx=20,sticky=W)
        lbl3=Label(frame1,text="PRIYANSHI SHARMA",font=("times new roman",10,"bold"),bg="white").grid(row=7,column=3,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name17,onvalue=1,offvalue=0).grid(row=8,column=0,padx=20,sticky=W)
        lbl4=Label(frame1,text="RICHA KUMARI",font=("times new roman",10,"bold"),bg="white").grid(row=8,column=1,sticky=W)
    
        chk3=Checkbutton(frame1,bg="white",variable=self.name18,onvalue=1,offvalue=0).grid(row=8,column=2,padx=20,sticky=W)
        lbl3=Label(frame1,text="ROHIT PANDEY",font=("times new roman",10,"bold"),bg="white").grid(row=8,column=3,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name19,onvalue=1,offvalue=0).grid(row=9,column=0,padx=20,sticky=W)
        lbl4=Label(frame1,text="SACHIN SINGH",font=("times new roman",10,"bold"),bg="white").grid(row=9,column=1,sticky=W)

        chk3=Checkbutton(frame1,bg="white",variable=self.name20,onvalue=1,offvalue=0).grid(row=9,column=2,padx=20,sticky=W)
        lbl3=Label(frame1,text="SATYAM SAHU",font=("times new roman",10,"bold"),bg="white").grid(row=9,column=3,sticky=W)
        
        chk3=Checkbutton(frame1,bg="white",variable=self.name21,onvalue=1,offvalue=0).grid(row=10,column=0,padx=20,sticky=W)
        lbl3=Label(frame1,text="SHAIL KUMARI",font=("times new roman",10,"bold"),bg="white").grid(row=10,column=1,sticky=W)
        chk4=Checkbutton(frame1,bg="white",variable=self.name22,onvalue=1,offvalue=0).grid(row=10,column=2,padx=20,sticky=W)
        lbl4=Label(frame1,text="SHAILJA PAL",font=("times new roman",10,"bold"),bg="white").grid(row=10,column=3,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name23,onvalue=1,offvalue=0).grid(row=11,column=0,padx=20,sticky=W)
        lbl4=Label(frame1,text="SONALI MISHRA",font=("times new roman",10,"bold"),bg="white").grid(row=11,column=1,sticky=W)
    
        chk3=Checkbutton(frame1,bg="white",variable=self.name24,onvalue=1,offvalue=0).grid(row=11,column=2,padx=20,sticky=W)
        lbl3=Label(frame1,text="VINOD KUMAR SHARMA",font=("times new roman",10,"bold"),bg="white").grid(row=11,column=3,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name25,onvalue=1,offvalue=0).grid(row=12,column=0,padx=20,sticky=W)
        lbl4=Label(frame1,text="EMPTY",font=("times new roman",10,"bold"),bg="white").grid(row=12,column=1,sticky=W)

        chk3=Checkbutton(frame1,bg="white",variable=self.name26,onvalue=1,offvalue=0).grid(row=12,column=2,padx=20,sticky=W)
        lbl3=Label(frame1,text="EMPTY",font=("times new roman",10,"bold"),bg="white").grid(row=12,column=3,sticky=W)
        
        chk4=Checkbutton(frame1,bg="white",variable=self.name27,onvalue=1,offvalue=0).grid(row=13,column=0,padx=20,sticky=W)
        lbl4=Label(frame1,text="EMPTY",font=("times new roman",10,"bold"),bg="white").grid(row=13,column=1,sticky=W)
    
        chk3=Checkbutton(frame1,bg="white",variable=self.name28,onvalue=1,offvalue=0).grid(row=13,column=2,padx=20,sticky=W)
        lbl3=Label(frame1,text="EMPTY",font=("times new roman",10,"bold"),bg="white").grid(row=13,column=3,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name29,onvalue=1,offvalue=0).grid(row=14,column=0,padx=20,sticky=W)
        lbl4=Label(frame1,text="EMPTY",font=("times new roman",10,"bold"),bg="white").grid(row=14,column=1,sticky=W)
    
        chk3=Checkbutton(frame1,bg="white",variable=self.name30,onvalue=1,offvalue=0).grid(row=14,column=2,padx=20,sticky=W)
        lbl3=Label(frame1,text="EMPTY",font=("times new roman",10,"bold"),bg="white").grid(row=14,column=3,sticky=W)

 

        btn=Button(frame1,text="Submit",command=self.name,font=('times new roman',20,'bold'),bd=5,fg="white",bg="blue",cursor="hand2")
        btn.grid(row=15,columnspan=2,pady=10,padx=50,column=0,sticky=W)
        btn=Button(frame1,text="Send",command=self.send1,font=('times new roman',20,'bold'),bd=5,fg="white",bg="blue",cursor="hand2")
        btn.grid(row=15,columnspan=2,padx=50,pady=10,column=3,sticky=W)


         
       

    def send(self):
        h=int(time.strftime("%H"))
        m=int(time.strftime("%M"))
    
        if len(self.mobile.get())!=10:
            messagebox.showerror("Error","Please Enter 10 Digit Number",parent=self.root)
            return
        elif self.message.get()=="":
            messagebox.showerror("Error","Please Enter Your message",parent=self.root)
            return
        elif self.times.get()==0:
            messagebox.showerror("Error","Please Enter How many times send message",parent=self.root)
        else:
            x=messagebox.askyesno("Saure","Are you saure for send message")
        if x==True:
            try:
                sendwhatmsg(f'+91 {self.mobile.get()}',self.message.get(),h,(m+1))


                for i in range(self.times.get()-1):
                    typewrite(self.message.get())
                    press('enter')
            except Exception as es:
                messagebox.showerror('Error',f'Due To : {str(es)}',parent=self.root)
        else:
            return
        
    def name(self):
        
        self.ask=messagebox.askyesno("Right","Are you Saure for send message ?",parent=self.root)
        if self.ask==True:
            if self.count==1:
            
                if self.name1.get()==1:
                    self.x.append("Aaditya Sharma\n")
                
                if self.name2.get()==1:
                    self.x.append("Abhimanyu Tiwari\n")
                if self.name3.get()==1:
                    self.x.append("Abhishek Mishra\n")
                
                if self.name4.get()==1:
                    self.x.append("Abhishek Tiwari\n")
                if self.name5.get()==1:
                    self.x.append("Akash Gupta\n")
                
                if self.name6.get()==1:
                    self.x.append("Ankit Kumar Gautam\n")
                if self.name7.get()==1:
                    self.x.append("Anmol Verma\n")
                
                if self.name8.get()==1:
                    self.x.append("Astha Sachan\n")
                if self.name9.get()==1:
                    self.x.append("Deepak Kumar\n")
                
                if self.name10.get()==1:
                    self.x.append("Harsh Shukla\n")
                if self.name11.get()==1:
                    self.x.append("Himanshu Dubey\n")
                
                if self.name12.get()==1:
                    self.x.append("Himanshu Rajput\n")
                if self.name13.get()==1:
                    self.x.append("Manoj Kumar\n")
                
                if self.name14.get()==1:
                    self.x.append("Pawan Kumar\n")
                if self.name15.get()==1:
                    self.x.append("Phool Chand Varun\n ")
                
                if self.name16.get()==1:
                    self.x.append("Priyanshi Sharma\n")
                if self.name17.get()==1:
                    self.x.append("Richa Kumari\n")
                
                if self.name18.get()==1:
                    self.x.append("Rohit Pandey\n")
                if self.name19.get()==1:
                    self.x.append("Sachin Singh\n")
                
                if self.name20.get()==1:
                    self.x.append("Satyam Sahu\n")
                if self.name21.get()==1:
                    self.x.append("Shail Kuamri\n")
                if self.name22.get()==1:
                    self.x.append("Shaila Pal\n")
                
                if self.name23.get()==1:
                    self.x.append("Sonali Mishra\n")
                if self.name24.get()==1:
                    self.x.append("Vinod Kumar Sharma\n")
                
                if self.name25.get()==1:
                    self.x.append("No")
                if self.name26.get()==1:
                    self.x.append("No")
                
                if self.name27.get()==1:
                    self.x.append("No")
                if self.name28.get()==1:
                    self.x.append("No")
                
                if self.name29.get()==1:
                    self.x.append("No")
                if self.name30.get()==1:
                    self.x.append("No")
                
                self.count+=1
                
            else:
                return
        else:
            return

        
    def send1(self):
        
        if self.ask==True:
            student_name=""
            stu_num=1
            for i in self.x:
                student_name+=str(stu_num)+"-"+i
                stu_num+=1
            x=messagebox.askyesno("Saure","Are you saure for send message",parent=self.root)
            h=int(time.strftime("%H"))
            m=int(time.strftime("%M"))
            date=strftime("%d/%m/%Y")
            if x==True:
                try:
                    sendwhatmsg(f'+91 8795103163',f"ADIT KANPUR Present Student Date-{date} \n{student_name}",h,(m+1))


                    # for i in range(self.times.get()-1):
                    #     typewrite(self.message.get())
                    #     press('enter')
                except Exception as es:
                    messagebox.showerror('Error',f'Due To : {str(es)}',parent=self.root)
            else:
                return
        else:
            messagebox.showerror("Error","First select then send message !")
        

if __name__=="__main__":
    root=Tk()
    obj=WhatsApp(root)
    root.mainloop()



