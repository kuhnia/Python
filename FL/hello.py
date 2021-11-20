from datetime import datetime
from flask import Flask
import pytz

app = Flask(__name__)

@app.route('/<path:timezone>')
def hello_world(timezone):
    currentTimeZone = pytz.timezone(timezone)
    str = datetime.now(currentTimeZone).strftime('%H:%M:%S')
    return str

if __name__ == '__main__':
    app.run()