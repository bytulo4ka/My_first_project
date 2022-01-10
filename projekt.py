import discord
from credits import token
from discord.ext import commands
import time
from discord.utils import get

data = time.strftime('%d.%m.%Y')
times = '16:00:00'
day = time.strftime('%A')
client = discord.Client()
bot = commands.Bot(command_prefix='!')
reactions = ['✅', '❌', '⏰']

@bot.command()
async def start(ctx):
    while True:
        time_now = time.strftime('%H:%M:%S')
        if time_now == times and day == 'Monday':
            a = await ctx.channel.send('КВ '+ ' ' + data + '  ' + '14:00 МСК отмечаемся :white_check_mark: точно иду, :x: нет не иду, :alarm_clock:   точно не знаю или могу опоздать @everyone')
            for name in reactions:
                emoji = get(ctx.guild.emojis, name=name)
                await a.add_reaction(emoji or name)
        elif time_now == times and day == 'Tuesday':
            b = await ctx.channel.send('КВ'+ ' ' + data + '  ' +'20:00 МСК отмечаемся :white_check_mark: точно иду, :x: нет не иду, :alarm_clock:   точно не знаю или могу опоздать @everyone')
            for name in reactions:
                emoji = get(ctx.guild.emojis, name=name)
                await b.add_reaction(emoji or name)
        elif time_now == times and day == 'Thursday':
            a = await ctx.channel.send('КВ'+ ' ' + data + '  ' +'14:00 МСК отмечаемся :white_check_mark: точно иду, :x: нет не иду, :alarm_clock:   точно не знаю или могу опоздать @everyone')
            for name in reactions:
                emoji = get(ctx.guild.emojis, name=name)
                await a.add_reaction(emoji or name)
            b = await ctx.channel.send('КВ'+ ' ' + data + '  ' +'20:00 МСК отмечаемся :white_check_mark: точно иду, :x: нет не иду, :alarm_clock:   точно не знаю или могу опоздать @everyone')
            for name in reactions:
                emoji = get(ctx.guild.emojis, name=name)
                await b.add_reaction(emoji or name)
        elif time_now == times and day == 'Saturday':
            a = await ctx.channel.send('КВ'+ ' ' + data + '  ' +'14:00 МСК отмечаемся :white_check_mark: точно иду, :x: нет не иду, :alarm_clock:   точно не знаю или могу опоздать @everyone')
            for name in reactions:
                emoji = get(ctx.guild.emojis, name=name)
                await a.add_reaction(emoji or name)
            b = await ctx.channel.send('КВ'+ ' ' + data + '  ' +'20:00 МСК отмечаемся :white_check_mark: точно иду, :x: нет не иду, :alarm_clock:   точно не знаю или могу опоздать @everyone')
            for name in reactions:
                emoji = get(ctx.guild.emojis, name=name)
                await b.add_reaction(emoji or name)
        elif time_now == times and day == 'Sunday':
            a = await ctx.channel.send('КВ '+ ' ' + data + '  ' + '14:00 МСК отмечаемся :white_check_mark: точно иду, :x: нет не иду, :alarm_clock:   точно не знаю или могу опоздать @everyone')
            for name in reactions:
                emoji = get(ctx.guild.emojis, name=name)
                await a.add_reaction(emoji or name)



bot.run(token)