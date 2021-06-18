class Setter:
    '''
    A class to represent setter in volleyball
    '''

    def __init__(self, name):
        self.name = name

    def get_position(self):
        return 'Setter'

    def common_saying(self):
        return 'So long as I\'m here, you will be the strongest.'


class Libero:
    '''
    A class to represent libero in volleyball
    '''

    def __init__(self, name):
        self.name = name

    def get_position(self):
        return 'Libero'

    def common_saying(self):
        return 'Rolling... Thunder... Again. That was perfect.'


def get_player(player='setter'):
    ''' 
    The factory method
    '''

    players = dict(setter=Setter('Tobio'), libero=Libero('Nishinoya'))

    return players[player]


spiker = get_player()
libero = get_player('libero')
print(spiker.common_saying())
print(libero.common_saying())
