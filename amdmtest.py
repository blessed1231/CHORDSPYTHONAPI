from main import AmDm
import json 

chords = AmDm.get_chords_list(AmDm, 'сплин танцуй')
 

print(json.dumps(chords[0], indent=4))
song = AmDm.get_chords_song(AmDm, 'http://amdm.ru/akkordi/splin/102024/tancuy/')
print(song)