from flask import Flask, render_template

app = Flask(__name__)

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
@app.route('/bishimbaev')
def bishimbaev():
    return render_template('bishimbaev.html')
@app.route('/moshennik')
def moshennik():
    return render_template('moshennik.html')

if __name__ == '__main__':
    app.run(debug=True)
