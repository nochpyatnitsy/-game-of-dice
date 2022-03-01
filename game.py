from tkinter import *
import random , time


def trow ():
    __painting = random.choice(['b.png' ,'b2.png' ,'b3.png' ,
                                'b4.png' ,'b5.png' ,'b6.png'])
    return __painting


def img (event):
    global __mark_1 , __mark_2
    for i in range (18):
        __mark_1 = PhotoImage(file = (trow()))
        __mark_2 = PhotoImage(file = (trow()))
        __Block_1['image'] = __mark_1
        __Block_2['image'] = __mark_2
        root.update()
        time.sleep(0.12)


root = Tk()
root.geometry('400x400')
root.title('game of dice. Click and play!')
root.resizable(height = False , width = False)
root.iconphoto(True , PhotoImage (file = ('icon.png')))


__Background = [PhotoImage(file = 'BG.gif' , format = 'gif -index %i' %(i)) for i in range(100)]
def update(ind):
    frame = __Background[ind]
    ind += 1
    label.configure(image = frame)
    root.after(100 , update , ind)
label = Label(root)
label.pack()
root.after(1 , update , 1)


__Block_1 = Label(root)
__Block_1.place(relx = 0.3 , rely = 0.5 , anchor = CENTER)
__Block_2 = Label(root)
__Block_2.place(relx = 0.7 , rely = 0.5 , anchor = CENTER)


root.bind('<1>' , img)
img ('event')



root.mainloop()