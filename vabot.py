import discord
import random
import sys
import os
import datetime
import wavelink

from discord import app_commands, Interaction
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from datetime import datetime, timedelta, time

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
bot = discord.Client(intents=intents)
TOKEN = 'token here'
command = app_commands.CommandTree(bot)
start_time = datetime.now().replace(microsecond=0)




#-------------------------------------------------CODE START-------------------------------------------------#

#bot is ready for combat
@bot.event
async def on_ready():
    await command.sync()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    channel = bot.get_channel(1045319345900888135)
    await channel.send(f'> `{current_time}` - ***Bot is ready!***')
        # Setting `Watching ` status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="ppl die inside"))
    print("\nReady for combat!")
    bot.loop.create_task(node_connect())

async def node_connect():
    await bot.wait_until_ready()
    await wavelink.NodePool.create_node(bot=bot, host='127.0.0.1', port=2300, password='youshallnotpass', https=False)

#wavelink is ready for combat
@bot.event
async def on_wavelink_node_ready(node: wavelink.Node):
    channel = bot.get_channel(1045319345900888135)
    await channel.send(f'<:arrow:1046748055334031534> `Lavalink` - Node, ID= **{node.identifier}** is ready!')
    print(f"Node {node.identifier} is ready!") 



# restarts the bot
@command.command(description="Restart bot!")
@app_commands.default_permissions(administrator=True)
async def restart(interaction: discord.Interaction):
    if interaction.user.id == 419195631198928906:
        await interaction.response.send_message("Restarting...")
        now = datetime.now()
        current_time = now.strftime("%d %B - %H:%M:%S")
        channel = bot.get_channel(1045319345900888135)
        await channel.send(f"> `{current_time}` - Bot is restarting...")
        print("Bot is restarting...")
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        await interaction.response.send_message("You don't have permission to use this command!")
        now = datetime.now()
        current_time = now.strftime("%d %B - %H:%M:%S")
        channel = bot.get_channel(1045319345900888135)
        await channel.send(f"> `{current_time}` - {interaction.user.mention} tried to restart the bot!")
        print("Unauthorized access attempt by " + str(interaction.user))

# shuts down the bot
@command.command(description="Shuts down the bot!")
@app_commands.default_permissions(administrator=True)
async def shutdown(interaction: discord.Interaction):
    if interaction.user.id == 419195631198928906:
        await interaction.response.send_message("shutting down...")
        now = datetime.now()
        current_time = now.strftime("%d %B - %H:%M:%S")
        channel = bot.get_channel(1045319345900888135)
        await channel.send(f"❗ `{current_time}` - Bot is shutting down...")
        print("Bot is shutting down...")
        sys.exit()
    else:
        await interaction.response.send_message("You are not allowed to shut down the bot!")
        now = datetime.now()
        current_time = now.strftime("%d %B - %H:%M:%S")
        channel = bot.get_channel(1045319345900888135)
        await channel.send(f"❗ `{current_time}` - {interaction.user.mention} tried to shut down the bot!")
        print("Unauthorized access attempt by " + str(interaction.user))





# /greetings command
@command.command(description="Hi *shits pants aggressively*")
@app_commands.describe(greet='Input username')
async def greetings(interaction: discord.Interaction, greet: discord.User):
    await interaction.response.send_message(f"Hello, {greet.mention} how are you doing?")

# /love command
@command.command(description="ILY")
@app_commands.describe(lover='Input username')
async def love(interaction: discord.Interaction, lover: discord.User):
    await interaction.response.send_message(f"I love you {lover.mention}!, I love you so much!")
    channel = interaction.channel
    await channel.send("https://tenor.com/view/i-love-you-love-love-you-cute-gif-25661527")
    
# /slap command
@command.command(description="Gonna slap the McShit out of you!")
@app_commands.describe(victim='Input victim')
async def slap(interaction: discord.Interaction, victim: discord.User):
    mentions = discord.AllowedMentions(
        users=False,
    )
    await interaction.response.send_message(f"Slaps {victim.mention} with a McShit!")
    channel = interaction.channel
    await channel.send("https://tenor.com/view/blocked-over-image-discord-rage-wtf-rage-angry-guy-threaten-blocked-gif-21778187")
    
