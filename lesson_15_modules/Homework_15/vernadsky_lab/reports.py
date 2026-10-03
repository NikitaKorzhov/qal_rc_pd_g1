from collections import Counter
from .minerals import MINERAL_CATALOG,get_mineral,show_mineral
from .observations import get_observations

def summary():
    minerals_count = len(MINERAL_CATALOG)
    observations = get_observations()
    obs_count = len(observations)
    
    if obs_count == 0:
        active_researcher = "No observatioms"
    else:
        researchers = [obs["researcher"] for obs in observations]
        active_researcher = Counter(researchers).most_common(1)[0][0]
        
    return f"Minerals in catalog: {minerals_count}\nObservations in journal: {obs_count}\nMost active researcher: {active_researcher}"

def mineral_report(name: str):
    catalog_data = get_mineral(name)
    if catalog_data is None:
        return f"Мінерал '{name}' відсутній у каталозі"
    
    observations = get_observations(name)
    result=f"Report by {name}\n{show_mineral(name)}\n"
    for observation in observations:
        result+=f"[{observation['date']}] {observation['researcher']}, {observation['note']}\n"
    
    return result
    