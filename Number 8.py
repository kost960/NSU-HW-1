login = input("Введите ваш логин:")
password = input("Введите ваш пароль:")
print("Login:", login)
print("Password:", password)

new_password = password.replace(password, input("Введите новый пароль:"))

print("Login:", login)
print("New password:", new_password)