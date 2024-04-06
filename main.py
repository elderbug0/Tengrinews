from flask import Flask, render_template, request, redirect, jsonify, url_for


app = Flask(__name__)

news_data = {
    'corruption': {
        'title': 'Прозрачность в системе', 
        'url': '/systema_gos',
        'image': '/static/photos/eyes.png',
        'keywords': ['демпинг мафия жалобщиков и прозрачность что изменит новый закон о госзакупках']
    },
    'tokaev': {
        'title': 'Визит Токаева в Узбекистане', 
        'url': '/tokaev',
        'image': '/static/photos/photo_467829.jpeg',
        'keywords': ['токаев прилетел в узбекситан']
    },
    'earn': {
        'title': 'Как заработать много денег', 
        'url': '/earn',
        'image': '/static/photos/photo_467839.jpeg',
        'keywords': ['как заработать столько денег, чтобы можно было не работать в казахстане']
    },
    'aktobe': {
        'title': 'Потоп в Актобе', 
        'url': '/aktobe',
        'image': '/static/photos/photo_467838.jpeg',
        'keywords': ['как выглядит прорванная плотина в актюбинской области']
    },
    'turkistan': {
        'title': 'В тени Туркестана', 
        'url': '/aktobe',
        'image': '/static/photos/photo_3494.jpeg',
        'keywords': ['в тени туркестана. почему мужчины покидают райский город на юге казахстана']
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

@app.route('/moshennik')
def moshennik():
    return render_template('moshennik.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data['query'].lower()
    matches = [value for value in news_data.values() if any(query in keyword for keyword in value['keywords'])]
    return jsonify(matches)




if __name__ == '__main__':
    app.run(debug=True)
