import spotipy
from collections import Counter
from spotipy.oauth2 import SpotifyOAuth

import os
from dotenv import load_dotenv

os.system('cls')

music= []
artista = []
artista_id = []
generos = []

load_dotenv()
Spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("CLIENT_ID"),##YOUR KEY CLIENT ID,
    client_secret=os.getenv("CLIENT_SECRET"),##YOUR KEY CLIENT SECRET,
    redirect_uri="http://localhost:8888/callback",
    scope="playlist-read-private playlist-read-collaborative user-read-recently-played",
    cache_path=".cache-spotify"  # Desativa o cache
))


def buscar_music(generos, limite=5):
    for genero in generos:
        print(f'\nRecomendações para o gênero: {genero}')
        res = Spotify.search(q=f'genre:{genero}', type='track', limit=limite)
        
        for idx, item in enumerate(res['tracks']['items']):
            nome = item['name']
            artista = item['artists'][0]['name']
            print(f'{nome} - {artista}')

def buscar_artista_id(nome_artista):
    resultado = Spotify.search(q=nome_artista, type='artist', limit=1)
    if resultado['artists']['items']:
        artista = resultado['artists']['items'][0]
        artista_id.append(artista['id'])

# Função para obter as últimas músicas
def get_recent_tracks(limit=25):
    recent_tracks = Spotify.current_user_recently_played(limit=limit)
    tracks = []
    for item in recent_tracks['items']:
        track = item['track']
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        artist_id = track['artists'][0]['id']

        artista_info = Spotify.artist(artist_id)
        artista_genr = artista_info['genres']

        artista.append(artist_name)
        print(f"Música: {track_name} - Artista: {artist_name} - Gêneros: {', '.join(artista_genr) if artista_genr else 'Nenhum gênero disponível'}")
        
    return {'items': tracks}

#mostrar as ultimas musicas
print('\nSuas últimas músicas ouvidas no Spotify:')
recent_tracks = get_recent_tracks() 
for i in artista: buscar_artista_id(i)

generos = []
for i in artista_id:
    arts = Spotify.artist(i)
    generos.extend(arts['genres'])

print('\n')

contagem = Counter(generos)
contagemArtista = Counter(artista)

topArtista = contagemArtista.most_common(3)
top_generos = contagem.most_common(3)  # Lista de tuplas (gênero, frequência)

print('\nCantores e gêneros das suas últimas músicas (ordenados por frequência):')
print('top generos')
for genero, frequencia in top_generos:
    print(f'- {genero} (aparece {frequencia} vezes)')
print('\ntop cantores')
for artista, num in topArtista:
    print(f'- {artista} (aparece {num} vezes)')

# Para usar nas recomendações (apenas os nomes dos gêneros)
generos_recomendacao = [genero for genero, freq in top_generos]

print('\nmusicas: ')
for genero in generos_recomendacao:
    res = Spotify.search(q=f'genre:{genero}', type='track', limit=7)
    for idx, item in enumerate(res['tracks']['items']):
        nome = item['name']
        artista = item['artists'][0]['name']
        if nome not in music:
            music.append(nome)
            print(f'\n{nome} by {artista}')