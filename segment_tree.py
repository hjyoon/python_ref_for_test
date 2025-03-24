class SegmentTree:
    def __init__(self, data):
        self.n = len(data)

        self.size = 1
        while self.size < self.n:
            self.size *= 2

        self.tree = [0] * (2 * self.size)

        self._build(data)

    def _build(self, data):
        for i in range(self.n):
            self.tree[self.size + i] = data[i]

        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, idx, val):
        pos = self.size + idx
        self.tree[pos] = val

        pos //= 2
        while pos >= 1:
            self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]
            pos //= 2

    def query(self, left, right):
        left += self.size
        right += self.size

        result = 0
        while left <= right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 0:
                result += self.tree[right]
                right -= 1

            left //= 2
            right //= 2

        return result


arr = [1, 3, 5, 7, 9, 11]  # 초기 데이터
seg = SegmentTree(arr)

print("query(0,2) =", seg.query(0, 2))  # 1 + 3 + 5 = 9

seg.update(1, 10)

print("query(0,2) =", seg.query(0, 2))  # 1 + 10 + 5 = 16
