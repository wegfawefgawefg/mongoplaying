import time
import os

import redis
# import pymongo
from flask import Flask
from flask import request

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

# @app.route('/')
# def hello():
#     count = get_hit_count()
#     return 'Hello World! I have been seen {} times.\n'.format(count)

@app.route('/list_firmwares')
def list_firmwares():
    return str(cache.get("firmware_names"))

@app.route('/get_firmware_by_name')
def get_firmware_by_name(firmware_name):
    fw = cache.get(firmware_name)
    return str(fw)

# def store_message():
#     hc = get_hit_count()
#     cache.lpush("messages", str(hc))
#     # new_message = request.args.get('message')
#     # if new_message:
#     #     cache.lpush("messages", new_message)
#     binary_messages = cache.lrange("messages", 0, -1)
#     messages = [m.decode() for m in binary_messages]
#     return str(messages)

FIRMWARE_PATH = "/app/firmwares"

def populate_firmwares():
    print("POPULATING FIRMWARES")
    starting_firmware_names = list(os.listdir(FIRMWARE_PATH))
    print(starting_firmware_names)
    cache.lpush("firmware_names", *starting_firmware_names)
    for name in starting_firmware_names:
        loc = os.path.join(FIRMWARE_PATH, name)
        with open(loc, "rb") as f:
            data = f.read(8)
            print(data)
            print(type(data))
            data = bytes(data)
            print(data)
            print(type(data))
            cache.set(name, data)

populate_firmwares()
