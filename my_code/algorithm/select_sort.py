def select_sort(items, comp=lambda x, y: x<y):
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        +3+3