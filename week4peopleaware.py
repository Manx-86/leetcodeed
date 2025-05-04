class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        day = 1
        forget_map, spread_map = defaultdict(int), defaultdict(list)
        active = 0
        spread_map[day + delay] = [day, 1]
        while (spread_map or forget_map) and day <= n:
            if day in forget_map:
                active -= forget_map.pop(day)
            if day in spread_map:
                start_day, num_people = spread_map[day]
                forget_map[start_day + forget] = num_people
                active += num_people
                spread_map.pop(day)
            if active:
                spread_map[day + delay] = [day, active]
            day += 1
        total_known = sum(forget_map.values()) + sum(count for _, count in spread_map.values())
        return total_known % (10**9 + 7)
