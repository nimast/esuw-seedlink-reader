# -*- coding: utf-8 -*-
from . import helpers
import numpy as np
import socketio 
from obspy.clients.seedlink.easyseedlink import EasySeedLinkClient



class GsiClient(EasySeedLinkClient):

    global emit_data
    global sio 

    emit_data = False
    sio = socketio.Client()

    def __init__(self, addr):
        super().__init__(addr)
        #self.sio = socketio.AsyncClient()\
        sio.connect('https://earth-signal-universe-wide.space/')
        print('my sid is', sio.sid)

    @staticmethod
    @sio.event
    def connect():
        print("I'm connected!")
        emit_data = True
    
    @staticmethod
    @sio.event
    def connect_error(data):
        print("The connection failed!")
        emit_data = False   

    @staticmethod
    @sio.event
    def disconnect():
        print("I'm disconnected!")
        emit_data = False

    # @sio.on('*')
    # async def catch_all(event, data):
    #     print("ASYNCIO EVENT")
    #     print(event)
    #     print(data)
    #     pass
    """
    Read seedlink
    """

    def on_data(self, trace):
        """
        Override the on_data callback
        """
        print('Received trace:')
        print(trace)
        print()
        trace.detrend(type='linear')
        div = np.true_divide(trace.data, 405966.0)
        print(div)
        if (emit_data):
            sio.emit('seis-rec', {'data': div.tolist()})

def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())
