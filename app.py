from flask import Flask, render_template, request
import random

app = Flask(__name__)
with open('answers.txt', 'r') as file:
    answers = [line.strip().split() for line in file]

def get_random_place():
    random_place = random.choice(answers)
    return float(random_place[0]), float(random_place[1])

def get_map_url(lat, lon):
    return f'https://static-maps.yandex.ru/1.x/?ll={lon},{lat}&size=600,400&z=12&l=map&pt={lon},{lat},pm2rdm'

@app.route('/')
def home():
    lat, lon = get_random_place()
    map_url = get_map_url(lat, lon)
    saving(lat, lon, True)
    return render_template('index.html', map_url=map_url, lat=lat, lon=lon)

@app.route('/check', methods=['POST'])
def check():
    user_lat = float(request.form.get('lat'))
    user_lon = float(request.form.get('lon'))

    lat, lon = get_random_place()


    diff_lat = lat - user_lat
    diff_lon = lon - user_lon
    return f'Разница в координатах: Широта - {diff_lat}, Долгота - {diff_lon}'


if __name__ == '__main__':
    app.run(debug=True)
