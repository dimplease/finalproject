from flask import Flask, render_template, request
import random

app = Flask(__name__)
@app.route('/')
def home():
    lat = str(random.randint(0, 89) + random.random())
    lon = str(random.randint(0, 89) + random.random())
    map_url = f'https://static-maps.yandex.ru/1.x/?ll={lon},{lat}&size=600,400&z=12&l=map&pt={lon},{lat},pm2rdm'
    return render_template('index.html', map_url=map_url, lat=lat, lon=lon)

@app.route('/check', methods=['POST'])
def check():
    return 'Координаты успешно проверены!'

if __name__ == '__main__':
    app.run(debug=True)