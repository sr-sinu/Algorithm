def solution(start, dest, limit):
    total_cost = 0
    max_station = 0

    for i in range(len(start)):
        ride_cost = 1 + 2 * abs(dest[i] - start[i])
        total_cost += ride_cost
        max_station = max(max_station, start[i], dest[i])
    
    return min(total_cost, limit[max_station])

# Example cases
print(solution([1, 0, 2, 4], [2, 2, 0, 5], [3, 17, 7, 4, 5, 17]))
print(solution([1, 2, 0, 2, 3], [2, 1, 2, 1, 2], [4, 8, 18, 16, 20]))
print(solution([2, 2], [4, 3], [1, 1, 1, 1, 9, 1, 1]))