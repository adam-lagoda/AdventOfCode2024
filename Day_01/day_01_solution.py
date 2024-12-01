# Solution for Day 01 of Advent of Code 2024

# Part 1
def total_distance(list1, list2):
    """Calculate the total difference between two lists of integers."""
    list1.sort()
    list2.sort()
    return sum(abs(a - b) for a, b in zip(list1, list2))


with open("Day_01/input_data.txt", "r") as file:
    distances = [line.strip() for line in file]
    historian_A, historian_B = [], []
    for distance in distances:
        distance_split = distance.split()
        historian_A.append(int(distance_split[0]))
        historian_B.append(int(distance_split[1]))

print("Total Distance:", total_distance(historian_A, historian_B))


# Part 2
def similarity_score(left_list, right_list):
    right_count = {}
    for num in right_list:
        if num in right_count:
            right_count[num] += 1
        else:
            right_count[num] = 1

    score = 0
    for num in left_list:
        if num in right_count:
            score += num * right_count[num]

    return score


print("Similarity Score:", similarity_score(historian_A, historian_B))

# with open("Day_01/output_data.txt", "w") as file:
#     file.write(f"Total Distance: {total_distance(historian_A, historian_B)}\n")
#     file.write(f"Similarity Score: {similarity_score(historian_A, historian_B)}\n")
