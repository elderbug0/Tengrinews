from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/systema_gos')
def corrution():
    return render_template('new_law.html')

if __name__ == '__main__':
    app.run(debug=True)
