import websocket
from websocket import create_connection
url2 = "wss://push1-v2.kucoin.com"
url = "wss://api.gemini.com/v2/marketdata"

websocket.enableTrace(True)
ws = websocket.WebSocket()
ws.connect(url)
ws.send('{"type": "subscribe","subscriptions":[{"name":"candles_1h","symbols":["BTCUSD"]}]}')
print(ws.recv())
ws.close
