async def handler(websocket, path):
    while True:
        message = await producer()
        await websocket.send(message)