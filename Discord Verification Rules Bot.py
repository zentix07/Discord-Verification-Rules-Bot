import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import discord.ui


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)



@bot.event
async def on_ready():
  print('System rebooted.')
  bot.add_view(Verification())

class Verification(discord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
  @discord.ui.button(label="Verify",custom_id = "Verify",style = discord.ButtonStyle.success)
  async def verify(self, interaction, button):
    role = 1083897631635411035
    user = interaction.user
    if role not in [y.id for y in user.roles]:
      await user.add_roles(user.guild.get_role(role))
      await user.send("You have been verified!")

@bot.command()
@has_permissions(administrator=True)
async def CreateVerify(ctx):
  embed = discord.Embed(title = "Verification", description = "Click below to verify.")
  await ctx.send(embed = embed, view = Verification())










@bot.command()
@has_permissions(administrator=True)

async def MakeRules(ctx):
    embed=discord.Embed(
    title=" ",
        url="https://github.com/zentix07",
        description=" ",
        color=discord.Color.blue())

    embed.add_field(name=" ", value=" ", inline=False)
    embed.add_field(name=" ", value=" ", inline=False)
    embed.add_field(name=" “, value=" ", inline=False)
    embed.add_field(name=" ", value=" ", inline=False)
    embed.add_field(name=" ", value=" ", inline=False)
    embed.add_field(name=" ", value=" ", inline=False)
    embed.add_field(name=" ", value=" ", inline=False)
    embed.add_field(name=" ", value=" ", inline=False)
    embed.add_field(name=“ ”, value=" ", inline=False)
    embed.add_field(name=" ", value=" ", inline=False)
    embed.add_field(name=" ", value=" ", inline=False)
    embed.add_field(name=" ", value=" ", inline=False)
    embed.add_field(name=" ", value=" ", inline=False)
    embed.add_field(name=" ", value=" ", inline=False)
    embed.add_field(name=" ", value=" ", inline=False)
    embed.add_field(name=" ", value=" ", inline=False)
    embed.add_field(name=" ", value=" ", inline=False)

    embed.set_footer(text="Bot made by Zentix#0700 and yJulien#5228")
    await ctx.send(embed=embed)













bot.run(“Token”)

