from flask import Flask
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def print_date():
    date_time = datetime.now().strftime("%d-%b-%Y %H:%M:%S")
    date_str = f"Date and time is: {date_time}\n"
    return date_str


if __name__ == "__main__":
    app.run(host='0.0.0.0')


