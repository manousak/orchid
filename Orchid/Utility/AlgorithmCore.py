from abc import ABCMeta, abstractmethod

class AlgorithmCore:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def pre_process(self): pass
    
    @abstractmethod
    def run(self): pass
    
    @abstractmethod
    def post_process(self): pass
