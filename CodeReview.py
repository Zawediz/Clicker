from tkinter import *

n = 0
auto = 0
hands = 1


def click(event):
    global n
    n += hands
    count['text'] = 'ВАШ СЧЁТ : ' + str(n) + '\n' + 'ВАШИ АВТОНАЖАТИЯ : ' + str(auto) + '\n' + 'У ВАС РУК : ' + str(
        hands)


def PurchaseAuto():
    global n
    global auto
    if n < 100:
        ErrorLabel = Label(root, text='НЕ ХВАТАЕТ СЧЕТА ДЛЯ ПОКУПКИ', fg='red')
        ErrorLabel.place(relx=0.3, rely=0)
    else:
        ErrorLabel = Label(root,
                           text='                                                                        ')
        ErrorLabel.place(relx=0.3, rely=0)
        n -= 100
        auto += 1


def Auto():
    global n
    global auto
    n += auto
    count['text'] = 'ВАШ СЧЁТ : ' + str(n) + '\n' + 'ВАШИ АВТОНАЖАТИЯ : ' + str(auto) + '\n' + 'У ВАС РУК : ' + str(
        hands)
    root.after(1000, Auto)


def PurchaseHand():
    global n
    global hands
    if n < 50:
        ErrorLabel = Label(root, text='НЕ ХВАТАЕТ СЧЕТА ДЛЯ ПОКУПКИ', fg='red')
        ErrorLabel.place(relx=0.3, rely=0)
    else:
        ErrorLabel = Label(root,
                           text='                                                                        ')
        ErrorLabel.place(relx=0.3, rely=0)
        n -= 50
        hands += 1


root = Tk()
root.title('КЛИКЕР')
w = 500
h = 500
XCoordinate = (root.winfo_screenwidth() - w) / 2
YCoordinate = (root.winfo_screenheight() - h) / 2
root.geometry('%dx%d+%d+%d' % (w, h, XCoordinate, YCoordinate))

MainButtonPhoto = PhotoImage(file='red_button.gif')
MainButton = Button(root, width=100, height=100, image=MainButtonPhoto)
MainButton.bind_all('<space>', click)
MainButton.place(relx=.4, rely=.3)

MainButtonLabel = Label(root, text='ЖМИ НА ПРОБЕЛ', fg='purple')
MainButtonLabel.place(relx=0.4, rely=0.25)

QuitButtonPhoto = PhotoImage(file='exit_button.gif')
QuitButton = Button(root, text='ВЫХОД', command=root.quit, width=50, height=25, image=QuitButtonPhoto)
QuitButton.place(relx=0, rely=0)

count = Label(root,
              text='ВАШ СЧЁТ : ' + str(n) + '\n' + 'ВАШИ АВТОНАЖАТИЯ : ' + str(auto) + '\n' + 'У ВАС РУК : ' + str(
                  hands), fg='green')
count.place(relx=0.7, rely=0)

AutoUpgradeButtonPhoto = PhotoImage(file='blue_button.gif')
AutoUpgradeButton = Button(root, command=PurchaseAuto, width=100, height=100, image=AutoUpgradeButtonPhoto)
AutoUpgradeButton.place(relx=0.05, rely=0.8)

AutoUpgradeButtonLabel = Label(root, text='КУПИТЬ АВТОНАЖАТИЕ ЗА 100', fg='blue')
AutoUpgradeButtonLabel.place(relx=0, rely=0.75)

Auto()

HandUpgradeButtonPhoto = PhotoImage(file='hand.gif')
HandUpgradeButton = Button(root, command=PurchaseHand, width=100, height=100, image=HandUpgradeButtonPhoto)
HandUpgradeButton.place(relx=0.75, rely=0.8)

HandUpgradeButtonLabel = Label(root, text='КУПИТЬ РУКУ ЗА 50', fg='brown')
HandUpgradeButtonLabel.place(relx=0.75, rely=0.75)

root.mainloop()
