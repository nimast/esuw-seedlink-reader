# -*- coding: utf-8 -*-
from . import helpers
import numpy as np
import socketio 
from obspy.clients.seedlink.easyseedlink import EasySeedLinkClient

class GsiClient(EasySeedLinkClient):

    global sio 
    emit_data = False

    sio = socketio.Client()

    def __init__(self, addr):
        super().__init__(addr)
        np.set_printoptions(suppress=True)
        #self.sio = socketio.AsyncClient()\
        sio.connect('https://earth-signal-universe-wide.space/')
        print('my sid is', sio.sid)

    @staticmethod
    @sio.event
    def connect():
        
        print('what is emit data before connect? ', GsiClient.emit_data)
        print("I'm connected!")
        GsiClient.emit_data = True
        print('what is emit data after connect? ', GsiClient.emit_data)
    
    @staticmethod
    @sio.event
    def connect_error(data):
        print("The connection failed!")
        GsiClient.emit_data = False   

    @staticmethod
    @sio.event
    def disconnect():
        print("I'm disconnected!")
        GsiClient.emit_data = False

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
        print('Received trace, will emit? :', GsiClient.emit_data)
        print(trace)
        #print()
        trace.detrend(type='linear')
        div = np.true_divide(trace.data, 0.405966)
        rounded = np.round_(div, decimals=8)
        #print(div)
        if (GsiClient.emit_data):
            #print('data emittted')
            sio.emit('seis-rec', {'data': rounded.tolist()})
        else:
            pass
            #print('emit skipped')


