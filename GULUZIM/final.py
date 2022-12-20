
citybaza = ['New York', 'London']
key = None
while True:
    x = input('''

            Выберите действие:
            1. Добавить новый город
            2. Отобразить список городов
            3. Заменить город
            4. Удалить город
            5. Выход
''')
    if x == '1':
        if key is None:
            city = input('введите город : ')
            if city not in citybaza and city.isalpha() :
                citybaza.append(city)
                print(citybaza)
                print('город добавлен ! ')
                key = city
            else :
                print('такой город уже есть в списке ')
            #проверка нa некорр название 
    if x == '2':
        print(citybaza, end="\n")

    if x == '3':
        if key is not None:
            newcity = input('введите новый город : ')
            if newcity not in citybaza:
                citybaza.remove(city)
                citybaza.append(newcity)
                print(citybaza)
            else:
                print('такой город уже свуществует ')
        
        else : 
            print('gorod otsutstvuiet ')
            True


    if x == '4':
         city = input("Какой город удалить:")
         citybaza.remove(city)
         print(citybaza)

    if x == '5':
        break
           
            
           
            
            
              

