import asyncio
import websockets


async def say_hello(websocket, path):
    name = await websocket.recv()
    print(f'< {name}')

    greeting = f'Hello {name}!'
    await websocket.send(greeting)

    print(f'> {greeting}')


start_server = websockets.serve(say_hello, 'localhost', 8765)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
