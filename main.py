import discord


def get_token():
    return ""  # put your key here



class MyClient(discord.Client):


    async def on_ready(self):

        # does this on start

        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


    async def on_message(self, message):

        if message.author.id == self.user.id:  # we do not want the bot to reply to itself
            return

        # if message is !hello

        if message.content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)  # say hello
            game = discord.Game("with the API")  # create status object
            await client.change_presence(status=discord.Status.idle, activity=game)  # change status



intents = discord.Intents.default()  # create client's intents
client = MyClient(intents=intents)  # create client
client.run(get_token())  # run client
