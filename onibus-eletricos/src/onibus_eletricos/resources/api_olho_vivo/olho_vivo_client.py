from .url_builder import RequestMaker

class APIOlhoVivoClient:

    HOST='api.olhovivo.sptrans.com.br'
    METHOD='http'
    VERSION='2.1'

    def __init__(self, token:str):

        self.request = RequestMaker(self.METHOD, self.HOST, self.VERSION)
        self.token=token

        self.autenticar()

    def autenticar(self)->None:

        endpoint = 'Login/Autenticar'
        params = {'token' : self.token}

        #a api nao retorna um json valido
        resp = self.request.post(endpoint, params, as_json=False)
        success = resp=='true'
        if not success:
            raise RuntimeError(f'Falha ao atenticar: {resp}')
        print('Autenticado com sucesso.')

    @property
    def posicao_atual_onibus(self):

        endpoint = 'Posicao'
        return self.request.get(endpoint)