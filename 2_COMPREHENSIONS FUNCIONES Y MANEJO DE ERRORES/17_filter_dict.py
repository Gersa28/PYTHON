# Lista de diccionarios que representa los partidos y sus resultados
matches = [
    {
        'home_team': 'Bolivia',
        'away_team': 'Uruguay',
        'home_team_score': 3,
        'away_team_score': 1,
        'home_team_result': 'Win'
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Mexico',
        'home_team_score': 1,
        'away_team_score': 1,
        'home_team_result': 'Draw'
    },
    {
        'home_team': 'Ecuador',
        'away_team': 'Venezuela',
        'home_team_score': 5,
        'away_team_score': 0,
        'home_team_result': 'Win'
    },
]

# Imprimimos la lista de partidos y su longitud
print("Lista de partidos:", matches)
print("Cantidad de partidos:", len(matches))

# Filtramos los partidos en los que el equipo local ganó
new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))

# Imprimimos la nueva lista de partidos filtrados y su longitud
print("Nueva lista de partidos (solo victorias locales):", new_list)
print("Cantidad de partidos con victoria local:", len(new_list))

# Imprimimos nuevamente la lista original de partidos y su longitud
print("Lista original de partidos:", matches)
print("Cantidad de partidos en la lista original:", len(matches))
