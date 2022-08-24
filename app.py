import discord
from discord.ext import commands
from discord.utils import get
class DiscordClient:
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.presences = True
        self.bot = commands.Bot(command_prefix='!',intents=intents, case_insensitve=True)
    async def start_status(self):
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(f"Dark Moded!"))

    async def add_role(self,user_id):
        guild = self.bot.get_guild(1011894736979775508)
        role = guild.get_role(1011895024180547604)
        user = guild.get_member(int(user_id))
        await user.add_roles(role)
