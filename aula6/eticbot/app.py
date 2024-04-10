import click
from eticbot import bot as discord_bot



@click.group
def bot():
    pass

@bot.command()
# @click.option("-g","--guildID","guild_id")
@click.option("-t", "--token")
    
def start(guild_id:str, token:str):
    discord_bot.client.run(token)


    click.secho("hi from bot")

if __name__ == '__main__':
    bot(auto_envvar_prefix="ETIC")