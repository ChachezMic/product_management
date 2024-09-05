from flask import Flask
app = Flask(__name__)

@app.route('/')
def hey_you():
    return 'Hey You!'

if __name__ == '__main__':
    app.run()
