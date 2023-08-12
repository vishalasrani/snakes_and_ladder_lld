class Player:

    id = 1

    def __init__(self, name, email_id):
        self.player_id = Player.id
        Player.id += 1
        self.name = name
        self.email_id = email_id
        self.current_position = 0

    def set_current_position(self, position):
        self.current_position = position
        return

    def get_current_position(self):
        return self.current_position
    