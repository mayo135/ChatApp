import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv() # ← これで .env を読み込む！

# Socket.ioのセットアップ --- (※1)
socketio = SocketIO(app)

# MongoDBの接続先設定 --- (※2)
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
mongo_uri = os.getenv("MONGO_URI")
db = client["SNS"]
messages_collection = db["messages"]

#メッセージ全削除
#result = messages_collection.delete_many({})
#print(f"{result.deleted_count} 件のメッセージを削除しました。")

@app.route("/")
def index():
    return render_template("index.html")

# メッセージの読み込み --- (※3)
@socketio.on('load messages')
@socketio.on('load messages')
def load_messages():
    # 最新10件を取得
    messages = messages_collection.find().sort('_id', -1).limit(10)
    messages_list = list(messages)[::-1]
    
    # 【重要】ObjectIdが含まれるデータをそのまま送らず、必要なものだけリストにする
    formatted_messages = []
    for m in messages_list:
        formatted_messages.append({
            'name': m.get('name', 'Anonymous'),
            'message': m.get('message', ''),
            'time': m.get('time', '')
        })
    emit('load all messages', formatted_messages)

# メッセージの登録 --- (※5)
@socketio.on('send message')
def send_message(data):
    new_msg = {
        'name': data['name'] if data['name'] else 'Anonymous',
        'message': data['message'],
        'time': datetime.now().strftime('%H:%M')
    }
    # ここで new_msg に '_id' が自動追加される
    messages_collection.insert_one(new_msg)
    
    # 【重要】new_msg をそのまま送らず、必要な項目だけを辞書にして送る
    emit('load one message', {
        'name': new_msg['name'],
        'message': new_msg['message'],
        'time': new_msg['time']
    }, broadcast=True)

# 【追加】入力中ステータスの通知
@socketio.on('typing')
def handle_typing(data):
    # data は {'name': 'ユーザー名', 'is_typing': True}
    # 送信者以外（include_self=False）に「誰々が入力中」と伝える
    emit('display typing', data, broadcast=True, include_self=False)

if __name__ == "__main__":
    socketio.run(app, debug=True, port=5001)