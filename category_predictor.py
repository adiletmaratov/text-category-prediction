from machine_trainer import MachineTrainer


class CategoryPredictor(object):
    def __init__(self):
        self._machine_trainer = MachineTrainer()

    def train_machine(self):
        self._machine_trainer.train_machine()
