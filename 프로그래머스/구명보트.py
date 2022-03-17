def solution(people, limit):
    people.sort()

    left = 0
    right = len(people) - 1
    count = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        count += 1

    return count

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))