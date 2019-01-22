from ogame import OGame


class Bot:

    def __init__(self, server_name, user_name, password):
        self.server_name = server_name
        self.user_name = user_name
        self.password = password

        self.session = None

    def connect(self):
        self.session = OGame(self.server_name, self.user_name, self.password)
