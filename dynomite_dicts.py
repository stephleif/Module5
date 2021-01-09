#dynomite_dicts
"""
in the third file, called dynomite_dicts.py do the following:

Create an empty dictionary called pokedex.
Add the following key, value pairs to the dictionary:
  'Venosaur': ['Grass', 'Poisen']
  'Charizard': ['Fire', 'Flying']
  'Blastoise': ['Water']

 

Remove 'Blastoise' from the dictionary.
"""
if __name__ == "__main__":
    pokedex = dict()
    #pokemon_types['Squirtle'] = 'water'
    pokedex['Venosaur'] = ['Grass', 'Poisen']
    pokedex['Charizard'] = ['Fire', 'Flying']
    pokedex['Blastoise'] = ['Water']
    #del pokemon_types['squirtel']
    del pokedex['Blastoise']
    print(pokedex)
    print("All done dynomite_dicts!")
