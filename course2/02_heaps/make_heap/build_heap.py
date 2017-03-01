# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def Swap(self, i, j):
    self._swaps.append((i - 1,j - 1))
    self._data[i - 1], self._data[j - 1] = self._data[j - 1], self._data[i - 1]

  def DataLen(self):
    return len(self._data)

  def ItemAt(self, i):
    return self._data[i - 1]

  def InBounds(self, i):
    return i <= self.DataLen()

  def SiftDown(self, j):
    l = j * 2
    r = j * 2 + 1
    min_index = j


    if self.InBounds(l) and self.ItemAt(l) < self.ItemAt(min_index):
      # self.Swap(min_index, l)
      min_index = l

    if self.InBounds(r) and self.ItemAt(r) < self.ItemAt(min_index):
      # self.Swap(min_index, r)
      min_index = r

    if min_index != j:
      self.Swap(j, min_index)
      self.SiftDown(min_index)

  def GenerateSwaps(self):
    l = len(self._data)
    for i in range(l // 2, 0, -1):
      self.SiftDown(i)

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

# main
heap_builder = HeapBuilder()
heap_builder.Solve()