# /showavatar command
@command.command(description="Show avatar!")    
@app_commands.describe(show='Input username')
async def showavatar(interaction: discord.Interaction, show: discord.User):
    userAvatar = show.display_avatar
    embed = discord.Embed(title=f"Avatar",description=f"")
    embed.set_image(url=userAvatar)
    embed.set_author(name=show, icon_url=userAvatar)
    await interaction.response.send_message(embed=embed)



#-------------------------------------------------BOT EVENTS START-------------------------------------------------#

#bot events
@bot.event
async def on_message(message):
    if message.content == "ping":
        await message.channel.send("pong")

    if message.content == "hello":
        await message.channel.send("Hello!")

    if message.content == "cool":
        await message.add_reaction("<a:coolbird:1044910964929208370>")

    if message.content == "how are you?":
        await message.channel.send("I'm fine, thanks!")

    if message.content.startswith("chad"):
        await message.channel.send("https://tenor.com/view/gigachad-chad-gif-20773266")

    if message.content.startswith("bruh"):
        await message.channel.send("https://tenor.com/view/bruh-moment-gif-23616422")

    if message.content.startswith("cringe"):
        await message.channel.send("https://tenor.com/view/dies-from-cringe-pink-skull-cgi-render-gif-23154103")

    if message.content == "W":
        await message.channel.send("https://tenor.com/view/giga-chad-chad-meme-dub-gif-25628266")

    # ask questions!
    if message.content.startswith("-"):
        user_message = message.content
        prediction = open('E:\\Python\\bot\\answers.txt').read().splitlines()
        file = random.choice(prediction)
        you = message.author.mention
        quote_text = f'**{you}** asked: \n> {user_message}\nVabot says: \n> **{file}**'
        await message.reply(quote_text)

    # no ping event
    if message.content == "@everyone":
        await message.delete()
        await message.channel.send("**No pinging *everyone*!**")
    if message.content == "@here":
        await message.delete()
        await message.channel.send("**No pinging *here*!**")

#edit event
@bot.event 
async def on_message_edit(before, after):
    if before.content != after.content:
        channel = before.channel
        channels = bot.get_channel(1045487867188744286)
        embed = discord.Embed(title="Message edited", description=f"**{before.author}** edited a message in {channel.mention}", color=0xF1C8F6)
        embed.add_field(name="Before", value=before.content, inline=False)
        embed.add_field(name="After", value=after.content, inline=False)
        embed.set_footer(text=f"Message ID: {before.id}")
        await channels.send(embed=embed)

#delete event
@bot.event
async def on_message_delete(message):
    if message.author == bot.user:
        return
    else:
        channelSend = bot.get_channel(1045487867188744286)
        embed = discord.Embed(title="Message deleted", description=f"**{message.author}** deleted a message in {message.channel.mention}", color=0xF1C8F6)
        await channelSend.send(embed=embed)

#new member event
@bot.event
async def on_member_join(member: discord.Member):
    channel = bot.get_channel(1046109451779850251)
    await channel.send(f"> Welcome to the ***Coding shelter*** {member.mention}!!! Please read the <#1044575795957473280> and enjoy your stay!")

#member leave event
@bot.event
async def on_member_remove(member: discord.Member):
    mentions = discord.AllowedMentions(
        users=False,
    )
    channel = bot.get_channel(1046109451779850251)
    await channel.send(f"> {member.mention} has left the server, so long friend :(", allowed_mentions=mentions)




#-------------------------------------------------BOT EVENTS END-------------------------------------------------#



# random facts command
@command.command(description="Random weird facts!")
async def weirdfact(interaction: discord.Interaction):
    lines = open('E:\\Python\\bot\\facts.txt').read().splitlines()
    file = random.choice(lines)
    await interaction.response.send_message(file)

# ping command
@command.command(description="Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! `{round(bot.latency * 1000)}ms`")

