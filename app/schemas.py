# app/schemas.py

from pydantic import BaseModel
from typing import Optional

# Schema for creating a new country configuration
class ConfigurationCreate(BaseModel):
    country_code: str
    business_name: Optional[str] = None
    registration_number: Optional[str] = None
    # Add other fields as necessary

# Schema for updating an existing country configuration
class ConfigurationUpdate(BaseModel):
    country_code: str
    business_name: Optional[str] = None
    registration_number: Optional[str] = None
    # Add other fields as necessary

# Schema for reading a country configuration
class Configuration(BaseModel):
    country_code: str
    business_name: Optional[str] = None
    registration_number: Optional[str] = None
    # Add other fields as necessary

    class Config:
        orm_mode: bool = True
