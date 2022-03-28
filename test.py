from esuwseedlinkreader.core import GsiClient
import asyncio

#async def main():
def main():

  client = GsiClient('82.102.143.63:18000')
  client.select_stream('IS', 'DSI', 'ENZ')
  client.run()

main()
#asyncio.run(main())