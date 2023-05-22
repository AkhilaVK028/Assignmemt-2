import asyncio
import websockets


async def client():
    async with websockets.connect('ws://localhost:8000') as websocket:
        print('Connected to server.')

        while True:
            message = input("Enter a message: ")
            await websocket.send(message)
            print('Sent message:', message)
            response = await websocket.recv()
            print('Received response:', response)
            if message.lower() == 'exit':
                break
        await websocket.close()
        print('Disconnected from server.')


asyncio.get_event_loop().run_until_complete(client())