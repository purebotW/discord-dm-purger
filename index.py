import discord, os

class Purger(discord.Client):
    def __init__(self, **kwargs):
        super().__init__(request_offline_members=False, chunk_guilds_on_startup=False, guild_subscriptions=False, **kwargs)

    def check(self, message):
        return message.author == self.user
    
    async def on_connect(self):
        for friend in self.user.friends:
            print(f'Purging DMS with {str(friend)}')
            async for message in friend.dm_channel.history(limit=100).filter(self.check):
                await message.delete()
    
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
