import tkinter


class GameItems:
    n = 0
    auto = 0
    hands = 1


def click(event):
    main_button.unbind_all('<space>')
    game.n += game.hands
    count['text'] = 'ВАШ СЧЁТ : ' + str(game.n) + '\n' + 'ВАШИ АВТОНАЖАТИЯ : ' + str(
        game.auto) + '\n' + 'У ВАС РУК : ' + str(game.hands)
    root.after(100, set_clicked)


def set_clicked():
    main_button.bind_all('<space>', click)


def purchase_auto():
    if game.n < 100:
        error_label = tkinter.Label(root, text='НЕ ХВАТАЕТ СЧЕТА ДЛЯ ПОКУПКИ', fg='red')
        error_label.place(relx=0.3, rely=0)
    else:
        error_label = tkinter.Label(root,
                                    text='                                                                        ')
        error_label.place(relx=0.3, rely=0)
        game.n -= 100
        game.auto += 1


def auto_function():
    game.n += game.auto
    count['text'] = 'ВАШ СЧЁТ : ' + str(game.n) + '\n' + 'ВАШИ АВТОНАЖАТИЯ : ' + str(
        game.auto) + '\n' + 'У ВАС РУК : ' + str(game.hands)
    root.after(1000, auto_function)


def purchase_hand():
    if game.n < 50:
        error_label = tkinter.Label(root, text='НЕ ХВАТАЕТ СЧЕТА ДЛЯ ПОКУПКИ', fg='red')
        error_label.place(relx=0.3, rely=0)
    else:
        error_label = tkinter.Label(root,
                                    text='                                                                        ')
        error_label.place(relx=0.3, rely=0)
        game.n -= 50
        game.hands += 1


root = tkinter.Tk()
root.title('КЛИКЕР')
game = GameItems()
w = 500
h = 500
x_coordinate = (root.winfo_screenwidth() - w) / 2
y_coordinate = (root.winfo_screenheight() - h) / 2
root.geometry('%dx%d+%d+%d' % (w, h, x_coordinate, y_coordinate))

main_button_photo = tkinter.PhotoImage(file='red_button.gif')
main_button = tkinter.Button(root, width=100, height=100, image=main_button_photo)
main_button.bind_all('<space>', click)
main_button.place(relx=.4, rely=.3)

main_button_label = tkinter.Label(root, text='ЖМИ НА ПРОБЕЛ', fg='purple')
main_button_label.place(relx=0.4, rely=0.25)

quit_button_photo = tkinter.PhotoImage(file='exit_button.gif')
quit_button = tkinter.Button(root, text='ВЫХОД', command=root.quit, width=50, height=25, image=quit_button_photo)
quit_button.place(relx=0, rely=0)

count = tkinter.Label(root,
                      text='ВАШ СЧЁТ : ' + str(game.n) + '\n' + 'ВАШИ АВТОНАЖАТИЯ : ' + str(
                          game.auto) + '\n' + 'У ВАС РУК : ' + str(
                          game.hands), fg='green')
count.place(relx=0.7, rely=0)

auto_upgrade_button_photo = tkinter.PhotoImage(file='blue_button.gif')
auto_upgrade_button = tkinter.Button(root, command=purchase_auto, width=100, height=100,
                                     image=auto_upgrade_button_photo)
auto_upgrade_button.place(relx=0.05, rely=0.8)

auto_upgrade_button_label = tkinter.Label(root, text='КУПИТЬ АВТОНАЖАТИЕ ЗА 100', fg='blue')
auto_upgrade_button_label.place(relx=0, rely=0.75)

auto_function()

hand_upgrade_button_photo = tkinter.PhotoImage(file='hand.gif')
hand_upgrade_button = tkinter.Button(root, command=purchase_hand, width=100, height=100,
                                     image=hand_upgrade_button_photo)
hand_upgrade_button.place(relx=0.75, rely=0.8)

hand_upgrade_button_label = tkinter.Label(root, text='КУПИТЬ РУКУ ЗА 50', fg='brown')
hand_upgrade_button_label.place(relx=0.75, rely=0.75)

root.mainloop()
