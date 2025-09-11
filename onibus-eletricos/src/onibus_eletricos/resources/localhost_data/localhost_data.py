import os
import json
from typing import Literal
from ..env_variables import LOCALHOST_DATAFOLDER

class LocalhostData:


    def __init__(self, tier:Literal['raw', 'bronze', 'silver', 'gold']):

        self.base_folder = self.__solve_data_folder()
        if tier not in ('raw', 'bronze', 'silver', 'gold'):
            raise ValueError(f"Invalid tier: {tier}. Must be one of ('raw', 'bronze', 'silver', 'gold').")
        self.tier = tier

        self.folder = self.__solve_tier_folder()

    def __solve_data_folder(self)->str:
        if not os.path.exists(LOCALHOST_DATAFOLDER):
            print(f'Creating data folder at: {LOCALHOST_DATAFOLDER}')
            os.makedirs(LOCALHOST_DATAFOLDER)
        return os.path.abspath(LOCALHOST_DATAFOLDER)
    
    def __solve_tier_folder(self):

        tier_folder = os.path.join(self.base_folder, self.tier)
        if not os.path.exists(tier_folder):
            os.makedirs(tier_folder)
        
        return os.path.abspath(tier_folder)
    
    
    def save_json(self, data:dict, filename:str)->None:
        filepath = os.path.join(self.folder, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_json(self, filename:str)->dict:
        filepath = os.path.join(self.folder, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
        
