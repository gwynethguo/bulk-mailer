from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class EmailHistoryPostRequest(BaseModel):
    """
    Model for POST request to insert email history.
    """
    email_id: UUID
    recipient_email: str
    department_code: str
    email_subject: str
    status: Optional[str] = "SENT"

class EmailHistoryGetResponse(BaseModel):
    """
    Model for GET response of email history.
    """
    email_id: str
    email_subject: str
    department_code: str
    latest_created_at: datetime

class EmailHistoryGetResponseList(BaseModel):
    """
    Model for GET response list of email history.
    """
    message: str
    data: List[EmailHistoryGetResponse]

class EmailCountGetResponse(BaseModel):
    """
    Model for GET response of email count by department.
    """
    count: int
    department_code: str

class EmailCountGetResponseList(BaseModel):
    """
    Model for GET response list of email count by department.
    """
    message: str
    data: List[EmailCountGetResponse]

class TrackingCounterGetResponse(BaseModel):
    """
    Model for GET response of tracking counter.
    """
    count: int
    email_id: str
    email_subject: str
    latest_created_at: datetime

class TrackingCounterGetResponseList(BaseModel):
    """
    Model for GET response list of tracking counter.
    """
    message: str
    data: List[TrackingCounterGetResponse]
