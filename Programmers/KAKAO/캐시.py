def solution(cacheSize, cities):
    answer = 0

    if cacheSize == 0:
        return len(cities)*5

    cache = []
    for c in range(len(cities)):
        cities[c] = cities[c].upper()

    for i in cities:
        print(cache)
        if len(cache) < cacheSize and i not in cache:
            cache.append(i)
            answer += 5
            continue

        if i in cache:
            cache.pop(cache.index(i))
            cache.append(i)
            answer += 1
        else:
            cache.pop(0)
            cache.append(i)
            answer += 5

    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))