from datetime import datetime

def min_platforms(arrivals, departures):
    arrivals = [datetime.strptime(time.strip(), "%H:%M") for time in arrivals]
    departures = [datetime.strptime(time.strip(), "%H:%M") for time in departures]

    arrivals.sort()
    departures.sort()

    platforms_needed = 0
    max_platforms = 0
    i = 0  
    j = 0  

    while i < len(arrivals):
        if arrivals[i] <= departures[j]:
            platforms_needed += 1  
            i += 1  
        else:
            platforms_needed -= 1  
            j += 1 

        max_platforms = max(max_platforms, platforms_needed)

    return max_platforms


arrivals_input = input("Enter arrival times (comma separated, e.g., 9:00, 9:40): ")
departures_input = input("Enter departure times (comma separated, e.g., 9:10, 12:00): ")

arrivals = arrivals_input.split(",")
departures = departures_input.split(",")

print("Minimum platforms needed:", min_platforms(arrivals, departures))
