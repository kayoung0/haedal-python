import bs4
import requests
import datetime
import csv

headers ={
  'User-Agent': 'Not_Crawling X)'
}

response = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn', headers=headers).text
soup = bs4.BeautifulSoup(response, 'html.parser')
movies = soup.select('.tit3')

now = datetime.datetime.now()

for movie in movies:
    print(movie.select_one('a').text)

with open("movie_rank.csv",'w',newline='') as r:
    wr = csv.writer(r)
    wr.writerow([f'{now} 기준 네이버 영화 랭킹'])
    wr.writerow(['rank','name'])
    for i in range(50):
        wr.writerow([i+1,movies[i].select_one('a').text])