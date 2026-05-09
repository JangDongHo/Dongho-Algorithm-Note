def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = []
    time = 0
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        
        else:
            time += 5
            
            if len(cache) == cacheSize:
                cache.pop(0)
            
            cache.append(city)
                
    return time