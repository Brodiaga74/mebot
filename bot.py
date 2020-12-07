#-*- coding: utf-8 -*-
import discord
import random
import time
import requests
import googletrans
import wikipedia
import pyshorteners
#import requests
#from PIL import Image,ImageFont,ImageDraw
from discord.ext import commands
from discord.utils import get
from googletrans import Translator
from datetime import datetime
import json
import asyncio
import pymongo
from pymongo import MongoClient
import sqlite3

import nekos

import psutil as ps
from Cybernator import Paginator

from psutil import virtual_memory
from io import BytesIO
from PIL import Image,ImageFilter,ImageDraw,ImageFont







client = commands.Bot(command_prefix = '?', intents = discord.Intents.all())
client.remove_command('help')



@client.event
async def on_ready():
	print('Connected!')
	await client.change_presence( status = discord.Status.do_not_disturb, activity = discord.Game('YouTube Community'))
    
@client.command()
async def NAME(ctx):
  await ctx.send('Привет!')


#kick
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def kick(ctx,member: discord.Member,*,reason = None):
	emb = discord.Embed(title = 'Пользователь был удалён с сервера', colour = discord.Color.red())
	await member.kick(reason = reason)
	emb.set_author(name=member.name, icon_url = member.avatar_url)
	emb.add_field(name = 'Информация', value = 'Удалённый пользователь: {}'.format(member.mention))
	await ctx.send(embed = emb)

#ban
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def ban(ctx,member: discord.Member,*,reason = None):
	emb = discord.Embed(title = 'Пользователь забанен!', colour = discord.Color.red())
	await member.ban(reason = reason)
	emb.set_author(name=member.name, icon_url = member.avatar_url)
	emb.add_field(name = 'Информация', value = 'Забаненный пользователь: {}'.format(member.mention))
	await ctx.send(embed = emb)

#Авто-выдача роли
@client.event
async def on_member_join(member):
	channel = client.get_channel(785465494047293482)
	role = discord.utils.get(member.guild.roles, id = 785465365119500309)
	await member.add_roles(role)
	await channel.send(embed = discord.Embed(description = f'<a:GO_9266_arrow_rainbow:771687279671377920>  Здравствуй, {member.mention}\n<a:QUFixed:679590287613362176>  Добро пожаловать на сервер **YouTube Community**. Сервер лампового общения. На нём вы можете поиграть с участниками, посмотреть их видосики или же просто пообщаться в чате!\n<a:QUCok234:677846343938473984> После авторизации не забудь прочитать правила сервера <#785467131545255966>! \n<a:QUhi:677846306621751302> Приятного общения!', color = #00ffe6))

#Авто-выдача роли
@client.event
async def on_member_remove(member):
	channel = client.get_channel(747820695014080512)
	await channel.send(embed = discord.Embed(description = f'``{member.name}``,покинул нас. \nЧтож, удачи ему.', color = 0xFFA500))

client.run("Nzg1NDY3NzQ0MDEwMjQwMDIx.X84R1w.HBps5Dje3eivrW9DW6aFJ_GayXo")