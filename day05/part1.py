from collections import namedtuple
import sys

MapRange = namedtuple("MapRange", ["range", "offset"])

input = (line.strip() for line in sys.stdin)

seeds = [int(val) for val in next(input)[7:].split(" ")]

next(input)

def read_block_to_map_ranges(input):
    for line in input:
        if line == "":
            return
        destination, source, size = [int(val) for val in line.split(" ")]
        yield MapRange(range(source, source + size), destination - source)

def lookup_map(value, map_ranges):
    for range in map_ranges:
        if value in range.range:
            return value + range.offset
    return value

def lookup_all_maps(value, lookup_maps):
    for map_ranges in lookup_maps:
        value = lookup_map(value, map_ranges)
    return value

sections_headers = [
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:",
]

lookup_maps = []
for section_header in sections_headers:
    header_line = next(input)
    assert header_line == section_header
    lookup_maps.append(list(read_block_to_map_ranges(input)))

seed_locations = (lookup_all_maps(seed, lookup_maps) for seed in seeds)
print(min(seed_locations))