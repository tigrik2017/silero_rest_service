import os
import torch

class Config:
    _instance = None
    _device = torch.device('cpu')
    _model = None
    _currentModel = None
    _generationsRoot = 'output'
    _modelsRoot = 'models'

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        
        if not os.path.isdir(f'{cls._modelsRoot}'):
            os.mkdir(f'{cls._modelsRoot}', mode = 0o777)
        
        if not os.path.isdir(f'{cls._generationsRoot}'):
            os.mkdir(f'{cls._generationsRoot}', mode = 0o777)
            
        return cls._instance

    @property
    def device(self):
        return self._device

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def current_model(self):
        return self._currentModel

    @current_model.setter
    def current_model(self, value):
        self._currentModel = value

    @property
    def generations_root(self):
        return self._generationsRoot

    @generations_root.setter
    def generations_root(self, value):
        self._generationsRoot = value

    @property
    def models_root(self):
        return self._modelsRoot

    @models_root.setter
    def models_root(self, value):
        self._modelsRoot = value
