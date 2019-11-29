# coding: utf-8
import configparser

# SlackのAPIを利用するためのトークンを設定ファイルから読み込む
conf = configparser.ConfigParser()
conf.read('./config.ini')
VERIFICATION_TOKEN = conf['slack']['verification_token']

API_TOKEN = conf['slack']['BOT_USER_OAUTH_ACCESS_TOKEN']

# 対応するメッセージがなかった場合に反応するメッセージ
DEFAULT_REPLY = "Sorry, I dont't understand you."

# Botが実行するスクリプトを配置するディレクトリパスのリスト
PLUGINS = ['plugins']
