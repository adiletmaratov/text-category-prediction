from .machine_trainer import MachineTrainer


class CategoryPredictor(object):
    def __init__(self):
        self._machine_trainer = MachineTrainer()

    def train_machine(self):
        self._machine_trainer.train()

    def predict_category(self, user_input):
        user_input = [user_input]
        predicted = self._machine_trainer.classifier.predict(user_input)
        self._print_results(user_input, predicted)

    def _print_results(self, user_input, predicted):
        for new_sentence, category in zip(user_input, predicted):
            result = "{} => {}".format(new_sentence,
                                       self._machine_trainer.data_set.target_names[category])
            print(result)