# no ping command
@command.command(description="A command thats does not ping me")
async def dontpingme(interaction: discord.Interaction, self: discord.User):
    mentions = discord.AllowedMentions(
        users=False,
    )
    await interaction.response.send_message(f"Hello, {interaction.user.mention}", allowed_mentions=mentions)

#purge command
@command.command(description="Purge messages!")
@app_commands.default_permissions(manage_messages=True)
@app_commands.describe(amount='Input amount', reason='Input reason')
async def purge(interaction: discord.Interaction, amount: int, reason: str):
    await interaction.response.defer(ephemeral=False)
    await interaction.channel.purge(limit=amount)
    await interaction.followup.send(f"{interaction.user.mention} Deleted `{amount}` messages in {interaction.channel.mention}\nFor reason: `{reason}`")

#kick command
@command.command(description="Kick a member from the server!")
@app_commands.default_permissions(kick_members=True)
@app_commands.describe(member='Input member', reason='Input reason')
async def kick(interaction: discord.Interaction, member: discord.Member, reason: str):
    channel = bot.get_channel(1045798126352597043)
    await interaction.response.defer(ephemeral=False)
    await member.kick(reason=reason)
    await interaction.followup.send(f"> {interaction.user.mention} Kicked **{member}** For reason: `{reason}`")
    mentions = discord.AllowedMentions(
        users=False,
    )
    await channel.send(f"> {interaction.user.mention} Kicked **{member}** For reason: `{reason}`", allowed_mentions=mentions)

#ban command
@command.command(description="Ban a member from the server!")
@app_commands.default_permissions(ban_members=False)
@app_commands.describe(member='Input member', reason='Input reason')
async def ban(interaction: discord.Interaction, member: discord.Member, reason: str):
    channel = bot.get_channel(1045798126352597043)
    await interaction.response.defer(ephemeral=False)
    await member.ban(reason=reason)
    await interaction.followup.send(f"> {interaction.user.mention} Banned **{member}** For reason: `{reason}`\n **UserID:** *{member.id}*")
    mentions = discord.AllowedMentions(
        users=False,
    )
    await channel.send(f"> {interaction.user.mention} Banned **{member}** For reason: `{reason}`\n **UserID:** *{member.id}*", allowed_mentions=mentions)

#unban command
@command.command(description="Unban a member from the server!")
@app_commands.default_permissions(ban_members=True)
@app_commands.describe(member='Input member', reason='Input reason')
@discord.app_commands.checks.has_role(1044687367061131406)
async def unban(interaction: discord.Interaction, member: discord.User, reason: str):
        channel = bot.get_channel(1045798126352597043)
        await interaction.response.defer(ephemeral=False)
        await interaction.guild.unban(member, reason=reason)
        await interaction.followup.send(f"> {interaction.user.mention} Unbanned **{member}**")
        mentions = discord.AllowedMentions(
        users=False,
        )
        await channel.send(f"> {interaction.user.mention} Unbanned **{member}**", allowed_mentions=mentions)
@unban.error
async def unban_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.errors.MissingRole):
        await interaction.response.send_message("You don't have permission to use this command!")
    
#duck facts command
@command.command(description="Random duck facts!")
async def duckfact(interaction: discord.Interaction):
    lines = open('E:\\Python\\bot\\ducks.txt').read().splitlines()
    file = random.choice(lines)
    await interaction.response.send_message(file)




#-------------------------------------------------MUSIC START-------------------------------------------------#



#music help command
@command.command(description="Music!")
async def musichelp(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=False)
    embed = discord.Embed(title="Music commands", description="", color=0xF1C8F6)
    embed.add_field(name="/play", value="`Play a song`!", inline=True)
    embed.add_field(name="/stop", value="`Stop playing a song`!", inline=True)
    embed.add_field(name="/pause", value="`Pause the song!`", inline=True)
    embed.add_field(name="/resume", value="`Resume the song!`", inline=True)
    embed.add_field(name="/skip", value="`Skip the song!`", inline=True)
    embed.add_field(name="/loop", value="`loop current song or queue!`", inline=True)
    embed.add_field(name="/queue", value="`Show the queue!`", inline=True)
    embed.add_field(name="/clear", value="`Clear the queue!`", inline=True)
    embed.add_field(name="/volume", value="`Change the volume!`", inline=True)
    embed.add_field(name="/current", value="`Show the song that is currently playing!`", inline=True)
    embed.set_footer(text="Music commands requested by: " + str(interaction.user))
    await interaction.followup.send(embed=embed)

