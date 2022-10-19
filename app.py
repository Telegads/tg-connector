from fastapi import FastAPI
from tg_parser import retrieve_channel_info

app = FastAPI()


@app.get('/get_info/{channel_name}')
async def get_info(channel_name):
    d = await retrieve_channel_info(channel_name)
    return d
