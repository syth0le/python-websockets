async def handler(websocket, path):
    while True:
        message = await websocket.recv()
        await consumer(message)