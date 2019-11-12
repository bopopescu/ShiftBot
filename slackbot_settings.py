# coding: utf-8

import configparser

# SlackのAPIを利用するためのトークンを設定ファイルから読み込む
conf = configparser.ConfigParser()
conf.read('./config.ini')
API_TOKEN = conf['slack']['verification_token']

# 対応するメッセージがなかった場合に反応するメッセージ
DEFAULT_REPLY = "I dont't understand you."

# Botが実行するスクリプトを配置するディレクトリパスのリスト
PLUGINS = ['plugins']
