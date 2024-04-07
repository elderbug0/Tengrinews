from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime


app = Flask(__name__)









news_data = {
    'corruption': {
        'title': 'Демпинг мафия жалобщиков', 
        'url': '/systema_gos',
        'image': '/static/photos/eyes.png',
        'keywords': ['демпинг мафия жалобщиков и прозрачность что изменит новый закон о госзакупках'],
        'date': '2024-04-10'
        
    },
    'earn': {
        'title': 'Как заработать много денег', 
        'url': '/earn',
        'image': '/static/photos/photo_467839.jpeg',
        'keywords': ['как заработать столько денег, чтобы можно было не работать в казахстане'],
        'date': '2024-04-06'
    },
    'tokaev': {
        'title': 'Токаев прилетел в Узбекситан', 
        'url': '/tokaev',
        'image': '/static/photos/photo_467829.jpeg',
        'keywords': ['токаев прилетел в узбекситан'],
        'date': '2024-04-05'
    },

    'aktobe': {
        'title': 'Как выглядит прорванная плотина в Актюбинской области', 
        'url': '/aktobe',
        'image': '/static/photos/photo_467838.jpeg',
        'keywords': ['как выглядит прорванная плотина в актюбинской области'],
        'date': '2024-04-07'
    },
    'turkistan': {
        'title': 'В тени Туркестана', 
        'url': '/turkistan',
        'image': '/static/photos/photo_3494.jpeg',
        'keywords': ['в тени туркестана. почему мужчины покидают райский город на юге казахстана'],
        'date': '2024-04-08'
    },
    'nazbank': {
        'title': 'Нацбанк предупредил казахстанцев', 
        'url': '/nazbank',
        'image': '/static/photos/photo_467710.jpg.png',
        'keywords': ['нацбанк предупредил казахстанцев"'],
        'date': '2024-4-04'
    },
    'kazavto': {
        'title': 'Задержан экс-председатель правления "КазАвтоЖола', 
        'url': '/kazavto',
        'image': '/static/photos/photo_467662.jpeg.png',
        'keywords': ['задержан экс-председатель правления "казавтожола"'],
        'date': '2024-04-09'
    },
    'babushka': {
        'title': 'Сделано бабушкой. Кто и почему продает закрутки на улицах Астаны?', 
        'url': '/babushka',
        'image': '/static/photos/photo_3503.jpeg.png',
        'keywords': ['сделано бабушкой кто и почему продает закрутки на улицах астаны'],
        'date': '2024-04-03'
    },
    'voda': {
        'title': '"Вода зашла во все дома": где нашли пристанище казахстанцы, чьи дома затопили паводки', 
        'url': '/voda',
        'image': '/static/photos/photo_3498.jpeg.png',
        'keywords': ['вода зашла во все дома: где нашли пристанище казахстанцы, чьи дома затопили паводки'],
        'date': '2024-04-02'
    },

}





@app.route('/')
def home():
    return render_template('index.html')
@app.route('/systema_gos')
def corrution():
    return render_template('new_law.html')
@app.route('/tokaev')
def tokaev():
    return render_template('tokaev.html')
@app.route('/earn')
def earn():
    return render_template('earn.html')
@app.route('/aktobe')
def aktobe():
    return render_template('aktobe.html')
@app.route('/turkistan')
def bishimbaev():
    return render_template('turkistan.html')
@app.route('/kazavto')
def kazavto():
    return render_template('kazavto.html')
@app.route('/nazbank')
def nazbank():
    return render_template('nazbank.html')
@app.route('/babushka')
def babushka():
    return render_template('babushka.html')
@app.route('/voda')
def voda():
    return render_template('voda.html')


@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data['query'].lower()
    matches = [value for value in news_data.values() if any(query in keyword for keyword in value['keywords'])]
    return jsonify(matches)

@app.route('/filter')
def filter():
    return render_template('filter.html')

@app.route('/filter_news', methods=['POST'])
def filter_news():
    choice = request.json.get('filter_choice')
    all_news = list(news_data.values())

    for news_item in all_news:
        news_item['date'] = datetime.strptime(news_item.get('date', '2024-01-01'), '%Y-%m-%d')

    if choice == 'Последние':
        filtered_news = sorted(all_news, key=lambda x: x['date'], reverse=True)
    else:  # Earliest
        filtered_news = sorted(all_news, key=lambda x: x['date'])

    for news_item in filtered_news:
        news_item['date'] = news_item['date'].strftime('%Y-%m-%d')

    return jsonify(filtered_news)

if __name__ == '__main__':
    app.run(debug=True)
