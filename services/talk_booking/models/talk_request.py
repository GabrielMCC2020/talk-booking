import datetime

from enum import Enum
from pydantic import BaseModel, PositiveInt
from .address import Address

class TalkRequestStatus(str, Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"

class TalkRequest(BaseModel):
    id: str
    event_time: datetime.datetime
    address: Address
    topic: str
    duration_in_minutes: PositiveInt
    requester: EmailStr
    status: TalkRequestStatus
    

