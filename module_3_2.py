def send_email(message, receiver, sender = "university.help@gmail.com"):

    if "@" not in receiver or ".com" not in receiver and ".ru" not in receiver and ".net" not in receiver and "@" not in sender or ".com" not in sender and ".ru" not in sender and ".net" not in sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {receiver}")

    elif receiver == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {receiver}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {receiver}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
