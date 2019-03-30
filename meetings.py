# meetings_list = [{'name': 'google interview!', 'duration': 1}, . . . . ]

from itertools import combinations

# O(n log n) time complexity
def max_meetings(meetings_list, hours):
    if not isinstance(meetings_list, list):
        raise Exception('Meetings list must be of type list')
    if not isinstance(hours, (int, float)):
        raise Exception('hours must be of type int or float')
    if not meetings_list or len(meetings_list) == 0:
        raise Exception('meetings list must contain 1 or more meeting items')
    if hours == 0:
        return [] # return an empty list because we have no free time
    
    if sum([meeting['duration'] for meeting in meetings_list]) <= hours:
        return meetings_list
    else:
        used = 0
        can_attend = []
        # now add meeting elements to a list while we have available hours
        for meeting in list(sorted(meetings_list, key = lambda m: m['duration'])):
            if used + meeting['duration'] <= hours:
                can_attend.append(meeting)
                used += meeting['duration']
                if used == hours:
                    break
    return can_attend

# O(n^c) where n = len(meetings_list) and c = number of combinations * m = len of combination
def max_used_hours(meetings_list, hours):
    if not isinstance(meetings_list, list):
        raise Exception('Meetings list must be of type list')
    if not isinstance(hours, (int, float)):
        raise Exception('hours must be of type int or float')
    if not meetings_list or len(meetings_list) == 0:
        raise Exception('meetings list must contain 1 or more meeting items')
    if hours == 0:
        return [] # return an empty list because we have no free time
    if hours > 24:
        raise Exception('Hours cannot exceed 24 hours')
    
    if sum([meeting['duration'] for meeting in meetings_list]) <= hours:
        return meetings_list
    else:
        last_found = 0
        for r in range(len(meetings_list), 0, -1):
            for combo in combinations(meetings_list, r):
                if last_found <= hours:
                    last_found = sum([meet['duration'] for meet in combo])
                    if last_found == hours:
                        return list(combo)
                last_found = 0
                    
        


meetings_dict = [{'name': 'morning stand up', 'duration': .5},{'name': 'google interview!', 'duration': 1}, {'name': 'meeting 1', 'duration': 2}, {'name': 'sales call', 'duration': .5}]


print(max_meetings(meetings_dict, 2))
print(max_used_hours(meetings_dict, 3))
print(max_used_hours(meetings_dict, 2))
print(max_used_hours(meetings_dict, 3.5))
print(max_used_hours(meetings_dict, 4.5))
print(max_used_hours(meetings_dict, .5))
print(max_used_hours(meetings_dict, 1))