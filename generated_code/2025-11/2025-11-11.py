def activity_selection(activities):
    n = len(activities)
    activities.sort(key=lambda x: x[1])
    selected_activities = []
    last_end_time = 0

    for activity in activities:
        if activity[0] >= last_end_time:
            selected_activities.append(activity)
            last_end_time = activity[1]

    return selected_activities

# 示例
activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9)]
print(activity_selection(activities))
