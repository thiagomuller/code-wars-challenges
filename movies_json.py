#This is a code for training python with json files

class Movies_json:
    def __init__(self , name = "" , year = 0 , director = "" , main_actor = "", studio = ""):
        self.__name = name
        self.__year = year
        self.__director = director
        self.__main_actor = main_actor
        self.__studio = studio

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
        return self.__name

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self,value):
        self.__year = value
        return self.__year

    @property
    def director(self):
        return self.__director
    @director.setter
    def director(self,value):
        self.__director = value
        return self.__director

    @property
    def main_actor(self):
        return self.__main_actor
    @main_actor.setter
    def main_actor(self,value):
        self.__main_actor = value
        return self.__main_actor

    @property
    def studio(self):
        return self.__studio
    @studio.setter
    def studio(self,value):
        self.__studio = value
        return self.__studio


