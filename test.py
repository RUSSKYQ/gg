from tkinter import *

root1 = Tk()
root1.title("Тестирование для пятых классов")
root1.geometry("1260x768")
root1.resizable(width=False, height=False)

c = Canvas(root1, width=1260, height=768, bg="#f5f5f5")
c.pack()

name = StringVar()
surname = StringVar()
klass = StringVar()


surname_label = Label(text="Введите фамилию:", bg="#f5f5f5", font="Calibri 12")
name_label = Label(text="Введите имя:", bg="#f5f5f5", font="Calibri 12")
klass_label = Label(text="Введите класс:", bg="#f5f5f5", font="Calibri 12")

surname_label.place(x=5, y=5)
name_label.place(x=355, y=5)
klass_label.place(x=658, y=5)

surname_entry = Entry(textvariable=surname)
name_entry = Entry(textvariable=name)
klass_entry = Entry(textvariable=klass)

surname_entry.place(x=177, y=7)
name_entry.place(x=480, y=7)
klass_entry.place(x=794, y=7)

label000 = Label(text="Если ситуация совершенно не кажется вам неприятной, то поставьте — 0.", font="Calibri 9", bg="#f5f5f5")
label000.place(x=5, y=70)
label001 = Label(text="Если она немного волнует, беспокоит — 1.", font="Calibri 9", bg="#f5f5f5")
label001.place(x=5, y=100)
label002 = Label(text="Если ситуация достаточно неприятна и вы хотите избежать её, то поставьте — 2.", font="Calibri 9", bg="#f5f5f5")
label002.place(x=5, y=130)
label003 = Label(text="Если ситуация неприятна, вызывает беспокойство, тревогу, страх — 3. ", font="Calibri 9", bg="#f5f5f5")
label003.place(x=5, y=160)
label004 = Label(text="А если ситуация крайне неприятна, вызывает очень сильный страх — 4. ", font="Calibri 9", bg="#f5f5f5")
label004.place(x=5, y=190)




label01 = Label(text="1.Участвовать в конкурсах, соревнованиях, олимпиадах.", font="Calibri 10", bg="#f5f5f5")
label01.place(x=5, y=250)


