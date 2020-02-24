# need do `pip install websocket-client`
import websocket
import urllib
import urllib.request
import json
import sys

data1 = [120,111,120,98,45,49,51,57,53,57,48,48,48,50,51,56,57,45,57,52,51,53,50,55,48,51,48,56,54,55,45,111,86,109,84,106,102,102,82,122,102,90,73,108,83,114,117,53,116,77,86,55,55,83,]
channel_sida = "DU30JG05B"
channel_gpuvoxels_bot = "GTRFXCMGB"
channel = "" # if you want to know your private channel, use bot.listen() and send "channel" to the bot.
msg_id = 0
msg_text = ""
IPAddr = ""

def get_ip():
    global IPAddr
    URL = 'https://api.ipify.org'
    connection = urllib.request.urlopen(URL)
    text = connection.read().decode("utf-8")
    IPAddr = text
get_ip()

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
    send_msg(ws, channel, f"{msg_text} [from: {IPAddr}]")
    print("Slack message sent: "+msg_text)
    ws.close()

def on_message(ws, msg):
    data = json.loads(msg)
    if "channel" in data:
        if "text" in data:
            if data["text"]=="channel":
                send_msg(ws, data["channel"], f"This channel is: {data['channel']}")

def send(text, number, to_channel="GTRFXCMGB"):
    global msg_text, channel
    data = [69,70,71]
    msg_text = text
    channel = to_channel
    ws_url = start_rtm(data[number])
    if ws_url=="":
        return -1
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(ws_url, on_open=on_open, on_message=on_message)
    ws.run_forever()
    return 0

def listen(number):
    data = [69,70,71]
    ws_url = start_rtm(data[number])
    if ws_url=="":
        return -1
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(ws_url, on_message=on_message)
    ws.run_forever()

if __name__ == "__main__":
    # listen(1)
    send("ok", 1, channel_sida)
