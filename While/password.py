# На каждой отдельной строчке пользователь вводит друг за другом пароли в виде строки символов. Валидными паролями будем считать строки, у которых длина варьируется от 5 до 9 символов включительно. Как только вы встретите первый невалидный пароль, ваша программа должна закончить считывать пароли и вывести последний введенный валидный пароль.
# Гарантируется, что первый пароль всегда валидный

prevPass = ''
while True:
    password = input()
    if len(password) > 9 or len(password) < 5:
        break
    else:
        prevPass = password
        
print(prevPass)