#play music command
class Button(discord.ui.View):
    def __init__(self, tracks: list[wavelink.YouTubeTrack]):
        super().__init__()
        for index, track in enumerate(tracks):
            button = Music(track, index+1)
            self.add_item(button)
        self.add_item(Cancel())

class Cancel(discord.ui.Button):
    def __init__(self):
        super().__init__(label='cancel', style=discord.ButtonStyle.red)
        self.value = None

    async def callback(self, interaction: Interaction):
        channel = interaction.user.voice.channel
        embed = discord.Embed(color=0xF1C8F6)
        embed.add_field(name="**Cancelled!**", value=f"Search cancelled! Bot has been *disconnected* from {channel.mention}", inline=True)
        await interaction.response.send_message(embed=embed)
        await interaction.guild.voice_client.disconnect()
        self.value = True
        self.disabled = True
        await interaction.message.edit(view=None)

@command.command(description="Play music!")
async def play(interaction: discord.Interaction, song: str):
    tracks = await wavelink.YouTubeTrack.search(query=song, return_first=False)
    view = Button(tracks[:4])
    guild = interaction.guild
    Str = ""
    var = "**Choose a track:**"
    backslash = '\n'
    for count, track in enumerate(tracks[:4], start=1):
        Str += f"\n**{count}: **{track.title}"
        embed = discord.Embed(color=0xF1C8F6)
        embed.add_field(name=var + backslash, value=Str, inline=False)
        embed.set_footer(text=f"Requested by: {interaction.user.name}")
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/1011681612729155644/1023548857948315678/250591C7-A4B6-4792-8302-318183D8D296.gif')
    await interaction.response.send_message(embed=embed, view=view)
    if not guild.voice_client:
        vc: wavelink.player = guild.voice_client or await interaction.user.voice.channel.connect(cls=wavelink.Player)
    else:
        vc: wavelink.Player = guild.voice_client

class Music(discord.ui.Button):
    def __init__(self, track: wavelink.YouTubeTrack, label: int):
        super().__init__(label=label, style=discord.ButtonStyle.blurple)
        self.track = track

    async def callback(self, interaction: discord.Interaction):
        guild = interaction.guild
        vc: wavelink.Player = guild.voice_client
        if vc.queue.is_empty and not vc.is_playing():
            td_str = str(timedelta(seconds=self.track.length))
            x = td_str.split(':')
            await vc.play(self.track)
            embed=discord.Embed(title="Song", url=f"{self.track.uri}", color=0xF1C8F6)
            embed.add_field(name="**Now playing:**", value=f"`{self.track}`", inline=True)
            embed.add_field(name="**Song duration:**", value=f"`{x[1]}:{x[2]}`", inline=True)
            embed.add_field(name="\u200b", value=f"\u200b", inline=False)
            embed.add_field(name="**Uploaded by:**", value=f"`{self.track.author}`", inline=False)
            embed.set_footer(text=f"Requested by: {interaction.user.name}")
            embed.set_image(url = self.track.thumbnail)
            await interaction.response.send_message(embed=embed)
            self.disabled = True
            await interaction.message.edit(view=None)
        else:
            await vc.queue.put_wait((self.track))
            embed = discord.Embed(color=0xF1C8F6)
            embed.add_field(name="**Added to queue:**", value=self.track.title, inline=False)
            await interaction.response.send_message(embed=embed)
        
        vc.ctx = guild
        vc.loop = False


