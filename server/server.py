
# import flast module
from flask import Flask
import time
from threading import Thread
from constants import Constants
from flask import Response
from flask import request

def translation_simulator(interval):
    time.sleep(Constants.TIMEOUT)
 
# instance of flask application
app = Flask(__name__)
translation_status = None

 
# status route that returns below text when /status url is accessed
@app.route("/status")
def status():
    global translation_status
    id = request.args.get('id')
    if id == None:
        return Response("Invalid arguments", status=400)
    try:
        id = int(id)
    except ValueError:
        # Handle the exception
        return Response("Invalid arguments", status=400)
    if translation_status == None:
        translation_status = Thread(target=translation_simulator, name=string(id))
        translation_status.start()
    if (not translation_status) or translation_status.is_alive():
        return "{status: 'pending'}"
    else:
        if id % 2 == 0:
            return "{status: 'completed'}"
        else:
            return "{status: 'error'}"
 
if __name__ == '__main__':
    app.run()
