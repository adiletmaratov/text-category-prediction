# Классификатор текста
 
## Поднятие окружения
 * Установка системных зависимостей
 
 ```
 sudo apt-get install python3 virtualenv
 ```
 
 * Далее нужно создать виртуальное окружение
 ```
 virtualenv text_analytics
 ``` 
 укажите версию python соответствующую вашей.

 * Теперь активируем виртуальное окружение
 
 ```
 source /path/to/newly/created/virtual/text_analytics/bin/activate
 ```
 
 * Склонируйте git репозиторий в желаемую папку
 
 * Пройдите в папку, где расположен репозиторий
 
 * При активированном виртуальном окружении выполните

```
 python
```
 Номер версии python в консоли должен быть больше или равен 3
 
 
## Использование классификатора текста
Есть два класса, которые нам помогут в определении категории текста. 
MachineTrainer и CategoryPredictor.

MachineTrainer - класс, который скачивает данные для обучения из сайта http://qwone.com/~jason/20Newsgroups. 
После скачивание происходит преобразование текста в векторные числа, усредняется частота встречаемых слов и используя SGDClassifier класс из библиотеки scikit, обучает машину.

CategoryPredictor - класс, который умеет определять категорию нового текста основываясь на уже существующих данных.


```python
from predictor.machine_trainer import MachineTrainer
from predictor.category_predictor import CategoryPredictor
mt = MachineTrainer()  # создание экземпляра класса для обучения
mt.train()    # обучение
cp = CategoryPredictor(mt)    #   создание экземпляра
cp.predict("god probably lives somewere in the heaven")    # определение категории предложения
```


