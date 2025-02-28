from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def landing_page():
    return render_template('index.html',name="index page", style='home.css')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', name='About page', style='about.css')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html',name="contact page")

if __name__ == '__main__':
    app.run(debug=True)