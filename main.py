from flask import Flask
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

@app.route('/')
def ingest():
    with open('./page.html', 'r') as f:
        page =  f.read()
    return page

if __name__ == '__main__':
    logging.info("STARTING THE APP")
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=False
    )