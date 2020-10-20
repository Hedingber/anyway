import logging

import random

from anyway.app_and_db import db
from anyway.models import (
    AccidentMarker,
    AccidentWeather,
)


def ensure_accidents_weather_data(filters=None):
    """
    :param filters: additional filters to add to the query that lists accident markers to add weather data to
    This is used mainly for testing
    :returns: int representing the number of accidents to which weather data was added
    """
    logging.info(f"Ensuring accidents weather data {filters}")
    query = db.session.query(AccidentMarker).filter(AccidentMarker.weather_data == None)
    if filters:
        query = query.filter(*filters)
    accident_markers_to_update = query.all()
    if accident_markers_to_update:
        logging.debug(f"Found accident markers without weather data. {len(accident_markers_to_update)}")
    accidents_weather_data = []
    for accident_marker in query.all():
        rain_rate = compute_accident_rain_data(accident_marker.latitude,
                                               accident_marker.longitude,
                                               accident_marker.accident_hour,
                                               accident_marker.accident_minute)
        accidents_weather_data.append({
                "accident_id": accident_marker.id,
                "provider_and_id": accident_marker.provider_and_id,
                "provider_code": accident_marker.provider_code,
                "accident_year": accident_marker.accident_year,
                "rain_rate": rain_rate,
            }
        )
    if accidents_weather_data:
        logging.debug(f"Adding weather data to accidents. {accidents_weather_data}")
        db.session.bulk_insert_mappings(AccidentWeather, accidents_weather_data)
        db.session.commit()
    logging.debug("Finished filling accidents weather data")
    return len(accident_markers_to_update) if accident_markers_to_update else 0


def compute_accident_rain_data(latitude, longitude, hour, minute):
    logging.info("Mocking rain data computation")
    return random.randint(0, 10)

