from fastapi import FastAPI, HTTPException
from tg_parser import retrieve_channel_info

app = FastAPI()


@app.get('/get_info/{channel_name}')
async def get_info(channel_name):
    try:
        d = await retrieve_channel_info(channel_name)
        return d
    except Exception as error:
        raise HTTPException(status_code=500, detail=repr(error))

