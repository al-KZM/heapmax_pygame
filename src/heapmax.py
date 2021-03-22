#!/usr/bin/python3

##############################################
#
# heapmax.py
# heapmax
#
##############################################
import math

def parent(i):
    return math.floor(i/2)

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def is_leaf(i, size):
    return i > math.floor(size/2)+1

def swap(arr, x1, x2):
    tmp = arr[x1]
    arr[x1] = arr[x2]
    arr[x2] = tmp

def heapify(arr, heap_size, i):
    # Check if i is in the heap
    if i >= heap_size:
        return True

    # Get left and right indexes
    l = left(i)
    r = right(i)

    # Fetch the max between i, left and right
    max_ix = i
    if l < heap_size:
        if arr[l] > arr[i]:
            max_ix = l
        else:
            max_ix = i
    if r < heap_size and arr[r] > arr[max_ix]:
        max_ix = r

    # If i is smaller than one of his children, swap it with the maximum and heapify it again
    if max_ix != i:
        swap(arr, i, max_ix)
        heapify(arr, heap_size, max_ix)


def build_max_heap(arr, heap_size):
    for i in range(heap_size//2, -1, -1):
        heapify(arr, heap_size, i)

def heap_extract_max(arr, heap_size):
    maxv = arr[0]
    arr[0] = arr[heap_size-1]
    heap_size -= 1
    heapify(arr, heap_size, 0)
    return heap_size

def heapsort(arr, heap_size):
    if heap_size <= 0:
        return True

    maxv = arr[0]
    heap_size = heap_extract_max(arr, heap_size)
    arr[heap_size] = maxv
    heapsort(arr, heap_size)

def increase_key(arr, ix, new_val):
    print(f"Increasing the key of {ix} from {arr[ix]} to {new_val}")
    if arr[ix] > new_val:
        return False

    arr[ix] = new_val
    p = parent(ix)
    while arr[ix] > arr[p]:
        swap(arr, ix, p)
        ix = p
        p = parent(p)

def insert_maxheap(arr, heap_size, val):
    print("Appending..")
    heap_size += 1
    arr.append(-math.inf)
    print(arr)
    increase_key(arr, heap_size-1, val)

    return heap_size

def check_valid_heap(arr, heap_size):
    for i in range(heap_size):
        l = left(i)
        r = right(i)

        if l < heap_size and arr[i] < arr[l]:
            return False
        if r < heap_size and arr[i] < arr[r]:
            return False

    return True