#skip music command
@command.command(description="Skip the song!")
async def skip(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=False)
    guild = interaction.guild
    vc: wavelink.Player = guild.voice_client
    if not vc.queue.is_empty:
        embed = discord.Embed(color=0xF1C8F6)
        embed.add_field(name="**Skip!**", value="\n Skipped the song!", inline=False)
        await vc.stop()
        await interaction.followup.send(embed=embed)
        
#show queue command
@command.command(description="See current songs in the queue")
async def queue(interaction: discord.Interaction):
    guild = interaction.guild
    vc = wavelink.Player = guild.voice_client

    if vc.queue.is_empty:
        embed = discord.Embed(color=0xF1C8F6)
        embed.add_field(
            name="**Queue!**", value="No tracks in the queue!", inline=False)
        await interaction.response.send_message(embed=embed)

    else:
        lijst = []
        queue = vc.queue.copy()
        count = 0
        for song in queue:
            count += 1
            lijst.append(f"**{count}:** {song.title}")

        embed = discord.Embed(color=0xF1C8F6)
        embed.add_field(name="**Queue:**",
                        value=('\n'.join(lijst)), inline=False)
        await interaction.response.send_message(embed=embed)

#change volume command
@command.command(description="Change music volume!")
async def volume(interaction: discord.Interaction , volume: int):
    guild = interaction.guild
    vc: wavelink.Player = guild.voice_client
    channel = interaction.channel

    if volume > 100:
        await interaction.response.defer(ephemeral=False)
        channel = interaction.channel
        embed = discord.Embed(color=0xF1C8F6)
        embed.add_field(name=f"**Beware!**", value=f"The max volume is **100%!**", inline=False)
        await channel.send(embed=embed)
        return
    else:
        await interaction.response.defer(ephemeral=False)
        await vc.set_volume(volume)
        embed = discord.Embed(color=0xF1C8F6)
        embed.add_field(
            name=f"**Volume change!**", value=f"Changed volume to: **{volume}%**", inline=False)
        await interaction.followup.send(embed=embed)

#leave voice channel command
@command.command(description="Make bot leave voice channel!")
async def leave(interaction: discord.Interaction): #stops working after restart, disconnect bot manually
    channel = interaction.user.voice.channel
    await interaction.response.defer(ephemeral=False)
    await interaction.guild.voice_client.disconnect() 
    embed = discord.Embed(color=0xF1C8F6)
    embed.add_field(name=f"**Beware!**", value=f"*Disconnected* from: {channel.mention}", inline=False)
    await interaction.followup.send(embed=embed)

#track end event
@bot.event
async def on_wavelink_track_end(player: wavelink.Player, track: wavelink.Track, reason):
    channel = bot.get_channel(1049729674005184532)
    ctx = player.ctx
    vc: player = ctx.voice_client
    if not player.queue.is_empty:
        next_song = await vc.queue.get_wait()
        await vc.play(next_song)
        embed = discord.Embed(color=0xF1C8F6)
        embed.add_field(name=f"**Now playing:**", value=f"{next_song}", inline=False)
        await channel.send(embed=embed)
    else:
        await vc.stop()

#pause music command
@command.command(description="Pause the song!")
async def pause(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=False)
    guild = interaction.guild
    vc: wavelink.Player = guild.voice_client
    await vc.set_pause(True)
    embed = discord.Embed(color=0xF1C8F6)
    embed.add_field(name="**Pause!**", value="\n The song has been paused!", inline=False)
    await interaction.followup.send(embed=embed)

#resume music command
@command.command(description="Resume the song!")
async def resume(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=False)
    guild = interaction.guild
    vc: wavelink.Player = guild.voice_client
    await vc.set_pause(False)
    embed = discord.Embed(color=0xF1C8F6)
    embed.add_field(name="**Resume!**", value="\n The song has been resumed!", inline=False)
    await interaction.followup.send(embed=embed)

#clear queue command
@command.command(description="Clear the queue!")
async def clear(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=False)
    guild = interaction.guild
    vc: wavelink.Player = guild.voice_client
    vc.queue.reset()
    embed = discord.Embed(color=0xF1C8F6)
    embed.add_field(name="**Clear!**", value="\n The queue has been cleared!", inline=False)
    await interaction.followup.send(embed=embed)

