**今すぐプレイ**
https://chatapp-hcwg.onrender.com
Markdown
# 🚀 Flask Real-time ChatApp

MongoDB と Socket.io を活用した、リアルタイムでメッセージの送受信ができるチャットアプリケーションです。

## ✨ 主な機能
- **リアルタイム通信**: Socket.io により、リロードなしで即座にメッセージが届きます。
- **メッセージ永続化**: MongoDB (Atlas) を使用し、過去のチャット履歴を保存します。
- **入力中ステータス**: 誰かが文字を打っているときに「入力中...」と表示されます。
- **レスポンシブデザイン**: スマホからも快適にチャットを楽しめます。

## 🛠 使用技術
- **Backend**: Python 3.9+, Flask
- **Real-time**: Flask-SocketIO, Eventlet
- **Database**: MongoDB (PyMongo)
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render

## 📁 フォルダ構成
```text
ChatApp/
├── .gitignore
├── requirements.txt    # 依存ライブラリ一覧
└── MessageApp/         # アプリ本体
    ├── app.py          # メインプログラム
    ├── templates/      # HTMLテンプレート
    └── static/         # CSS/JavaScript

Bash
python3 MessageApp/app.py
🌐 デプロイについて (Render)
このプロジェクトは Render で公開されています。