btn0100 = Checkbutton(text="0", background="#E0FFFF", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0100.place(x=910, y=240)

btn0101 = Checkbutton(text="1", background="#9ACD32", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0101.place(x=970, y=240)

btn0102 = Checkbutton(text="2", background="#FFA500", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0102.place(x=1030, y=240)

btn0103 = Checkbutton(text="3", background="#FF6347", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0103.place(x=1090, y=240)

btn0104 = Checkbutton(text="4", background="#A52A2A", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0104.place(x=1150, y=240)




label02 = Label(text="2.Думать о своём будущем.", font="Calibri 11", bg="#f5f5f5")
label02.place(x=5, y=300)

btn0200 = Checkbutton(text="0", background="#E0FFFF", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0200.place(x=910, y=290)

btn0201 = Checkbutton(text="1", background="#9ACD32", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0201.place(x=970, y=290)

btn0202 = Checkbutton(text="2", background="#FFA500", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0202.place(x=1030, y=290)

btn0203 = Checkbutton(text="3", background="#FF6347", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0203.place(x=1090, y=290)

btn0204 = Checkbutton(text="4", background="#A52A2A", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0204.place(x=1150, y=290)




label03 = Label(text="3.У тебя что-то не получается.", font="Calibri 11", bg="#f5f5f5")
label03.place(x=5, y=350)

btn0300 = Checkbutton(text="0", background="#E0FFFF", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0300.place(x=910, y=340)

btn0301 = Checkbutton(text="1", background="#9ACD32", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0301.place(x=970, y=340)

btn0302 = Checkbutton(text="2", background="#FFA500", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0302.place(x=1030, y=340)

btn0303 = Checkbutton(text="3", background="#FF6347", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0303.place(x=1090, y=340)

btn0304 = Checkbutton(text="4", background="#A52A2A", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0304.place(x=1150, y=340)




label04 = Label(text="4.Тебе грозит неудача, провал.", font="Calibri 11", bg="#f5f5f5")
label04.place(x=5, y=400)

btn0400 = Checkbutton(text="0", background="#E0FFFF", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0400.place(x=910, y=390)

btn0401 = Checkbutton(text="1", background="#9ACD32", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0401.place(x=970, y=390)

btn0402 = Checkbutton(text="2", background="#FFA500", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0402.place(x=1030, y=390)

btn0403 = Checkbutton(text="3", background="#FF6347", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0403.place(x=1090, y=390)

btn0404 = Checkbutton(text="4", background="#A52A2A", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0404.place(x=1150, y=390)




label05 = Label(text="5.Тебе предстоит важное, решающее дело.", font="Calibri 11", bg="#f5f5f5")
label05.place(x=5, y=450)

btn0500 = Checkbutton(text="0", background="#E0FFFF", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0500.place(x=910, y=440)

btn0501 = Checkbutton(text="1", background="#9ACD32", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0501.place(x=970, y=440)

btn0502 = Checkbutton(text="2", background="#FFA500", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0502.place(x=1030, y=440)

btn0503 = Checkbutton(text="3", background="#FF6347", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0503.place(x=1090, y=440)

btn0504 = Checkbutton(text="4", background="#A52A2A", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0504.place(x=1150, y=440)




label06 = Label(text="6.Сравниваешь себя с другими.", font="Calibri 11", bg="#f5f5f5")
label06.place(x=5, y=500)

btn0600 = Checkbutton(text="0", background="#E0FFFF", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0600.place(x=910, y=490)

btn0601 = Checkbutton(text="1", background="#9ACD32", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0601.place(x=970, y=490)

btn0602 = Checkbutton(text="2", background="#FFA500", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0602.place(x=1030, y=490)

btn0603 = Checkbutton(text="3", background="#FF6347", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0603.place(x=1090, y=490)

btn0604 = Checkbutton(text="4", background="#A52A2A", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0604.place(x=1150, y=490)




label07 = Label(text="7.Проверяются твои способности.", font="Calibri 11", bg="#f5f5f5")
label07.place(x=5, y=550)

btn0700 = Checkbutton(text="0", background="#E0FFFF", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0700.place(x=910, y=540)

btn0701 = Checkbutton(text="1", background="#9ACD32", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0701.place(x=970, y=540)

btn0702 = Checkbutton(text="2", background="#FFA500", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0702.place(x=1030, y=540)

btn0703 = Checkbutton(text="3", background="#FF6347", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0703.place(x=1090, y=540)

btn0704 = Checkbutton(text="4", background="#A52A2A", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0704.place(x=1150, y=540)




label08 = Label(text="8.Оценивается твоя работа.)", font="Calibri 11", bg="#f5f5f5")
label08.place(x=5, y=600)

btn0800 = Checkbutton(text="0", background="#E0FFFF", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0800.place(x=910, y=590)

btn0801 = Checkbutton(text="1", background="#9ACD32", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0801.place(x=970, y=590)

btn0802 = Checkbutton(text="2", background="#FFA500", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0802.place(x=1030, y=590)

btn0803 = Checkbutton(text="3", background="#FF6347", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0803.place(x=1090, y=590)

btn0804 = Checkbutton(text="4", background="#A52A2A", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0804.place(x=1150, y=590)





label09 = Label(text="9.Думаешь о своих делах.", font="Calibri 11", bg="#f5f5f5")
label09.place(x=5, y=650)

btn0900 = Checkbutton(text="0", background="#E0FFFF", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0900.place(x=910, y=640)

btn0901 = Checkbutton(text="1", background="#9ACD32", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0901.place(x=970, y=640)

btn0902 = Checkbutton(text="2", background="#FFA500", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0902.place(x=1030, y=640)

btn0903 = Checkbutton(text="3", background="#FF6347", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0903.place(x=1090, y=640)

btn0904 = Checkbutton(text="4", background="#A52A2A", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn0904.place(x=1150, y=640)





label10 = Label(text="10.Тебе надо принять для себя решение.", font="Calibri 11", bg="#f5f5f5")
label10.place(x=5, y=700)

btn1000 = Checkbutton(text="0", background="#E0FFFF", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn1000.place(x=910, y=690)

btn1001 = Checkbutton(text="1", background="#9ACD32", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn1001.place(x=970, y=690)

btn1002 = Checkbutton(text="2", background="#FFA500", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn1002.place(x=1030, y=690)

btn1003 = Checkbutton(text="3", background="#FF6347", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn1003.place(x=1090, y=690)

btn1004 = Checkbutton(text="4", background="#A52A2A", foreground="#000000", font="12", width=5, height=2, indicatoron=0)
btn1004.place(x=1150, y=690)


root1.mainloop()


