from tkinter import *
import random

window = Tk()
window.title("TIC TAC TOE")
but = []
k = []
lab = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
p = "x"
ch = []
pch = []
frame1 = Frame(master=window)
frame1.pack(fill=BOTH, side=LEFT, expand=False)
frame2 = Frame(master=window)
frame2.pack(fill=BOTH, side=LEFT, expand=False)


def kill():
    for r in but:
        if r not in pch and r not in ch:
            r.destroy()
        else:
            pass


for _ in range(0, 9):
    if _ < 3:
        ll = Label(master=frame2, text="o", height=2, width=4)
        ll.grid(row=_, column=0)
    elif _ < 6:
        ll = Label(master=frame2, text="o", height=2, width=4)
        ll.grid(row=_ - 3, column=1)
    elif _ < 10:
        ll = Label(master=frame2, text="o", height=2, width=4)
        ll.grid(row=_ - 6, column=2)


def win_lose_draw(lab):
    a = ["x", "x", "x"]
    b = ["o", "o", "o"]

    freq = {}
    for item in lab:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    if [lab[0], lab[1], lab[2]] == a or [lab[3], lab[4], lab[5]] == a or [lab[6], lab[7],
                                                                          lab[8]] == a:
        return 1
    elif [lab[0], lab[3], lab[6]] == a or [lab[1], lab[4], lab[7]] == a or [lab[2], lab[5],
                                                                            lab[8]] == a:
        return 1
    elif [lab[0], lab[4], lab[8]] == a or [lab[2], lab[4], lab[6]] == a:
        return 1
    elif [lab[0], lab[1], lab[2]] == b or [lab[3], lab[4], lab[5]] == b or [lab[6], lab[7],
                                                                            lab[8]] == b:
        return 2
    elif [lab[0], lab[3], lab[6]] == b or [lab[1], lab[4], lab[7]] == b or [lab[2], lab[5],
                                                                            lab[8]] == b:
        return 2
    elif [lab[0], lab[4], lab[8]] == b or [lab[2], lab[4], lab[6]] == b:
        return 2
    elif freq[" "] == 1:
        return 3
    else:
        pass


def com_choice(l):
    choice = random.choice(range(len(but)))
    print(ch)
    if but[choice] not in l and but[choice] not in ch:
        print(but[choice])
        but[choice].destroy()
        ch.append(but[choice])
        print(ch)
        print(choice)
        lab[choice] = "o"
    else:
        com_choice(l)


def clear(x, entry):
    but[x].destroy()
    if x < 3:
        label_2 = Label(master=frame2, text=entry, height=2, width=4)
        label_2.grid(row=x, column=0, sticky=E)
    elif x < 6:
        label_2 = Label(master=frame2, text=entry, height=2, width=4)
        label_2.grid(row=x - 3, column=1, sticky=E)
    elif x < 9:
        label_2 = Label(master=frame2, text=entry, height=2, width=4)
        label_2.grid(row=x - 6, column=2, sticky=E)

    pch.append(but[x])
    com_choice(pch)
    lab[x] = "x"
    print(lab)
    h = win_lose_draw(lab)
    if h == 1:
        l_w = Label(master=frame2, text="X wins", height=2, width=4)
        l_w.grid(row=5, column=0, sticky=E)
        kill()
    elif h == 2:
        l_w = Label(master=frame2, text="O wins", height=2, width=4)
        l_w.grid(row=5, column=0, sticky=E)
        kill()
    elif h == 3:
        l_w = Label(master=frame2, text="Draw", height=2, width=4)
        l_w.grid(row=5, column=0, sticky=E)
        kill()
    else:
        pass


for _ in range(0, 9):
    if _ < 3:
        btn = Button(master=frame2, height=2, width=4, command=lambda _=_: clear(_, p))
        btn.grid(row=_, column=0)
    elif _ < 6:
        btn = Button(master=frame2, height=2, width=4, command=lambda _=_: clear(_, p))
        btn.grid(row=_ - 3, column=1)
    elif _ < 10:
        btn = Button(master=frame2, height=2, width=4, command=lambda _=_: clear(_, p))
        btn.grid(row=_ - 6, column=2)

    but.append(btn)

window.mainloop()
