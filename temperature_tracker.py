# Temperature Tracker
print("=== 3-DAY TEMPERATURE LOGGER ===")

day1 = float(input("Day 1 temp (°C): "))
day2 = float(input("Day 2 temp (°C): "))
day3 = float(input("Day 3 temp (°C): "))

average = (day1 + day2 + day3) / 3
print(f"\nAverage temperature: {average:.1f}°C")
print(f"Highest: {max(day1, day2, day3)}°C")
print(f"Lowest: {min(day1, day2, day3)}°C")