from flask import Flask, request
import re
from mod_jieba import JiebaModel as SegModel
from utils import is_punctuation
app = Flask(__name__)
model = SegModel()

@app.route('/')
def hello():
    return {
        "message": "Hello"
    }


@app.route('/seg', methods=['POST'])
def seg():
    assert request.method == 'POST'
    data = None
    text = ""
    try:
        data = request.json
        text = data['text']
    except:
        data = None
    if not data:
        return {
            "msg": "error"
        }
    lst = [i for i in model.segment(text) if not is_punctuation(i)]
    
    return {
        "msg": "ok",
        "data": lst
    }
