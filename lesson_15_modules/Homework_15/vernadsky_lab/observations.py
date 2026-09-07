from .minerals import get_mineral
from datetime import datetime

_journal=[]

def record(researcher,mineral_name,note):
    if not get_mineral(mineral_name):
        return f"Mineral {mineral_name} not exists in catalog"
    _journal.append({"researcher":researcher,"mineral":mineral_name,"note":note,"date":datetime.now()})
    return f"Observatio added {researcher} -> {mineral_name}"

def get_observations(mineral_name: str = None):
    if not _journal:
        return []
    if mineral_name is not None:
        return [obs for obs in _journal if obs["mineral"] == mineral_name]

    return _journal