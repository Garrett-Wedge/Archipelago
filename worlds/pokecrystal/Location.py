
from BaseClasses import Location
#from Data import LoadLocationData


class PokemonCrystalLocation(Location):
    game: str = "Pokemon Crystal"

    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name = '', code = None, parent = None):
        super(PokemonCrystalLocation, self).__init__(player, name, code, parent)
        self.event = code is None

        #data = LoadLocationData.LoadDataFromFolder("Data")

        #print( data )