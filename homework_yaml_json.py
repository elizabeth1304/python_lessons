import json
from pprint import pprint

import yaml


class Painters:
    def __init__(self, *args):
        self.fullname, self.nationality, self.genre, self.artist = args

    def __str__(self):
        return f"{self.fullname} is an {self.nationality} artist from the {self.genre}. {self.fullname} was a {self.artist}."


painter_1 = Painters("Rafaël", "Italian", "high Renaissance", "portrait painter")
painter_2 = Painters("Michelangelo di Lodovico Buonarroti Simoni", "Italian", "Italian Renaissance", "painter, sculptor, architect and poet")
print(painter_1)
print(painter_2)

data = {"items":
        [{"name": painter_1.fullname,
          "nationality": painter_1.nationality,
          "genre": painter_1.genre,
          "artist": painter_1.artist,
          "worldwide_known": True,
          "paintings": ["https://onlinegallery.art/images/blog/2015-01-Selfportrait_of_Raffaelo_Uffizi_Florence.jpg", "https://nyblog.ru/wp-content/uploads/2021/01/kto-takoy-rafael-santi-foto-1.jpg"],
          "paintings_names": ['Self Portrait', "Angels or Cherubs"]},
        {"name": painter_2.fullname,
          "nationality": painter_2.nationality,
          "genre": painter_2.genre,
          "artist": painter_2.artist,
          "worldwide_known": True,
          "paintings": ["https://upload.wikimedia.org/wikipedia/commons/5/5b/Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg", "https://upload.wikimedia.org/wikipedia/commons/4/44/Michelangelo_piet%C3%A0_rondanini.jpg"],
          "paintings_names": ['The Creation of Adam ', "Rondanini Pietà"]}]
        }

with open("painters.yml", "w") as yaml_file:
    yaml.dump(data, yaml_file, sort_keys = False)

with open("painters.yml", "r") as o:
    data_2 = yaml.safe_load(o)
    pprint(data_2)

with open("painters_json", "w") as json_file:
    json.dump(data_2, json_file, indent=4)

with open("painters.txt", "w") as text_file:
    text_file.write(str(data_2))


