from tkinter import *
burst=[]
arrival=[]
pname=[]
wind = Tk()
def getprint():
	pass


def sch():
	pname.append(e1.get())
	burst.append(e2.get())
	arrival.append(e3.get())
	getprint()


wind.title("Process scheduling App")
wind.geometry("600x400")
#head
lh= Label(wind,text="**PROESS SCHEDULING**")
lh.place(x=320,y=50)
#name
l1=Label(wind,text="Process Name :-")
l1.place(x=280,y=100)

e1=Entry()
e1.place(x=380,y=100)
#burst
l2=Label(wind,text="Burst Time :-")
l2.place(x=280,y=140)

e2=Entry()
e2.place(x=380,y=140)

#arrival
l3=Label(wind,text="Arrival Time :-")
l3.place(x=280,y=180)

e3=Entry()
e3.place(x=380,y=180)

#next
bnext=Button(wind,text="Next Process",command=sch)
bnext.place(x=520,y=140)

#fcfs
bfcfs=Button(wind,text="FCFS")
bfcfs.place(x=280,y=210)

#RR
brr=Button(wind,text="Round Robin")
brr.place(x=340,y=210)

#sjf
bsjf=Button(wind,text="SJF")
bsjf.place(x=440,y=210)

#srtf
bsrtf=Button(wind,text="SRTF")
bsrtf.place(x=480,y=210)

#priority
bpri=Button(wind,text="PRIORITY")
bpri.place(x=540,y=210)

#table
dsh= Label(wind,text="-"*75)
dsh.place(x=280,y=250)

head=Label(wind,text="NO.     Process Name      Burst Time      Arrival Time")
head.place(x=280,y=270)

dsh= Label(wind,text="-"*75)
dsh.place(x=280,y=290)

mainloop()