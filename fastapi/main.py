import hashlib
import hmac
from os import environ
from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel
import databases

from models import webhook_event_table

ZOOM_WEBHOOK_KEY = environ.get("ZOOM_WEBHOOK_KEY")

DB_USER = environ.get("DB_USER", "user")
DB_PASSWORD = environ.get("DB_PASS", "password")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_NAME = environ.get("DB_NAME", "localhost")
SQLALCHEMY_DATABASE_URL = (
    f"postgresql+aiopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)

database = databases.Database(SQLALCHEMY_DATABASE_URL)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


class ZoomWebhookItem(BaseModel):
    payload: dict
    event: str
    event_ts: int


@app.post("/zoom/webhook")
async def zoom_webhook(webhook_item: ZoomWebhookItem):
    if webhook_item.event == 'endpoint.url_validation':
        message = hmac.new(bytes(ZOOM_WEBHOOK_KEY, 'latin-1'),
                           msg=bytes(webhook_item.payload['plainToken'], 'latin-1'),
                           digestmod=hashlib.sha256).hexdigest()
        return {
            'plainToken': webhook_item.payload['plainToken'],
            'encryptedToken': message
        }

    query = webhook_event_table.insert().values(**webhook_item.model_dump())
    webhook_id = await database.execute(query)

    return {}

'''
PoC - Proof of concept
'''

'''
ORM - sync
CORE - async
'''
