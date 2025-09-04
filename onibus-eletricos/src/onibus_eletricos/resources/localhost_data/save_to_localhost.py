import os
import json
from ..env_variables import LOCALHOST_DATAFOLDER

class LocalhostDataSaver:


    def __init__(self):

        self.folder = self.__solve_data_folder()

    def __solve_data_folder(self)->str:
        if not os.path.exists(LOCALHOST_DATAFOLDER):
            print(f'Creating data folder at: {LOCALHOST_DATAFOLDER}')
            os.makedirs(LOCALHOST_DATAFOLDER)
        return os.path.abspath(LOCALHOST_DATAFOLDER)
    
    
    def save_json(self, data:dict, filename:str)->None:
        filepath = os.path.join(self.folder, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_json(self, filename:str)->dict:
        filepath = os.path.join(self.folder, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
