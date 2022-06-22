import lyricsgenius as lg
import json
from controllers.env_config import GENIUS_TOKEN


class Genius:
    def __init__(self):
        """Iniciar Classe Genius"""
        self.ACCESS_TOKEN = GENIUS_TOKEN
        self.genius = lg.Genius(self.ACCESS_TOKEN,  # Token de acesso do cliente da página da API Genius Client
                                skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"])

    def get_lyrics(self, name, k):
        """ função para obter dados do artista."""
        try:
            # Buscar as 10 musicas mais populares do artista
            artist = self.genius.search_artist(name, max_songs=k, sort='popularity', per_page=10)
            #Musicas do artista
            artist_songs = artist.songs
            #Salvar titulo das musicas numa lista
            artist_songs_title = [song.title for song in artist_songs]
            return artist_songs_title

        except:
            print(f"Não foi possível encontrar as muśicas do artista: {name}")


if __name__ == '__main__':
    g = Genius()
    v = g.get_lyrics('Marilia Mensonsa', 10)
    print(v)
