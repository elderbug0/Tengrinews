from flask import Flask, render_template, request, jsonify, redirect
import json
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 
db = SQLAlchemy(app)





class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    article_url = db.Column(db.String, nullable=False)  


with app.app_context():
    db.create_all()



news_data = {
    'corruption': {
        'title': 'Демпинг мафия жалобщиков и прозрачность что изменит новый закон о госзакупках', 
        'url': '/systema_gos',
        'image': '/static/photos/eyes.png',
        'keywords': ['демпинг мафия жалобщиков и прозрачность что изменит новый закон о госзакупках'],
        'date': '2024-04-10'
        
    },
    'earn': {
        'title': 'Как заработать столько денег, чтобы можно было не работать в Казахстане', 
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
        'title': 'В тени Туркестана. почему мужчины покидают райский город на юге Казахстана', 
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
    'earthquake': {
        'title': '"Землетрясение ощутили жители Алматы', 
        'url': '/earthquake',
        'image': '/static/photos/photo_468033.jpeg.png',
        'keywords': ['землетрясение ощутили жители алматы'],
        'date': '2024-03-30'
    },
    'akim': {
        'title': 'Аким Костаная обратился к жителям города с просьбой', 
        'url': '/akim',
        'image': '/static/photos/photo_468043.jpeg.png',
        'keywords': ['аким костаная обратился к жителям города с просьбой'],
        'date': '2024-04-01'
    },
    'bishimbaev': {
        'title': '"Вы что, идеальный человек?" - вопросы присяжных зачитали в суде над Бишимбаевым', 
        'url': '/bishimbaev',
        'image': '/static/photos/photo_468156.jpg',
        'keywords': ['вы что идеальный человек вопросы присяжных зачитали в суде над бишимбаевым'],
        'date': '2024-03-29'
    },
    'grad': {
        'title': 'Алматинцев предупредили о крупном граде', 
        'url': '/grad',
        'image': '/static/photos/photo_468175.jpeg.png',
        'keywords': ['алматинцев предупредили о крупном граде'],
        'date': '2024-03-27'
    },
    'moroz': {
        'title': 'Морозы до 13 градусов придут в Казахстан', 
        'url': '/moroz',
        'image': '/static/photos/photo_468433.png.png',
        'keywords': ['морозы до 13 градусов придут в казахстан'],
        'date': '2024-04-11'
    },
    'antikor': {
        'title': 'Антикор нашел 129 миллионов тенге дома у налоговика из Астаны', 
        'url': '/antikor',
        'image': '/static/photos/photo_468414.jpeg (1).png',
        'keywords': ['антикор нашел 129 миллионов тенге дома у налоговика из астаны'],
        'date': '2024-03-25'
    },
}





@app.route('/')
def home():
    return render_template('index.html')

@app.route('/systema_gos', methods=['GET', 'POST'])
def corrution():
    if request.method == 'POST':
        comment_content = request.form.get('comment-input')
        new_comment = Comment(content=comment_content, article_url='/systema_gos')  
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.url)
    comments = Comment.query.filter_by(article_url='/systema_gos').order_by(Comment.date_posted.desc()).all() 

    return render_template('new_law.html', comments=comments)

@app.route('/tokaev', methods=['GET', 'POST'])
def tokaev():
    if request.method == 'POST':
        comment_content = request.form.get('comment-input')
        new_comment = Comment(content=comment_content, article_url='/tokaev') 
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.url)
    comments = Comment.query.filter_by(article_url='/tokaev').order_by(Comment.date_posted.desc()).all()  
    return render_template('tokaev.html', comments=comments)

@app.route('/earn', methods=['GET', 'POST'])
def earn():
    if request.method == 'POST':
        comment_content = request.form.get('comment-input')
        new_comment = Comment(content=comment_content, article_url='/earn')  
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.url)
    comments = Comment.query.filter_by(article_url='/earn').order_by(Comment.date_posted.desc()).all()  

    return render_template('earn.html', comments=comments)

@app.route('/aktobe', methods=['GET', 'POST'])
def aktobe():
    if request.method == 'POST':
        comment_content = request.form.get('comment-input')
        new_comment = Comment(content=comment_content, article_url='/aktobe') 
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.url)
    comments = Comment.query.filter_by(article_url='/aktobe').order_by(Comment.date_posted.desc()).all()  
    return render_template('aktobe.html', comments=comments)

