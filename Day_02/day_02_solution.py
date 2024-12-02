# Solution for Day 02 of Advent of Code 2024

# Part 1
def is_report_safe(report):
    increasing, decreasing = True, True
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if abs(diff) < 1 or abs(diff) > 3:  # within [1, 3] or [-1, -3]
            return False
        if diff > 0:
            decreasing = False
        if diff < 0:
            increasing = False
        if not (increasing or decreasing):
            return False
    return True


with open("Day_02/input_data.txt", "r") as file:
    reports = [list(map(int, line.strip().split())) for line in file]

safe_report_count = sum(is_report_safe(report) for report in reports)
print("Number of safe reports:", safe_report_count)


# Part 2
def is_report_safe_with_dampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]  # remove one element at index i
        if is_report_safe(modified_report):
            return True
    return False


dampener_safe_count = 0
for report in reports:
    if is_report_safe(report) or is_report_safe_with_dampener(report):
        dampener_safe_count += 1

print(f"Number of safe reports with dampener: {dampener_safe_count}")

with open("Day_02/output_data.txt", "w") as file:
    file.write(f"Number of safe reports:, {safe_report_count}\n")
    file.write(f"Number of safe reports with dampener: {dampener_safe_count}")
