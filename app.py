from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def landing_page():
    return render_template('index.html',name="index page")

if __name__ == '__main__':
    app.run(debug=True)