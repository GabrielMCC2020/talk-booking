import datetime
from typing import List # new

from pydantic import BaseModel, EmailStr, PositiveInt

from .responses import TalkRequestDetails, TalkRequestList

from models import Address
from models.talk_request import TalkRequestStatus

from fastapi import FastAPI
app = FastAPI()

@app.get("/talk-requests/", status_code=200,
response_model=TalkRequestList)
def talk_requests():
    return {
        "results": [
            {
                "id": "unique_id",
                "event_time": "2021-10-03T10:30:00",
                "address": {
                    "street": "Sunny street 42",
                    "city": "Sunny city 42000",
                    "state": "Sunny state",
                    "country": "Sunny country",
                },
            "topic": "FastAPI with Pydantic",
            "status": "PENDING",
            "duration_in_minutes": 45,
            "requester": "john@doe.com",
        }
    ]
}    

class TalkRequestDetails(BaseModel):
    id: str
    event_time: datetime.datetime
    address: Address
    topic: str
    duration_in_minutes: PositiveInt
    requester: EmailStr
    status: TalkRequestStatus
    
# new
class TalkRequestList(BaseModel):
    results: List[TalkRequestDetails]


