from flask import Flask, render_template, request
import random
import sqlite3

app = Flask(__name__)
con = sqlite3.connect('MyBD.sqlite')
cur = con.cursor()
records = cur.execute("""SELECT * from map""").fetchall()
answers = []
for i in records:
    answers.append(i)


def get_random_place():
    random_place = random.choice(answers)
    return float(random_place[0]), float(random_place[1])


def get_map_url(lat, lon):
    return f'https://static-maps.yandex.ru/1.x/?ll={lon},{lat}&size=600,400&z=12&l=map&pt={lon},{lat},pm2rdm'


def test(lat, lon):
    if abs(lon) > 180 or abs(lat) > 90:
        return 'error'


@app.route('/')
def home():
    lon, lat = get_random_place()
    map_url = get_map_url(lat, lon)
    return render_template('index.html', map_url=map_url, lat=lat, lon=lon)


@app.route('/check', methods=['POST'])
def check():
    user_lat = float(request.form.get('lat'))
    user_lon = float(request.form.get('lon'))

    lat, lon = get_random_place()

    diff_lat = lat - user_lat
    diff_lon = lon - user_lon
    if test(user_lat, user_lon) == 'error':
        return f'Пожалуйста введите корректные значения долготы и широты'
    elif diff_lat < 5 and diff_lon < 5:
        return f'Отличие между правильными координатами и вашим ответом меньше десяти. Так держать!'
    return f'Разница в координатах: Широта - {diff_lat}, Долгота - {diff_lon}'


if __name__ == '__main__':
    app.run(debug=True)
