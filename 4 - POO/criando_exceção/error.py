class TaErradoError(Exception):
    pass


class MostraError:
    raise TaErradoError('Isso não está certo! Verifique novamente.')


try:
    a = 'a'
    b = 5
    c = a + b
except TaErradoError as error:
    print(f'ERROR: {error}')
 