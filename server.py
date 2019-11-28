# This is a barebones socket.io server
from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

@sio.event
def connect(sid, version):
    print("connect", sid)
    return

@sio.event
def disconnect(sid):
    print('disconnect', sid)
    return

@sio.event
async def room(sid, data):
    print('room')
    print(data)
    sio.enter_room(sid, data)

@sio.event
async def leave_room(sid, data):
    print('leaving room')
    print('data')
    sio.leave_room(sid, data)


if __name__ == '__main__':
    web.run_app(app)