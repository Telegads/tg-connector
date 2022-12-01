from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi import status
import sentry_sdk

from tg_parser  import retrieve_channel_info, BadChannelNameException

sentry_sdk.init(
    dsn="https://a13775155f784e40b04cd464bb87e01f@o4503987462537216.ingest.sentry.io/4504251833581568",
    # disable performance monitoring
    traces_sample_rate=0.0,
)

app = FastAPI()

@app.get('/get_info/{channel_name}')
async def get_info(channel_name):
    try:
        d = await retrieve_channel_info(channel_name)
        return d
    except ValueError:
        raise HTTPException(
                status_code=500,
                detail="No accounts left"
            ) 
    except BadChannelNameException as error:
        raise HTTPException(
                status_code=500,
                detail="Channel not found"
            ) 