#show current song command
@command.command(description="Show the song that is currently playing!")
async def current(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=False)
    guild = interaction.guild
    vc: wavelink.Player = guild.voice_client
    if vc.is_playing():
        embed = discord.Embed(color=0xF1C8F6)
        embed.add_field(name=f"**Now playing:**", value=f"`{vc.source.title}`", inline=False)
        await interaction.followup.send(embed=embed)
    else:
       if not vc.is_playing():
        embed = discord.Embed(color=0xF1C8F6)
        embed.add_field(name=f"**Now playing:**", value=f"`No song is currently playing!`", inline=False)
        await interaction.followup.send(embed=embed)

#stop music command
@command.command(description="Stop the song!")
async def stop(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=False)
    guild = interaction.guild
    vc: wavelink.Player = guild.voice_client
    await vc.stop()
    embed = discord.Embed(color=0xF1C8F6)
    embed.add_field(name="**Stop!**", value="\n The song has been stopped!", inline=False)
    await interaction.followup.send(embed=embed)



#-------------------------------------------------MUSIC END-------------------------------------------------#



#mute members command
@command.command(description="Mute a member!")
@app_commands.default_permissions(administrator=True)
async def mute(interaction: discord.Interaction, member: discord.Member, reason: str):
    role = discord.utils.get(member.guild.roles, name="Muted")
    await member.add_roles(role)
    await interaction.response.send_message(f">>> {member.mention} has been **muted!**\n reason: `{reason}`")

#unmute members command
@command.command(description="Unmute a member!")
@app_commands.default_permissions(administrator=True)
async def unmute(interaction: discord.Interaction, member: discord.Member):
    role = discord.utils.get(member.guild.roles, name="Muted")
    await member.remove_roles(role)
    await interaction.response.send_message(f">>> {member.mention} has been **unmuted!**")









#-------------------------------------------------TESTING-------------------------------------------------#



#stats command
@command.command(description="Bot stats!")
async def stats(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    embed = discord.Embed(title="Bot stats", description="", color=0x00ff00)
    embed.add_field(name="Bot owner", value="Vabolos#1999", inline=True)
    embed.add_field(name="Bot uptime", value=f"{round(bot.latency * 1000)}ms", inline=True)
    embed.add_field(name="Bot latency", value=f"{round(bot.latency * 1000)}ms", inline=True)
    embed.set_footer(text="Stats requested by: " + str(interaction.user))
    await interaction.followup.send(embed=embed)
    


#loop music command
@command.command(description="Loop the queue!")
async def repeat(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=False)
    guild = interaction.guild
    vc: wavelink.Player = guild.voice_client
    vc.loop = True
    embed = discord.Embed(color=0xF1C8F6)
    embed.add_field(name="**Loop!**", value="\n The current song is on repeat!", inline=False)
    await interaction.followup.send(embed=embed)



#repeat command testing
class Bot(commands.Bot):
    def __init__(self):
        super().__init__()

class Repeat(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='Repeat', style=discord.ButtonStyle.blurple)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        embedOne = discord.Embed(title='Repeat song', description='Confirmed!', color=0xF1C8F6)
        await interaction.message.edit(embed=embedOne)
        self.loop = True
        self.value = True
        self.stop()
        await interaction.message.edit(view=None)

    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        embedTwo = discord.Embed(title='Repeat song', description='Cancelled!', color=0xF1C8F6)
        await interaction.message.edit(embed=embedTwo)
        self.value = False
        self.stop()
        await interaction.message.edit(view=None, delete_after=5)

@command.command(description="Button testing!")
async def testrepeat(interaction: discord.Interaction):
    view = Repeat()
    embed = discord.Embed(title='Repeat song', description='Do you want to repeat the current song?', color=0xF1C8F6)
    await interaction.response.send_message(embed=embed, view=view)



#-------------------------------------------------TESTING-------------------------------------------------#



bot.run(TOKEN)
