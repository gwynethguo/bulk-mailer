from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class EmailHistoryPostRequest(BaseModel):
    email_id: UUID
    recipient_email: str
    department_code: str
    email_subject: str
    status: Optional[str] = "SENT"


class EmailHistoryGetResponse(BaseModel):
    email_id: str
    email_subject: str
    department_code: str
    latest_created_at: datetime


class EmailHistoryGetResponseList(BaseModel):
    message: str
    data: List[EmailHistoryGetResponse]


class EmailCountGetResponse(BaseModel):
    count: int
    department_code: str


class EmailCountGetResponseList(BaseModel):
    message: str
    data: List[EmailCountGetResponse]


class TrackingCounterGetResponse(BaseModel):
    count: int
    email_id: str
    email_subject: str


class TrackingCounterGetResponseList(BaseModel):
    message: str
    data: List[TrackingCounterGetResponse]
