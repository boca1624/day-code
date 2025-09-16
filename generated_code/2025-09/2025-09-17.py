def activity_selection_activities(n, start_times, end_times):
    activities = sorted(zip(start_times, end_times), key=lambda x: x[1])
    count = 1
    last_end_time = activities[0][1]

    for start, end in activities:
        if start > last_end_time:
            count += 1
            last_end_time = end

    return count

# 示例使用
n = 6
start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]
print(activity_selection_activities(n, start_times, end_times))
