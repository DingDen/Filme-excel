import csv, imdb

ia = imdb.IMDb()

cod = [20880628, 10872600,  9419884, 7131622] #35011632, esse código estava dando erro na execução.
colums = ['imdbID', 'title', 'year', 'genres', 'kind']

movies = []
for i in cod:
    L1 = []
    code = f'{i}'
    series = ia.get_movie(code)
    for j in range(len(cod)):
        L1.append(series.data[colums[j]])
    movies.append(L1)

with open('FILMES.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(colums)
    write.writerows(movies)