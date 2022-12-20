#2

users = {
    'Guluzim':{
        'login': 'Guluzim',
        'password':'12345'
} }

key = None
while True:
    x = input(''' выберите действие :  
1 РЕГИСТРАЦИЯ
2 ВХОД
3 СПИСОК 
4 ВЫХОД
 ''')
    if x == '1':
        if key is None:
            login = input(' login : ')
            password = input('passeord: ')
            users.setdefault (login) 
            users.update({
                                login : {
                                    'login': login,
                                    'password': password
                                }
            })

    elif x == '2':
        if key is None:
            login = input(' login : ')
            password = input('password: ')
            if login in users.keys():
                if password == users[login]['password']:
                    key = login
                    print(f'ДОБРО ПОЖАЛОВАТЬ ! {login}')
                else : 
                    print('Данные введены неправильно!, попробуйте еще раз ')
                    True
    elif x == '3':
        print(users.keys())
    elif x == '4':
        print(f'всего хорошего {login}')
        

