from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from time import*

from pyautogui import *
from pywhatkit import *

class WhatsApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Unlimited WhatsApp Message")
        self.root.geometry("1920x1080+0+0")

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

        self.x=[]
        self.count=1
        self.ask=False

    

        

        img=Image.open("grey2.jpg")
        img=img.resize((1920,1080))
        self.photoimg=ImageTk.PhotoImage(img)
        lbl_img=Label(self.root,image=self.photoimg,borderwidth=0,bg="black")
        lbl_img.place(x=0,y=0,width=1920,height=1080)


        frame=Frame(lbl_img,bg="darkslategrey")
        frame.place(x=40,y=170,height=400,width=700)

        lblheader=Label(self.root,text="UNLIMITED WHATSAPP MESSEGE",bg="steelblue",fg="white",font=('times new roman',33,'bold'))
        lblheader.place(x=40,y=90,width=700,height=80)

        lbl1=Label(frame,text="Enter mobile number : ",bg="darkslategrey",fg="white",font=('times new roman',20,'bold'))
        lbl1.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        entry1=ttk.Entry(frame, textvariable=self.mobile,font=('times new roman',20,'bold'),width=15)
        entry1.grid(row=0,column=1,pady=10,sticky=W)

        lbl2=Label(frame,text="Enter Message for send : ",bg="darkslategrey",fg="white",font=('times new roman',20,'bold'))
        lbl2.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        entry2=ttk.Entry(frame, textvariable=self.message,font=('times new roman',20,'bold'),width=15)
        entry2.grid(row=1,column=1,pady=10,sticky=W)

        lbl3=Label(frame,text="How many times send : ",bg="darkslategrey",fg="white",font=('times new roman',20,'bold'))
        lbl3.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        entry3=ttk.Entry(frame, textvariable=self.times,font=('times new roman',20,'bold'),width=15)
        entry3.grid(row=2,column=1,pady=10,sticky=W)


        btn=Button(frame,text="Submit",command=self.send,font=('times new roman',30,'bold'),bd=10,fg="white",bg="blue",cursor="hand2")
        btn.grid(row=3,columnspan=2,pady=20)


        lab_pk=Label(self.root,text="Created By- Ashish Gupta",fg="white",bg="steelblue",font=('times new roman',15,'bold')).place(y=570,x=250,width=350)

        # print(self.times.get())

        frame1=Frame(lbl_img,bg="darkslategrey")
        frame1.place(x=950,y=135,height=500,width=800)

        lblheader1=Label(self.root,text="ADIT STUDENT",bg="steelblue",fg="white",font=('times new roman',30,'bold'))
        lblheader1.place(x=1000,y=90,width=400)
        

        chk1=Checkbutton(frame1,bg="white",variable=self.name1,onvalue=1,offvalue=0).grid(row=0,column=0,padx=20,sticky=W)
        lbl1=Label(frame1,text="Ambika Ajai Singh",font=("times new roman",10,"bold"),bg="white").grid(row=0,column=1,sticky=W)
        
        chk2=Checkbutton(frame1,bg="white",variable=self.name2,onvalue=1,offvalue=0).grid(row=0,column=2,padx=20,sticky=W)
        lbl2=Label(frame1,text="Anjali Kesharwani",font=("times new roman",10,"bold"),bg="white").grid(row=0,column=3,sticky=W)

        chk3=Checkbutton(frame1,bg="white",variable=self.name3,onvalue=1,offvalue=0).grid(row=1,column=0,padx=20,sticky=W)
        lbl3=Label(frame1,text="Annapurna Rawat",font=("times new roman",10,"bold"),bg="white").grid(row=1,column=1,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name4,onvalue=1,offvalue=0).grid(row=1,column=2,padx=20,sticky=W)
        lbl4=Label(frame1,text="Ashish Gupta",font=("times new roman",10,"bold"),bg="white").grid(row=1,column=3,sticky=W)

        chk1=Checkbutton(frame1,bg="white",variable=self.name5,onvalue=1,offvalue=0).grid(row=2,column=0,padx=20,sticky=W)
        lbl1=Label(frame1,text="Atul Srivastav",font=("times new roman",10,"bold"),bg="white").grid(row=2,column=1,sticky=W)
        
        chk2=Checkbutton(frame1,bg="white",variable=self.name6,onvalue=1,offvalue=0).grid(row=2,column=2,padx=20,sticky=W)
        lbl2=Label(frame1,text="Hanuman Yadav",font=("times new roman",10,"bold"),bg="white").grid(row=2,column=3,sticky=W)

        chk3=Checkbutton(frame1,bg="white",variable=self.name7,onvalue=1,offvalue=0).grid(row=3,column=0,padx=20,sticky=W)
        lbl3=Label(frame1,text="Jyoti Mishra",font=("times new roman",10,"bold"),bg="white").grid(row=3,column=1,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name8,onvalue=1,offvalue=0).grid(row=3,column=2,padx=20,sticky=W)
        lbl4=Label(frame1,text="Manorma",font=("times new roman",10,"bold"),bg="white").grid(row=3,column=3,sticky=W)
    
        chk3=Checkbutton(frame1,bg="white",variable=self.name9,onvalue=1,offvalue=0).grid(row=4,column=0,padx=20,sticky=W)
        lbl3=Label(frame1,text="Piyush Sharma",font=("times new roman",10,"bold"),bg="white").grid(row=4,column=1,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name10,onvalue=1,offvalue=0).grid(row=4,column=2,padx=20,sticky=W)
        lbl4=Label(frame1,text="Pratibha",font=("times new roman",10,"bold"),bg="white").grid(row=4,column=3,sticky=W)
    
        chk3=Checkbutton(frame1,bg="white",variable=self.name11,onvalue=1,offvalue=0).grid(row=5,column=0,padx=20,sticky=W)
        lbl3=Label(frame1,text="Pushoanjali Chaurasiya",font=("times new roman",10,"bold"),bg="white").grid(row=5,column=1,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name12,onvalue=1,offvalue=0).grid(row=5,column=2,padx=20,sticky=W)
        lbl4=Label(frame1,text="Richa Srivastava",font=("times new roman",10,"bold"),bg="white").grid(row=5,column=3,sticky=W)

        chk3=Checkbutton(frame1,bg="white",variable=self.name13,onvalue=1,offvalue=0).grid(row=6,column=0,padx=20,sticky=W)
        lbl3=Label(frame1,text="Saksham Katiyar",font=("times new roman",10,"bold"),bg="white").grid(row=6,column=1,sticky=W)
        chk4=Checkbutton(frame1,bg="white",variable=self.name14,onvalue=1,offvalue=0).grid(row=6,column=2,padx=20,sticky=W)
        lbl4=Label(frame1,text="Sakshi Chaurasiya",font=("times new roman",10,"bold"),bg="white").grid(row=6,column=3,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name15,onvalue=1,offvalue=0).grid(row=7,column=0,padx=20,sticky=W)
        lbl4=Label(frame1,text="Shilpi Jaiswal",font=("times new roman",10,"bold"),bg="white").grid(row=7,column=1,sticky=W)
    
        chk3=Checkbutton(frame1,bg="white",variable=self.name16,onvalue=1,offvalue=0).grid(row=7,column=2,padx=20,sticky=W)
        lbl3=Label(frame1,text="Sonu Kumar",font=("times new roman",10,"bold"),bg="white").grid(row=7,column=3,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name17,onvalue=1,offvalue=0).grid(row=8,column=0,padx=20,sticky=W)
        lbl4=Label(frame1,text="Sugandha Yadav",font=("times new roman",10,"bold"),bg="white").grid(row=8,column=1,sticky=W)
    
        chk3=Checkbutton(frame1,bg="white",variable=self.name18,onvalue=1,offvalue=0).grid(row=8,column=2,padx=20,sticky=W)
        lbl3=Label(frame1,text="Trapti",font=("times new roman",10,"bold"),bg="white").grid(row=8,column=3,sticky=W)

        chk4=Checkbutton(frame1,bg="white",variable=self.name19,onvalue=1,offvalue=0).grid(row=9,column=0,padx=20,sticky=W)
        lbl4=Label(frame1,text="Vaishnavi Kesharwani",font=("times new roman",10,"bold"),bg="white").grid(row=9,column=1,sticky=W) 

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
            x=messagebox.askyesno("Sure","Are you sure for send message")
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
        
        self.ask=messagebox.askyesno("Right","Are you Sure for send message ?",parent=self.root)
        if self.ask==True:
            if self.count==1:
            
                if self.name1.get()==1:
                    self.x.append("Ambika Ajai Singh\n")
                
                if self.name2.get()==1:
                    self.x.append("Anjali Kesharwani\n")
                if self.name3.get()==1:
                    self.x.append("Annapurna Rawat\n")
                
                if self.name4.get()==1:
                    self.x.append("ASHISH GUPTA\n")
                if self.name5.get()==1:
                    self.x.append("Atul Srivastav\n")
                
                if self.name6.get()==1:
                    self.x.append("Hanuman yadav\n")
                if self.name7.get()==1:
                    self.x.append("jyoti Mishra\n")
                
                if self.name8.get()==1:
                    self.x.append("Manorma\n")
                if self.name9.get()==1:
                    self.x.append("Piyush Sharma\n")
                
                if self.name10.get()==1:
                    self.x.append("Pratibha\n")
                if self.name11.get()==1:
                    self.x.append("Pushpanjali Chaurasiya\n")
                
                if self.name12.get()==1:
                    self.x.append("Richa Srivastav\n")
                if self.name13.get()==1:
                    self.x.append("Saksham Katiyar\n")
                
                if self.name14.get()==1:
                    self.x.append("Sakshi Chaurasiya\n")
                if self.name15.get()==1:
                    self.x.append("Shilpi Jaiswal\n ")
                
                if self.name16.get()==1:
                    self.x.append("Sonu Kumar\n")
                if self.name17.get()==1:
                    self.x.append("Sugandha Yadav\n")
                
                if self.name18.get()==1:
                    self.x.append("Trapti\n")
                if self.name19.get()==1:
                    self.x.append("Vaishnavi Kesharwani\n")
                
                
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
            x=messagebox.askyesno("Saure","Are you sure for send message",parent=self.root)
            h=int(time.strftime("%H"))
            m=int(time.strftime("%M"))
            date=strftime("%d/%m/%Y")
            if x==True:
                try:
                    sendwhatmsg(f'+91 9451451491',f" Prayagraj ADIT Present Students Date-{date} \n{student_name}",h,(m+1))


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



