import ssl
import websocket
import _thread as thread

def on_message(ws,message):
    print(message)

def on_error(ws,error):
    print(error)

def on_close(ws):
    print("## CLOSED ##")

def on_open(ws):
    
        ws.send(logon_msg)
    

if __name__ == "__main__":
    logon_msg = '{"type": "subscribe","subscriptions":[{"name":"l2","symbols":["BTCUSD"]}]}'
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://api.gemini.com/v2/marketdata",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close,
                                on_open = on_open)
    
    
    #ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    

