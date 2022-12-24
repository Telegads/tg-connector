from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import sentry_sdk

from tg_parser import retrieve_channel_info, BadChannelNameException, NoAccents

origins = [
    "https://staging.telegads.uz",
    "https://telegads.uz",
    "http://localhost:3000",
]


sentry_sdk.init(
    dsn="https://a13775155f784e40b04cd464bb87e01f@o4503987462537216.ingest.sentry.io/4504251833581568",
    # disable performance monitoring
    traces_sample_rate=0.0,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/get_info/{channel_name}')
async def get_info(channel_name):
    try:
        d = await retrieve_channel_info(channel_name)
        return {
            "status": "success",
            "data": d
            }
    except NoAccents:
        return {
            "status": "error",
            "data": "No accounts left"
        }
    except BadChannelNameException as error:
        return {
            "status": "error",
            "data": "Channel not found"
        } 
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="Internal error"
        )

