from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
soup = BeautifulSoup(response.text, "html.parser")

all_movies = soup.find_all("h3", class_ = "title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("./day_41-50/day_45/movies.txt", "w", encoding="utf8") as file:
    for movie in movies:
        file.write(f"{movie}\n")