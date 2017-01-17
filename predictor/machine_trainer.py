from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline


class MachineTrainer(object):
    def __init__(self):
        self._classifier = self._construct_classifier()
        self._is_trained = False
        self._data_set = None

    @staticmethod
    def _construct_classifier():
        return Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf',
             SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5,
                           random_state=42)),
        ])

    @property
    def classifier(self):
        return self._classifier

    @property
    def data_set(self):
        return self._data_set

    @property
    def is_trained(self):
        return self._is_trained

    def train(self):
        self._retrieve_data_set()
        self._fit_data()
        self._is_trained = True

    def _fit_data(self):
        self._classifier.fit(self._data_set.data, self._data_set.target)

    def _retrieve_data_set(self):
        self._data_set = fetch_20newsgroups(subset='train', shuffle=True)
