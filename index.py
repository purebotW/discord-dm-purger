import discord, os

class Purger(discord.Client):
    def __init__(self, **kwargs):
        super().__init__(request_offline_members=False, chunk_guilds_on_startup=False, guild_subscriptions=False, **kwargs)

    def check(self, message):
        return message.author == self.user
    
    async def on_connect(self):
        print('Now purging')
        if not self.user.friends:
            print('No friends to purge.')
            return
        for friend in self.user.friends:
            print(f'Purging DMS with {str(friend)}')
            if not friend.dm_channel:
                continue
            async for message in friend.dm_channel.history(limit=100).filter(self.check):
                await message.delete()
        print('Finished purging.')
        
    def main(self):
        os.system('cls')
        token = input('Token: ')
        os.system('cls')
        try:
            self.run(token, bot=False)
        except: 
            print('Improper token was given.')
            os.system('pause')
            
(Purger()).main()
