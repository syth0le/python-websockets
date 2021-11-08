import asyncio
import datetime
import random
import websockets


async def type_time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)


start_server = websockets.serve(type_time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
