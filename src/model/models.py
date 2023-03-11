from typing import Optional
from pydantic import BaseModel


class InputData(BaseModel):
    enrollee_id: int
    city_development_index: Optional[float]
    gender: Optional[str]
    relevent_experience: Optional[str]
    enrolled_university: Optional[str]
    education_level: Optional[str]
    major_discipline: Optional[str]
    experience: Optional[str]
    company_size: Optional[str]
    company_type: Optional[str]
    last_new_job: Optional[str]
    training_hours: Optional[int]
