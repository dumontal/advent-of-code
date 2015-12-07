#!/usr/bin/env python

import re

class Reindeer:

    def __init__(self, name, speed, active_time, rest_time):
        self.name = name
        self.speed = speed
        self.active_time = active_time
        self.rest_time = rest_time
        
        self.distance = 0
        self.score = 0

        self.turn = 'active'
        self.remaining = active_time

    def next_sec(self):
        if self.remaining > 0:
            self.remaining -= 1

            if self.turn == 'active':
                self.distance += self.speed

        if self.remaining == 0:
            if self.turn == 'active':
                self.turn = 'rest'
                self.remaining = self.rest_time
            else:
                self.turn = 'active'
                self.remaining = self.active_time

        return self.distance

    def award_point(self):
        self.score += 1

def parse_line(line):
    m = re.match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)
    return Reindeer(m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)))

def run_race_step(reindeers):
    max_distance = max(map(lambda r: r.next_sec(), reindeers))

    for reindeer in reindeers:
        if reindeer.distance == max_distance:
            reindeer.award_point()

if __name__ == '__main__':
    
    reindeers = set()

    f = open('data')
    for line in f:
        reindeers.add(parse_line(line))

    f.close()

    for step in range(2503):
        run_race_step(reindeers)

    distance = max(map(lambda r: r.distance, reindeers))
    print('[Part 1] Winner has run for', distance, 'km.')

    score = max(map(lambda r: r.score, reindeers))
    print('[Part 2] Winner has a score of', score, 'points.')
