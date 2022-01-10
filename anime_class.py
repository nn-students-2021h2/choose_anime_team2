from user_class import User  # will need when we'll take user's data into consideration


class Anime:
    def __init__(self, setting, genre):
        self.setting = setting
        self.genre = genre

    def choose_anime(self):
        """
        Accesses the database and selects anime based on user preferences
        :return: the name of chosen anime
        """
        pass
