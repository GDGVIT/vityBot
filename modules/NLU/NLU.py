# __author__ == shubham0704

from __future__ import unicode_literals
from __future__ import absolute_import
import logging
from vityBot.modules.NLU.kw_match import kw_match
from vityBot.modules.NLU.domains import *
from vityBot.modules.NLU.best_match import best_match

import sys, os
# sys.path.insert(0, os.path.abspath('rasa_nlu'))

from vityBot.modules.NLU.rasa_nlu.converters import load_db_data

from vityBot.modules.NLU.rasa_nlu.model import Interpreter, Trainer, Metadata
from vityBot.modules.NLU.rasa_nlu.config import RasaNLUConfig
import vityBot.modules.NLU.rasa_nlu


model_config = {
    "pipeline": [
        "nlp_spacy",
        "tokenizer_spacy",
        "ner_crf",
        "ner_spacy",
        "intent_featurizer_spacy",
        "intent_classifier_sklearn"
    ],
    "language": "en"
}

model_config = model_config
config = RasaNLUConfig(cmdline_args=model_config)
logging.basicConfig(level="INFO")


class NLU:

    def __init__(self):

        self.interpreter = None
        self.trainer = Trainer(config)

    def __call__(self):
        pass

    def train(self, db_name, uri=None):

        training_data = load_db_data(db_name, uri)
        self.interpreter = self.trainer.train(training_data)

    def classify(self, sent, user):

        if self.interpreter is None:
            print("train if you got new.. using old one ")
            try:
                model_directory = self.trainer.persist('./models/')
                metadata = Metadata.load(model_directory)
                self.interpreter = Interpreter.load(metadata, config)
            except:
                raise("Need to train model. No pre-trained model found.")

        result = self.interpreter.parse(sent)
		        
        probable_module = result["intent"]['name'].split("-")
        
        isCalc = len(probable_module) - 1
        module_name = kw_match(sent)
        print(isCalc)

        if isCalc:
            print('here')
            return eval(probable_module[0])(sent, user)

        return best_match(sent, probable_module[0])
