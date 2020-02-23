# need do `pip install websocket-client`
import websocket
import urllib
import urllib.request
import json
import sys

data1 = [120,111,120,98,45,49,51,57,53,57,48,48,48,50,51,56,57,45,57,52,51,53,50,55,48,51,48,56,54,55,45,111,86,109,84,106,102,102,82,122,102,90,73,108,83,114,117,53,116,77,86,55,55,83,]

sida = "DU30JG05B"
channel = "GTRFXCMGB"
msg_id = 0
msg_text = ""

def start_rtm(number):
    data = [*data1,number]
    data = [chr(i) for i in data]
    data = "".join(data)
    URL = "https://slack.com/api/rtm.connect?token={}".format(data)
    connection = urllib.request.urlopen(URL)
    text = connection.read().decode("utf-8")
    data = json.loads(text)
    if "url" in data:
        ws_url = data["url"]
        return ws_url
    return ""

def send_msg(ws, channel, message):
    global msg_id
    reply_obj = {"id": msg_id, "type": "message", "channel": channel, "text": message}
    msg_id += 1
    reply_str = json.dumps(reply_obj)
    ws.send(reply_str)

def on_open(ws):
    send_msg(ws, sida, "AUTOMSG: "+msg_text)
    print("Slack message sent: "+msg_text)
    ws.close()

def on_message(ws, msg):
    print(msg)

def send(text, number):
    global msg_text
    msg_text = text
    ws_url = start_rtm(number)
    if ws_url=="":
        return -1
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(ws_url, on_open=on_open, on_message=on_message)
    ws.run_forever()
    return 0

if __name__ == "__main__":
    send("test",0)
