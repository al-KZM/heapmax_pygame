#!/usr/bin/python3

##############################################
#
# gui.py
# heapmax
#
##############################################

import random
import math
import pygame
import heapmax

pygame.init()
size = width,height = 800,800
margin = 50
y_offset = 200

screen = pygame.display.set_mode(size)

black = (0,0,0)
white = (255,255,255)

font  = pygame.font.Font('freesansbold.ttf', 32)
font2  = pygame.font.Font('freesansbold.ttf', 16)

def draw_heapmax(screen, heap_size, arr, i=0, root_x=None, root_y=None, frame_x_start=margin, max_width=width-margin*2):
    if i >= heap_size:
        return True

    if not root_x:
        root_y, root_x = y_offset, frame_x_start + (max_width // 2)
    levels = math.ceil(math.log(heap_size, 2))
    if levels == 0: levels = 1
    shift  = (max_width//2) // levels

    left_x = root_x - shift
    right_x = root_x + shift

    step_down = (height-margin-y_offset)//levels
    new_y = root_y + step_down

    text = font.render(str(arr[i]), True, black, white)
    rect = text.get_rect()
    rect.center = (root_x, root_y)
    screen.blit(text, rect)

    if heapmax.left(i) < heap_size:
        pygame.draw.line(screen, black, (root_x, root_y+15), (left_x, new_y))
    if heapmax.right(i) < heap_size:
        pygame.draw.line(screen, black, (root_x, root_y+15), (right_x, new_y))

    draw_heapmax(screen, heap_size, arr, heapmax.left(i), left_x, new_y, frame_x_start, max_width//2)
    draw_heapmax(screen, heap_size, arr, heapmax.right(i), right_x, new_y, frame_x_start+max_width//2, max_width//2)


class Array:
    def __init__(self, size, max_capacity, limit=15):
        self.size = size
        self.arr = [0 for _ in range(size)]
        self.limit = limit
        self.capacity = max_capacity

    def randomize(self):
        print(self.arr)
        for i in range(self.size):
            choices = [i for i in range(1, self.limit+1) if i not in self.arr]

            self.arr[i] = random.choice(choices)

    def increase_size(self):
        if self.size >= self.capacity:
            print("Max capacity reached")
            return False
        self.size += 1
        return True

    def get_random_ix(self):
        return random.choice(list(range(self.size)))


arr = Array(7, 10)
arr.randomize()
heap_size = len(arr.arr)
modified = False

valid_msg = f"Heap is valid"
valid = font2.render(valid_msg, True, (0,255,0), white)
last_action = "Nothing"

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.KEYDOWN:
            modified = True
            if ev.key == pygame.K_h:
                last_action = "Heapify 0"
                heapmax.heapify(arr.arr, heap_size, 0)
            elif ev.key == pygame.K_b:
                last_action = "Build heapmax"
                heapmax.build_max_heap(arr.arr, heap_size)
            elif ev.key == pygame.K_r:
                last_action = "Randomize array"
                arr.randomize()
                heap_size = len(arr.arr)
            elif ev.key == pygame.K_m:
                last_action = "Extract maximum"
                heap_size = heapmax.heap_extract_max(arr.arr, heap_size)
            elif ev.key == pygame.K_p:
                print("Arr:", arr.arr)
                print("Heap size:", heap_size)
            elif ev.key == pygame.K_s:
                last_action = "Heapsort"
                heapmax.heapsort(arr.arr, heap_size)
            elif ev.key == pygame.K_i:
                last_action = "Increase random key"
                key_to_increase = arr.get_random_ix()
                increment = random.randint(1, 10)
                new_val = arr.arr[key_to_increase] + increment
                heapmax.increase_key(arr.arr, key_to_increase, new_val)
            elif ev.key == pygame.K_n: # Insert a random key
                last_action = "Insert random key"
                new_key = random.randint(1,50)
                if arr.increase_size():
                    heap_size = heapmax.insert_maxheap(arr.arr, heap_size, new_key)

    screen.fill(white)

    info_msg = f"{arr.arr} (Heap size: {heap_size}) Last action performed: {last_action}"
    info = font2.render(info_msg, True, black, white)
    info_rect = info.get_rect()
    info_rect.center = (400,100)
    screen.blit(info, info_rect)

    if modified:
        if heapmax.check_valid_heap(arr.arr, heap_size):
            valid_msg = f"Heap is valid"
            valid = font2.render(valid_msg, True, (0,255,0), white)
        else:
            valid_msg = f"Heap is invalid"
            valid = font2.render(valid_msg, True, (255,0,0), white)

    valid_rect = valid.get_rect()
    valid_rect.center = (500,200)
    screen.blit(valid, valid_rect)


    draw_heapmax(screen, heap_size, arr.arr)
    pygame.display.flip()


