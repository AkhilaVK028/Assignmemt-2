import asyncio
import websockets


# Define the WebSocket server behavior
async def server(websocket, path):
    print('New client connected.')

    try:
        while True:
            message = await websocket.recv()
            print('Received message:', message)
            response = 'Server received your message: ' + message
            await websocket.send(response)

    except websockets.ConnectionClosedOK:
        print('Client disconnected.')


# Start the WebSocket server
start_server = websockets.serve(server, 'localhost', 8000)

# Run the server indefinitely
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

