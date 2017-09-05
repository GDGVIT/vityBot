# __author__ == shubham0704

from __future__ import unicode_literals
import logging
from kw_match import kw_match
from domains import *
from best_match import best_match

import sys, os
sys.path.insert(0, os.path.abspath('rasa_nlu'))

from rasa_nlu.converters import load_db_data

from rasa_nlu.model import Interpreter, Trainer, Metadata
from rasa_nlu.config import RasaNLUConfig
import rasa_nlu


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
            print "train if you got new.. using old one "
            try:
                model_directory = self.trainer.persist('./models/')
                metadata = Metadata.load(model_directory)
                self.interpreter = Interpreter.load(metadata, config)
            except:
                raise("Need to train model. No pre-trained model found.")

        result = self.interpreter.parse(sent.decode('utf-8'))
		        
        probable_module = result["intent"]['name'].split("-")
        
        isCalc = len(probable_module) - 1
        module_name = kw_match(sent)

        if isCalc:
            return eval(probable_module[0])(sent, user)
    
	#return best_match(probable_module[0], sent)
        return best_match(sent)
