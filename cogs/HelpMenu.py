# Imports
import discord
from parameters import *
from helper import *
from discord.ext import commands


class HelpMenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group()
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                color=discord.Color.orange(),
                author='Help',
                description=f'Use `{prefix}help [module name]` for more information'
            )
            embed.add_field(name='**Administration**',
                            value='Managing the server', inline=False)
            embed.add_field(name='**Music**',
                            value='The music player', inline=False)
            await ctx.send(embed=embed)

    @help.command()
    async def Administration(self, ctx):
        cog = self.client.get_cog('Administration')
        commands = cog.get_commands()
        await ctx.send(embed=create_embed('test'))


def setup(client):
    client.add_cog(HelpMenu(client))