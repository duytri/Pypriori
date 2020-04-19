# coding: utf-8

class Rule(object):
    def __init__(self, antecedent, consequent, supp, conf):
        self.antecedent = antecedent
        self.consequent = consequent
        self.supp = supp
        self.conf = conf

    def __repr__(self):
        return '{}: {} ==> {} [{}, {}]'.format(
            type(self).__name__, self.antecedent,
            self.consequent, self.supp, self.conf
        )