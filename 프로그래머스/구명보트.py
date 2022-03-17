def solution(people, limit):
    people.sort()

    start = 0
    end = len(people) - 1
    count = 0

    while start <= end:
        if people[start] + people[end] > limit:
            end -= 1
            count += 1
        else:
            start += 1
            end -= 1
            count += 1

    return count

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))