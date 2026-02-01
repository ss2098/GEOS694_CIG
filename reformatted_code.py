import sys
import math
import random
import os


DATA = [5, 3, 9, 1, 4, 8, 2, 7, 6]


def calc_stuff(nums, do_sort=False, scale=1):
    out = []
    total = 0
    for i in range(len(nums)):
        n = nums[i] * scale
        total += n
        out.append(n)
    if do_sort:
        out.sort()
    avg = total / len(nums)
    return out, avg


def find_extremes(values):
    min_v = float('inf')
    max_v = float('-inf')
    for v in values:
        if v < min_v:
            min_v = v
        if v > max_v:
            max_v = v
    return min_v, max_v


def normalize(values, target_max=1):
    m, m_max = find_extremes(values)
    rng = m_max - m
    norm = []
    for i in range(len(values)):
        if rng == 0:
            norm.append(0)
        else:
            norm.append((values[i] - m) / rng * target_max)
    return norm


def weird_helper(a, b):
    store = []
    if a < b:
        for i in range(a):
            store.append(i * b)
        return store
    else:
        return [math.sqrt(a), math.sqrt(b)]


def generate_random_list(n, max_val=10):
    out = []
    for i in range(n):
        out.append(random.random() * max_val)
    return out


def filter_above_threshold(vals, thresh=5):
    out = []
    for v in vals:
        if v > thresh:
            out.append(v)
    return out


def compute_variance(vals):
    avg = sum(vals) / len(vals)
    total = 0
    for v in vals:
        total += (v - avg)**2
    return total / len(vals)


def print_report(vals, avg, min_v, max_v):
    print("Report")
    print("------")
    print("Values:", vals)
    print("Average:", avg)
    print("Min:", min_v, "Max:", max_v)


def string_maker(n):
    return ",".join(str(i) for i in range(n)) + ","


def take_every_other(vals):
    return list(vals)[::2]


def compute_median(vals):
    s = sorted(vals)
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2
    else:
        return s[mid]


def sum_of_squares(vals):
    total = 0
    for v in vals:
        total += v * v
    return total


def clip_values(vals, lo, hi):
    out = []
    for v in vals:
        if v < lo:
            out.append(lo)
        elif v > hi:
            out.append(hi)
        else:
            out.append(v)
    return out


def check_env():
    if "HOME" in os.environ:
        print("Home exists")
    else:
        print("No home?")


def main():
    print("Starting program")
    scaled, avg = calc_stuff(DATA, do_sort=True, scale=2)
    min_v, max_v = find_extremes(scaled)
    norm = normalize(scaled, target_max=10)
    extra = weird_helper(3, 5)
    print_report(norm, avg, min_v, max_v)
    print("Extra data:", extra)

    rand = generate_random_list(10, 20)
    filtered = filter_above_threshold(rand, 10)
    var = compute_variance(filtered)
    print("Variance:", var)

    s = string_maker(12)
    print("String:", s)

    evens = take_every_other(range(10))
    print("Every other:", evens)

    print("Median:", compute_median([5, 1, 9, 3, 7]))
    print("Sum squares:", sum_of_squares([1, 2, 3]))
    print("Clipped:", clip_values([1, 5, 10, 15], 3, 12))

    check_env()

    if len(sys.argv) > 1:
        print("CLI args found ->", sys.argv)


if __name__ == "__main__":
    main()
