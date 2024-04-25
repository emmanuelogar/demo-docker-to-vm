import time
import redis
from flask import Flask
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
@app.route('/')
def hello():
    count = cache.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)
