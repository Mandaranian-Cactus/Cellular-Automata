import pygame
import sys
import random

class Map:
    def __init__(self, block_w, w, h, birth_limit, death_limit, birth_chance):
        self.block_w = block_w
        self.w = w
        self.h = h
        self.map = [[0 for i in range(w)] for i in range(h)]
        self.birth_limit = birth_limit
        self.death_limit = death_limit
        self.birth_chance = birth_chance

    def birth_begin(self):
        for y in range(self.h):
            for x in range(self.w):
                result = random.choices([1,0], [self.birth_chance, 1 - self.birth_chance])[0]
                self.map[y][x] = result

    def draw(self, screen):
        for y in range(self.h):
            for x in range(self.w):
                if self.map[y][x]: color = (0,0,0)
                else: color = (255,255,255)

                pygame.draw.rect(screen.screen, color, (x * self.block_w, y * self.block_w, self.block_w, self.block_w))

    def check_neighbors(self, x, y):
        neighbor_cnt = 0
        try:
            if self.map[y][x - 1]: neighbor_cnt += 1
        except IndexError:
            neighbor_cnt += 1
            pass
        try:
            if self.map[y][x + 1]: neighbor_cnt += 1
        except IndexError:
            neighbor_cnt += 1
            pass
        try:
            if self.map[y - 1][x]: neighbor_cnt += 1
        except IndexError:
            neighbor_cnt += 1
            pass
        try:
            if self.map[y + 1][x]: neighbor_cnt += 1
        except IndexError:
            neighbor_cnt += 1
            pass
        try:
            if self.map[y - 1][x + 1]: neighbor_cnt += 1
        except IndexError:
            neighbor_cnt += 1
            pass
        try:
            if self.map[y - 1][x - 1]: neighbor_cnt += 1
        except IndexError:
            neighbor_cnt += 1
            pass
        try:
            if self.map[y + 1][x + 1]: neighbor_cnt += 1
        except IndexError:
            neighbor_cnt += 1
            pass
        try:
            if self.map[y + 1][x - 1]: neighbor_cnt += 1
        except IndexError:
            neighbor_cnt += 1
            pass

        return neighbor_cnt

    def next_gen(self, gen_steps):
        new_map = [["" for i in range(self.w)] for i in range(self.h)]

        for y in range(self.h):
            for x in range(self.w):
                neighbor_cnt = self.check_neighbors(x, y)

                if self.map[y][x]:
                    if neighbor_cnt < self.death_limit:
                        new_map[y][x] = 0
                    else:
                        new_map[y][x] = 1
                else:
                    if neighbor_cnt > self.birth_limit:
                        new_map[y][x] = 1
                    else:
                        new_map[y][x] = 0

        self.map = new_map

    def find_opening(self):
        for y in range(self.h):
            for x in range(self.w):
                if not self.map[y][x]:
                    return x, y

    def cover_borders(self):
        for i in range(self.w):
            self.map[0][i] = 1
            self.map[self.h - 1][i] = 1

        for i in range(self.h):
            self.map[i][0] = 1
            self.map[i][self.w - 1] = 1
