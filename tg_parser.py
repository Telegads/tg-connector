from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.errors import FloodError
from telethon import TelegramClient
from datetime import datetime, timedelta
import logging
import utils
import config
import random

# Настраиваем логи
logging.basicConfig(filename='errors.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.ERROR)
logger = logging.getLogger()


async def get_info(client, channel_name):
    """ Сам париснг канала """
    channel_ent = await client.get_entity(channel_name)
    channel = await client(GetFullChannelRequest(channel=channel_ent))

    avatar = channel.full_chat.chat_photo
    about = channel.full_chat.about
    name = channel.chats[0].title
    subs_count = channel.full_chat.participants_count

    date_3_days = datetime.utcnow() - timedelta(days=30)
    date_1_day = datetime.utcnow() - timedelta(days=1)
    views_last_30_days = 0
    posts_last_30_days = 0
    views_last_day = 0

    async for post in client.iter_messages(channel_ent):
        if post.date.replace(tzinfo=None) < date_3_days:
            break
        else:
            views_last_30_days += post.views or 0
            posts_last_30_days += 1
            if post.date.replace(tzinfo=None) >= date_1_day:
                views_last_day += post.views or 0

    info = {
        'description': about,
        'name': name,
        'subs_count': subs_count,
        'views_last_30_days': views_last_30_days,
        'posts_last_30_days': posts_last_30_days,
        'views_last_day': views_last_day
    }
    return info


async def fetch(client, channel_name):
    """ Ловим ошибки """
    try:
        r = await get_info(client, channel_name)
        return r
    except Exception as ex:
        if isinstance(ex, FloodError):
            return 'flood'
        logger.error(f'Channel {channel_name}: {ex}')
        return {'error': 'Internal error'}


async def build_client(session_file):
    client = TelegramClient(session_file, config.api_id, config.api_hash)
    try:
        await client.connect()
        await client.get_me()
    except:
        return False
    return client


def get_session_file():
    """ Выбирает файл сессии из папки """
    sessions = utils.get_sessions()
    if not sessions:
        return
    session = random.choice(sessions)
    return session


async def retrieve_channel_info(channel_name):
    """ Создаем клиент Telethon и собираем информацию """
    session = get_session_file()
    if not session:
        return {'error': 'No accounts alive'}

    while True:
        client = await build_client(session)
        async with client:
            d = await fetch(client, channel_name)

        if d == 'flood':
            logger.debug(f'{session} flood error')
            utils.mark_bad_session(session)
            session = get_session_file()
            if not session:
                return {'error': 'No accounts alive'}
            continue

        return d
