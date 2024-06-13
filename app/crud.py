# app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas

def create_country_configuration(db: Session, config: schemas.ConfigurationCreate):
    db_config = models.CountryConfiguration(**config.dict())
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config

def get_country_configuration(db: Session, country_code: str):
    return db.query(models.CountryConfiguration).filter(models.CountryConfiguration.country_code == country_code).first()

def update_country_configuration(db: Session, config: schemas.ConfigurationUpdate):
    db_config = get_country_configuration(db, config.country_code)
    if db_config:
        for key, value in config.dict(exclude_unset=True).items():
            setattr(db_config, key, value)
        db.commit()
        db.refresh(db_config)
    return db_config

def delete_country_configuration(db: Session, country_code: str):
    db_config = get_country_configuration(db, country_code)
    if db_config:
        db.delete(db_config)
        db.commit()
