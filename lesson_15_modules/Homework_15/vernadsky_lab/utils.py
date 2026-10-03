from .minerals import MINERAL_CATALOG

def hardest_minerals(n=3):
    """List of names of n most hard minerals."""
    # mineral_item це кортеж (name, data_dict)
    sorted_minerals = sorted(
        MINERAL_CATALOG.items(),
        key=lambda item: item[1].get('hardness', 0),
        reverse=True
    )
    return [name for name, data in sorted_minerals[:n]]

def search_by_origin(origin_keyword):
    """Search minerals by origin keywords."""
    keyword = origin_keyword.lower()
    result = []
    
    for name, data in MINERAL_CATALOG.items():
        origin_text = data.get('origin', '')
        if keyword in origin_text.lower():
            result.append(name)
            
    return result