class LogMixin:
    @staticmethod
    def white(msg):
        with open('log.log', 'a+') as file:
            file.write(msg)
            file.write('\n')

    def log_info(self, msg):
        self.white(f'INFO: {msg}')

    def log_error(self, msg):
        self.white(f'ERROR: {msg}')


class Eletronico(LogMixin):
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            error = f'{self._nome} já está ligado!'
            print(error)
            self.log_error(error)
            return

        info = 'Ligando...'
        self.log_info(info)
        self._ligado = True

    def desligar(self):
        if self._ligado:
            info = 'Desligando...'
            self.log_info(info)
            self._ligado = False
        else:
            error = f'{self._nome} já esta desligado!'
            print(error)
            self.log_error(error)

    def status(self):
        print(self._ligado)


class SmartPhone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = 'SmartPhone está desligado!'
            self.log_error(error)
            print('SmartPhone está desligado!')
            return
        if self._conectado:
            error = 'SmartPhone já está conectado!'
            self.log_error(error)
            print('SmartPhone já está conectado!')
            return

        info = 'SmartPhome foi conectado!'
        self.log_info(info)
        print('SmartPhome foi conectado!')
        self._conectado = True

    def desconectar(self):
        if self._conectado:
            info = 'SmartPhone foi desconectado'
            self.log_info(info)
            print('SmartPhone foi desconectado')
            self._conectado = False
        else:
            error = 'SmartPhone já esta desconectado!'
            self.log_error(error)
            print('SmartPhone já esta desconectado!')
