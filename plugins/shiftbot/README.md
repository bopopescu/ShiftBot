# shiftbot

ごみ捨て当番，議事録当番をお知らせするslackbotです．

## 注意点

このリポジトリにあるコードは，今実際に動いているコードと異なります．
議事録当番を決定するロジックが再現できそうになかったので，循環リストを使用したものに変更中です．

## 開発環境

- Python 3.7.4
- MySQL
- Python library
  - mysql_connector_python
  - slackbot

## 実装中

- 循環リストを用いたごみ当番交代のロジック
- リマインダーとしてダイレクトメッセージを送信
- 代理当番の登録