@app.route('/turkistan', methods=['GET', 'POST'])
def turkistan():
    if request.method == 'POST':
        comment_content = request.form.get('comment-input')
        new_comment = Comment(content=comment_content, article_url='/turkistan')  
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.url)
    comments = Comment.query.filter_by(article_url='/turkistan').order_by(Comment.date_posted.desc()).all()  
    return render_template('turkistan.html', comments=comments)

@app.route('/kazavto', methods=['GET', 'POST'])
def kazavto():
    if request.method == 'POST':
        comment_content = request.form.get('comment-input')
        new_comment = Comment(content=comment_content, article_url='/kazavto')  
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.url)
    comments = Comment.query.filter_by(article_url='/kazavto').order_by(Comment.date_posted.desc()).all()  
    return render_template('kazavto.html', comments=comments)

@app.route('/nazbank', methods=['GET', 'POST'])
def nazbank():
    if request.method == 'POST':
        comment_content = request.form.get('comment-input')
        new_comment = Comment(content=comment_content, article_url='/nazbank')  
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.url)
    comments = Comment.query.filter_by(article_url='/nazbank').order_by(Comment.date_posted.desc()).all()  
    return render_template('nazbank.html', comments=comments)

@app.route('/babushka', methods=['GET', 'POST'])
def babushka():
    if request.method == 'POST':
        comment_content = request.form.get('comment-input')
        new_comment = Comment(content=comment_content, article_url='/babushka')  
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.url)
    comments = Comment.query.filter_by(article_url='/babushka').order_by(Comment.date_posted.desc()).all()
    return render_template('babushka.html', comments=comments)

@app.route('/voda', methods=['GET', 'POST'])
def voda():
    if request.method == 'POST':
        comment_content = request.form.get('comment-input')
        new_comment = Comment(content=comment_content, article_url='/voda')  
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.url)
    comments = Comment.query.filter_by(article_url='/voda').order_by(Comment.date_posted.desc()).all()
    return render_template('voda.html', comments=comments)

@app.route('/earthquake', methods=['GET', 'POST'])
def earthquake():
    if request.method == 'POST':
        comment_content = request.form.get('comment-input')
        new_comment = Comment(content=comment_content, article_url='/earthquake') 
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.url)
    comments = Comment.query.filter_by(article_url='/earthquake').order_by(Comment.date_posted.desc()).all()
    return render_template('earthquake.html', comments=comments)

@app.route('/akim', methods=['GET', 'POST'])
def akim():
    if request.method == 'POST':
        comment_content = request.form.get('comment-input')
        new_comment = Comment(content=comment_content, article_url='/akim') 
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.url)
    comments = Comment.query.filter_by(article_url='/akim').order_by(Comment.date_posted.desc()).all()
    return render_template('akim.html', comments=comments)

@app.route('/bishimbaev', methods=['GET', 'POST'])
def bishimbaev():
    if request.method == 'POST':
        comment_content = request.form.get('comment-input')
        new_comment = Comment(content=comment_content, article_url='/bishimbaev') 
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.url)
    comments = Comment.query.filter_by(article_url='/bishimbaev').order_by(Comment.date_posted.desc()).all()
    return render_template('bishimbaev.html', comments=comments)

@app.route('/grad', methods=['GET', 'POST'])
def grad():
    if request.method == 'POST':
        comment_content = request.form.get('comment-input')
        new_comment = Comment(content=comment_content, article_url='/grad')  
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.url)
    comments = Comment.query.filter_by(article_url='/grad').order_by(Comment.date_posted.desc()).all()

    return render_template('grad.html' , comments=comments)

@app.route('/moroz', methods=['GET', 'POST'])
def moroz():
    if request.method == 'POST':
        comment_content = request.form.get('comment-input')
        new_comment = Comment(content=comment_content, article_url='/moroz')  
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.url)
    comments = Comment.query.filter_by(article_url='/moroz').order_by(Comment.date_posted.desc()).all()

    return render_template('moroz.html' , comments=comments)

@app.route('/antikor', methods=['GET', 'POST'])
def antikor():
    if request.method == 'POST':
        comment_content = request.form.get('comment-input')
        new_comment = Comment(content=comment_content, article_url='/antikor')  
        db.session.add(new_comment)
        db.session.commit()
        return redirect(request.url)
    comments = Comment.query.filter_by(article_url='/antikor').order_by(Comment.date_posted.desc()).all()

    return render_template('antikor.html' , comments=comments)


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
    app.run(port=5000)
