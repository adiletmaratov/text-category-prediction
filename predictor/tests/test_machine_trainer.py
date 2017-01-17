# coding=utf-8
from unittest import TestCase
from mock import patch

from predictor.machine_trainer import MachineTrainer


class MachineTrainerTestCase(TestCase):

    @patch('predictor.machine_trainer.MachineTrainer._retrieve_data_set')
    @patch('predictor.machine_trainer.MachineTrainer._fit_data')
    def test_should_change_is_trained_attribute_to_true(self, mock_fit, mock_dataset):
        """Если был вызван метод `train_machine`, атрибут is_trained
        должен быть переопределен в True"""
        machine_trainer = MachineTrainer()
        self.assertFalse(machine_trainer.is_trained)
        machine_trainer.train_machine()
        self.assertTrue(machine_trainer.is_trained)

    @patch('predictor.machine_trainer.MachineTrainer._retrieve_data_set')
    @patch('predictor.machine_trainer.MachineTrainer._fit_data')
    def test_data_retrieval_method_should_be_called_when_train_machine_called(self,
                                                                       mock_fit,
                                                                       mock_dataset):
        """Метод _retrieve_data_set должен быть вызван, если вызван
        метод train_machine"""
        machine_trainer = MachineTrainer()
        machine_trainer.train_machine()
        mock_dataset.assert_called_once()

    @patch('predictor.machine_trainer.MachineTrainer._retrieve_data_set')
    @patch('predictor.machine_trainer.MachineTrainer._fit_data')
    def test_fit_data_method_should_be_called_when_train_machine_called(self,
                                                                        mock_fit,
                                                                        mock_dataset):
        """Метод _retrieve_data_set должен быть вызван, если вызван
        метод train_machine"""
        machine_trainer = MachineTrainer()
        machine_trainer.train_machine()
        mock_fit.assert_called_once()


