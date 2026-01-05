def bubble_sort(items, comp=lambda x, y: x > y):
    items = items[:]
    n = len(items)
    for i in range(n-1):
        # 交换标志位，如果遍历途中出现了一次都未反转的情况，则可提前终止外侧循环
        swapped = False
        for j in range(n-1-i):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        if not swapped:
            break
    return items    