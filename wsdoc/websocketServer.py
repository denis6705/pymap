import json
from multiping import multi_ping
import asyncio
import datetime
import websockets

with open('nodes.json', encoding='utf-8') as f:
        nodes = json.load(f)

ips = [n['ip'] for n in nodes]

async def send_pings(websocket, path):
    while True:
        responses, no_responses = multi_ping(ips, timeout=2, retry=3)
        for n in nodes:
            if n['ip'] in responses:
                n['ping'] = responses[n['ip']] * 1000
                n['result'] = True
            else:
                n['ping'] = 9999
                n['result'] = False
        await websocket.send(json.dumps(nodes))


start_server = websockets.serve(send_pings, '0.0.0.0', 1234)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
