import requests
from cache import Cache

USGS_API_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"
cache = Cache()

def fetch_earthquakes(starttime, endtime):
    cache_key = f"{starttime}_{endtime}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    params = {
        'format': 'geojson',
        'starttime': starttime,
        'endtime': endtime,
        'minmagnitude': 2.0,
        'maxmagnitude': 10.0
    }
    response = requests.get(USGS_API_URL, params=params)
    response.raise_for_status()
    data = response.json()
    cache.set(cache_key, data)
    return data

def filter_felt_reports(data):
    return [eq for eq in data['features'] if eq['properties'].get('felt', 0) >= 10]

def filter_tsunami_alerts(data, state):
    return [
        eq for eq in data['features']
        if eq['properties'].get('tsunami') == 1 and state.lower() in eq['properties'].get('place', '').lower()
    ]
