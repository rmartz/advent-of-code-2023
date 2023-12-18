from collections import namedtuple
import sys

MapRange = namedtuple("MapRange", ["range", "offset"])

input = (line.strip() for line in sys.stdin)

def parse_seed_ranges(input):
    vals = input.split(" ")
    for i in range(0, len(vals), 2):  
        start, size = [int(val) for val in vals[i:i+2]]
        yield range(start, start + size)

seed_ranges = list(parse_seed_ranges(next(input)[7:]))

next(input)

def read_block_to_map_ranges(input):
    for line in input:
        if line == "":
            return
        destination, source, size = [int(val) for val in line.split(" ")]
        yield MapRange(range(source, source + size), destination - source)

def lookup_range_maps(source_ranges, destination_map_ranges):
    for source in source_ranges:
        low = source.start
        for destination_map_range in destination_map_ranges:
            destination = destination_map_range.range
            if low < destination.start and source.stop >= destination.start:
                # Subranges that don't overlap with a destination map are unchanged
                # Part of the source range is before this destination range, so yield a fixed subrange for the unmapped portion
                yield range(low, destination.start)
                low = destination.stop
            if source.stop <= destination.start:
                # We've moved past destinations that we can overlap with, no more overlaps
                break
            
            overlap_start = max(source.start, destination.start) + destination_map_range.offset
            overlap_end = min(source.stop, destination.stop) + destination_map_range.offset
            if overlap_start <= overlap_end:
                yield range(overlap_start, overlap_end) 
                low = destination.stop

        if low < source.stop:
            yield range(low, source.stop)

def lookup_all_range_maps(source_ranges, destination_map_ranges):
    for map_ranges in destination_map_ranges:
        source_ranges = list(lookup_range_maps(source_ranges, map_ranges))
    return source_ranges

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
    lookup_maps.append(
        sorted(read_block_to_map_ranges(input), key=lambda map_range: map_range.range.start)
    )

seed_subranges = (lookup_all_range_maps([seed_range], lookup_maps) for seed_range in seed_ranges)
seed_subrange_mins = (min(subrange.start for subrange in subranges) for subranges in seed_subranges)

print(min(seed_subrange_mins))