from esuwseedlinkreader.core import GsiClient
client = GsiClient('82.102.143.63:18000')
client.select_stream('IS', 'DSI', 'ENZ')
client.run()
