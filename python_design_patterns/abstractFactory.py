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


class SetterFactory:
    ''' Concrete Factory'''

    def get_player(self):
        return Setter("Tobio")

    def get_mood(self):
        return "Neutral/Calm"


class VolleyBallTeam:
    ''' VolleyBall houses our abstract factory'''

    def __init__(self, player_factory=None):
        ''' player_factory is our abstract factory'''
        self._player_factory = player_factory

    def show_player(self):
        player = self._player_factory.get_player()
        player_mood = self._player_factory.get_mood()
        print('Player name is {}'.format(player.name))
        print('Player position is {}'.format(player.get_position()))
        print('Player mood is {}'.format(player_mood))


factory = SetterFactory()

team = VolleyBallTeam(factory)

team.show_player()
