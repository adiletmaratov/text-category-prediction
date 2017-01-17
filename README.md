# Классификатор текста
 
## Поднятие окружения
 * Установка системных зависимостей
 ```sh
 sudo apt-get install python3 virtualenv
 ```
 * Далее нужно создать виртуальное окружение
 ```sh
 virtualenv -p /usr/bin/python3.5 text_analytics
 ``` 
 укажите версию python соответствующую вашей. (от 3 - 3.6)
 * Теперь активируем виртуальное окружение
 ```sh
 source /path/to/newly/created/virtual/environment/bin/activate
 ```
 * Склонируйте git репозиторий в желаемую папку
 * Пройдите в папку, где расположен репозиторий
 * При активированном виртуальном окружении выполните
```sh
 python
 ```
 Номер версии python в консоли должен быть больше или равно 3
 
 
## Использование классификатора текста
Класс, который используется пользователем называется CategoryPredictor.
 


