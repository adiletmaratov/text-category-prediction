# Классификатор текста
 
## Поднятие окружения
 * Установка системных зависимостей
 
 ```
 sudo apt-get install python virtualenv
 ```
 
 * Далее нужно создать виртуальное окружение
 ```
 virtualenv text_analytics
 ``` 

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
 Номер версии python в консоли должен быть 2.7
 
 
## Использование классификатора текста
Есть два класса, которые нам помогут в определении категории текста. 
MachineTrainer и CategoryPredictor.

MachineTrainer - класс, который скачивает данные для обучения из сайта http://qwone.com/~jason/20Newsgroups. 
После скачивание происходит преобразование текста в векторные числа, усредняется частота встречаемых слов и используя SGDClassifier класс из библиотеки scikit, обучает машину.

CategoryPredictor - класс, который умеет определять категорию нового текста основываясь на уже существующих данных.

Внимание! Так как данные для обучения были на английском языке, ожидается, что новые входные данные будут тоже на английском языке. Используйте английский язык для определения категории.

Категории, выбирает CategoryPredictor класс.
* comp.graphics
* comp.os.ms-windows.misc
* comp.sys.ibm.pc.hardware
* comp.sys.mac.hardware
* comp.windows.x	rec.autos
* rec.motorcycles
* rec.sport.baseball
* rec.sport.hockey	sci.crypt
* sci.electronics
* sci.med
* sci.space
* misc.forsale	talk.politics.misc
* talk.politics.guns
* talk.politics.mideast	talk.religion.misc
* alt.atheism
* soc.religion.christian

```python
from predictor.machine_trainer import MachineTrainer
from predictor.category_predictor import CategoryPredictor
mt = MachineTrainer()  # создание экземпляра класса для обучения
mt.train()    # обучение
cp = CategoryPredictor(mt)    #   создание экземпляра
cp.predict("god probably lives somewere in the heaven")    # определение категории предложения

# >>> god probably lives somewere in the heaven => soc.religion.christian
```



