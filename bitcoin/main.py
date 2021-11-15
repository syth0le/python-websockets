import asyncio
import json
import time

import matplotlib.pyplot as plt
import websockets

X = []
Y = []

fig = plt.figure()
ax = fig.add_subplot()
fig.show()


def update_graph():
    ax.plot(X, Y, color='b')
    ax.scatter(X, Y, color='r')
    ax.legend([f"Last price: {Y[-1]}$"])
    fig.canvas.draw()
    plt.pause(0.1)


async def main():
    url = 'wss://stream.binance.com:9443/stream?streams=btcusdt@miniTicker'
    async with websockets.connect(url) as con:
        i = 0
        while True:
            data = json.loads(await con.recv())['data']

            event_time = time.localtime(data['E'] // 1000)

            print(f"{event_time.tm_hour}:{event_time.tm_min}:{event_time.tm_sec} - {data['c']}")

            X.append(i)
            Y.append(float(data['c']))

            update_graph()
            i += 1


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
