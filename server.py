# Server Setup: Need to setup a server that can handle WebSocket connections - socket.io

# Client Integration: We'll set up the socket.io client in my Pygame script to send package count data to the server without disrupting the game's performance

import socketio
from aiohttp import web
import os

# Create a Socket.io server

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

# Serve the HTML client

# async def index(request):
#     with open('indexv2.html', 'r') as f:
#         return web.Response(text=f.read(), content_type='text/html')
    
# # Socket.io events

# async def connect(sid, environ):
#     print('Client connected', sid)

# @sio.event
# async def disconnect(sid):
#     print('Client disconnected:', sid)

# @sio.event
# async def package_data(sid, data):
#     print('Package Data', data)
#     await sio.emit('update_dashboard', data)

# app.router.add_get('/', index)

# if __name__ == '__main__':
#     web.run_app(app, port=8080)

# Serve HTML from the React build directory
async def index(request):
    return web.FileResponse('./dashboard/build/index.html')

# Setting up static routes to serve the contents of the React build folder
app.router.add_static('/', path='./dashboard/build', name='build')

@sio.event
async def connect(sid, environ):
    print('Client connected:', sid)

@sio.event
async def disconnect(sid):
    print('Client disconnected:', sid)

@sio.event
async def package_data(sid, data):
    print('Package Data:', data)
    await sio.emit('update_dashboard', data)

app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app, port=8080)
