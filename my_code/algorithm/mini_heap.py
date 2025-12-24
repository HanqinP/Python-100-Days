class MinHeap:
    def __init__(self):
        self.a = [] # 用数组表示完全二叉树

    def push(self, x):
        # 1) 先把元素插到“最后”（数组末尾）
        self.a.append(x)
        # 2) 上滤：与父节点比较，若更小就上移
        i = len(self.a) - 1
        while i > 0:
            p = (i - 1) // 2
            if self.a[i] < self.a[p]:
                self.a[i], self.a[p] = self.a[p], self.a[i]
                i = p
            else:
                break
        pass

    def pop(self):
        if not self.a:
            raise IndexError("pop from empty heap")
        # 1) 堆顶与最后一个交换，将最后一个弹出
        self.a[0], self.a[-1] = self.a[-1], self.a[0]
        top = self.a.pop()
        # 2) 下滤：将新的堆顶下沉到合适的位置
        i = 0
        n = len(self.a)
        while True:
            l = 2*i + 1
            r = l + 1
            smallest = i
            if l < n and self.a[l] < self.a[smallest]:
                smallest = l
            if r < n and self.a[r] < self.a[smallest]:
                smallest = r
            if smallest == i:
                break
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            i = smallest
        return top
        


myheap = MinHeap()
myheap.push(2)
myheap.push(1)
myheap.push(3)
myheap.push(25)
myheap.push(12)
myheap.push(29)
myheap.push(46)
print(myheap.a)
print(myheap.pop())