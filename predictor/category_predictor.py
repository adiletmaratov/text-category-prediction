# coding=utf-8
class CategoryPredictor(object):
    """Класс определяет категорию предложения после обучения данными из
    http://qwone.com/~jason/20Newsgroups/ """
    def __init__(self, machine_trainer):
        self._machine_trainer = machine_trainer
        self._classifier = machine_trainer.classifier

    def predict(self, user_input):
        user_input = [user_input]
        predicted = self._classifier.predict(user_input)
        self._print_results(user_input, predicted)

    def _print_results(self, user_input, predicted):
        for new_sentence, category in zip(user_input, predicted):
            result = "{} => {}".format(new_sentence,
                                       self._machine_trainer.data_set.target_names[category])
            print(result)
