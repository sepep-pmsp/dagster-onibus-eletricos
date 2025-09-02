from requests import Session
from typing import Optional

class RequestMaker:

    def __init__(self, method:str, host:str, version:Optional[str]=None)->None:

        self.method = method
        self.host = host
        self.version = version
        self.session = Session()

        self.url_base = self.build_base_url()

    def build_base_url(self):

        url = f'{self.method}://{self.host}'

        if self.version:
            url = url+f'/v{self.version}'

        return url

    def build_params_str(self, params:dict)->str:

        params = [f"{key}={value}" for key, value in params.items()]
        params = '&'.join(params)
        params = f'?{params}'

        return params

    def build_request_url(self, endpoint:Optional[str]=None, params:Optional[dict]=None)->str:

        url = self.url_base
        if endpoint:
            url = self.url_base + '/' + endpoint.strip('/')
        
        if params:
            params_str = self.build_params_str(params)
            url = url + params_str
        
        return url
    

    def post(self,endpoint:Optional[str]=None, params:Optional[dict]=None, data:Optional[dict]=None, as_json:bool=True)->dict:

        url = self.build_request_url(endpoint, params)
        print(f'Fazendo post em: {url}. Dados: {data}')
        with self.session.post(url, data=data) as r:
            if as_json:
                return r.json()
            return r.text
        
    def get(self, endpoint:Optional[str]=None, params:Optional[dict]=None, as_json:bool=True)->dict:

        url = self.build_request_url(endpoint, params)
        print(f'Fazendo get em {url}.')
        with self.session.get(url) as r:
            if as_json:
                return r.json()
            return r.text