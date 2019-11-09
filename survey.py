from tkinter import *
from tkinter import messagebox
from tkinter import ttk


root = Tk()  # создаем окно для опроса
root.title('Опрос')
root.geometry('400x800')


def question1():
    question = Label(root, text='Какие точки общественного питания Вы посещаете чаще всего?')
    prompt = Label(root, text='Введите название(я) кафе/ресторана(Например:Теремок)')
    answer = Entry()
    butt = ttk.Button(root, text='Ответить', command=lambda: no_answer(question2))
    question.grid(row=0)
    prompt.grid(row=1)
    answer.grid(row=2)
    butt.grid(row=3)

    def no_answer(question2):
        if answer.get() == '':
            messagebox.showerror('Ошибка', 'Введите ответ')
        else:
            question2()


def question2():
    question = Label(root, text='Что является наиболее важным для вас, при выборе кафе/ресторана?')
    butt1 = ttk.Button(root, text='Быстрое обслуживание', command=lambda: question3())
    butt2 = ttk.Button(root, text='Низкая цена', command=lambda: question3())
    butt3 = ttk.Button(root, text='Высокое качество продуктов', command=lambda: question3())
    question.grid(row=5)
    butt1.grid(row=6)
    butt2.grid(row=7)
    butt3.grid(row=8)


def question3():
    question = Label(root, text='Как часто Вы посещаете ресораны быстрого питания (фаст-фуд)?')
    butt1_1 = ttk.Button(root, text='Практически каждый день', command=lambda: final())
    butt2_1 = ttk.Button(root, text='Несколько раз в месяц', command=lambda: final())
    butt3_1 = ttk.Button(root, text='Раз в несколько месяцев', command=lambda: final())
    butt4_1 = ttk.Button(root, text='Не посещаю')
    question.grid(row=10)
    butt1_1.grid(row=11)
    butt2_1.grid(row=12)
    butt3_1.grid(row=13)
    butt4_1.grid(row=14)


def final():
    end = Label(root, text='Спасибо за Ваши ответы', font='Courier 20')
    end.grid(row=16)


question1()
root.mainloop()
