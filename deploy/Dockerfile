# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip uninstall -y telethon


# 
COPY ./ /code/

ARG TG_API_ID_ARG
ARG TG_API_HASH_ARG

ARG S3_ACCESS_ID_ARG
ARG S3_ACCESS_KEY_ARG

ENV TG_API_ID=$TG_API_ID_ARG
ENV TG_API_HASH=$TG_API_HASH_ARG
ENV S3_ACCESS_ID=$S3_ACCESS_ID_ARG
ENV S3_ACCESS_KEY=$S3_ACCESS_KEY_ARG

# 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
