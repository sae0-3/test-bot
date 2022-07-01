import discord
from discord.ext import commands
from requests import get

tokenCC = open('tokenCC.txt', 'r')
tokenBot = open('tokenBot.txt', 'r')

headersCC = { 'Authorization': f'{tokenCC.read()}' }
tokenCC.close()

bot = commands.Bot(command_prefix='|')
token = f'{tokenBot.read()}'
tokenBot.close()

#*--------------
@bot.command()
async def ccClan(ctx, tag):
    url = 'https://api.clashofclans.com/v1/clans/%23' + tag
    data = get(url, headers=headersCC).json()

    embed = discord.Embed(title=data['name'], description=data['description'], color=discord.Color.orange())
    embed.set_thumbnail(url=data['badgeUrls']['medium'])
   
    embed.add_field(name='Tag:', value=data['tag'])
    embed.add_field(name='Members:', value=data['members'])
    embed.add_field(name='Location:' , value=data['location']['name'])
    embed.add_field(name='Required Trophies', value=data['requiredTrophies'])
    embed.add_field(name='Type:' , value=data['type'])
    embed.add_field(name='Level:' , value=data['clanLevel'])
    embed.add_field(name='Points:' , value=data['clanPoints'])
    embed.add_field(name='Chat Language', value=f"{data['chatLanguage']['name']} {data['chatLanguage']['languageCode']}")
    embed.add_field(name='Required Town Hall Level', value=data['requiredTownhallLevel'])
  
    embed.add_field(name='Versus Points:' , value=data['clanVersusPoints'])
    embed.add_field(name='War Frecuency:' , value=data['warFrequency'])
    embed.add_field(name='Wars Won:' , value=data['warWins'])
    embed.add_field(name='War Win Streak:' , value=data['warWinStreak'])
    embed.add_field(name='Lost Wars:' , value=data['warLosses'])
    embed.add_field(name='Public war record:' , value=data['isWarLogPublic'])
    embed.add_field(name='War League:' , value=data['warLeague']['name'])

    await ctx.send(embed=embed)

#*--------------
@bot.command()
async def ccMembers(ctx, tag):
    urlClan = 'https://api.clashofclans.com/v1/clans/%23' + tag
    dataClan = get(urlClan, headers=headersCC).json()

    url = f'https://api.clashofclans.com/v1/clans/%23{tag}/members'
    data = get(url, headers=headersCC).json()

    embed = discord.Embed(title=dataClan['name'], description='Members:', color=discord.Color.green())
    embed.set_thumbnail(url=dataClan['badgeUrls']['medium'])

    for x in data['items']:
        embed.add_field(name=x['name'], value=x['tag'])
       
    await ctx.send(embed=embed)    

#*--------------
@bot.command()
async def ccPlayer(ctx, tag):
    url = 'https://api.clashofclans.com/v1/players/%23' + tag
    data = get(url, headers=headersCC).json()

    embed = discord.Embed(title=data['name'], color=discord.Color.red())
    embed.set_thumbnail(url=data['league']['iconUrls']['medium'])

    embed.add_field(name='Tag:', value=data['tag'])
    embed.add_field(name='Town Hall Level:', value=data['townHallLevel'])
    embed.add_field(name='Trophies:', value=data['trophies'])
    embed.add_field(name='Level of Experience:', value=data['expLevel'])
    embed.add_field(name='Best Trophies:', value=data['bestTrophies'])
    embed.add_field(name='War Stars:', value=data['warStars'])
    embed.add_field(name='Attacks Won:', value=data['attackWins'])
    embed.add_field(name='Defense Victories:', value=data['defenseWins'])
    embed.add_field(name='League:', value=data['league']['name'])
    embed.add_field(name='Clan:', value=f"{data['clan']['name']} - {data['clan']['tag']}")
    embed.add_field(name='Donations:', value=data['donations'])
    embed.add_field(name='Role:', value=data['role'])
    embed.add_field(name='Donations Received:', value=data['donationsReceived'])
    embed.add_field(name='War Preference:', value=data['warPreference'])

    await ctx.send(embed=embed)

#*---------------------------------------------------------------------------
@bot.event
async def on_ready():
    print("My Bot is Ready")

bot.run(token)
