import doctest
import sys

class MinHeap(object):
    """
    Min Heap
    >>> bh = MinHeap()
    >>> bh.buildHeap([9,5,14,18,-17,27,33,19,11,21])
    >>> bh.findMin()
    -17
    >>> bh.delMin()
    -17
    >>> bh.list[1:]
    [5, 9, 14, 11, 21, 27, 33, 19, 18]
    >>> bh.insert(-100)
    >>> bh.delMin()
    -100
    """

    def __init__(self):
        """
        add self.list 0 with initialization in order to divide
        """
        self.list = [-sys.maxsize]
        self.size = 0


    def insert(self, k):
        """
        Insert element to the MinBinaryHeap
        """
        self.list.append(k)
        self.size += 1
        self.perc_up(self.size)


    def findMin(self):
        """
        Find the min element and return it
        """
        return self.list[1]


    def delMin(self):
        """
        Delete the min element
        and return it
        """
        retrival = self.list[1]
        self.size -= 1
        self.list[1] = self.list[-1]
        self.list.pop()
        self.perc_down(1)

        return retrival


    def isEmpty(self):
        """
        Return if the MinBinaryHeap is empty
        """
        return self.size == 0

    def __len__(self):
        """
        Magic Method: return the length of MinBinaryHeap
        """
        return self.size


    def buildHeap(self, alist):
        """
        Build a MinBinaryHeap from alist which is a collection of data
        """
        self.list.extend(alist)
        self.size = len(alist)

        i = self.size//2
        while i > 0:
            self.perc_down(i)
            i -= 1

    def perc_up(self, i):
        """"
        perc_up i
        """
        while i//2>0:
            if self.list[i] < self.list[i // 2]:
                self.list[i], self.list[i // 2] = self.list[i // 2], self.list[i]
            i = i // 2

    def perc_down(self, i):
        """
        perc down i
        """
        while (i * 2) <= self.size:
            mc = self.minChild(i)
            if self.list[i] > self.list[mc]:
                self.list[i], self.list[mc] = self.list[mc], self.list[i]
            i = mc

    def minChild(self, i):
        """
        find the min child
        """
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.list[i * 2] < self.list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def __iter__(self):
        return iter(self.list[1:])


class MaxHeap(object):
    """
    Max Heap
    >>> bh = MaxHeap()
    >>> bh.buildHeap([9,5,14,18,-17,27,33,19,11,21])
    >>> bh.delMax()
    33
    >>> bh.insert(100)
    >>> bh.delMax()
    100
    >>> len(bh)
    9
    """

    def __init__(self):
        self.heap = MinHeap()

    def insert(self, k):
        self.heap.insert(-k)

    def delMax(self):
        return -self.heap.delMin()

    def buildHeap(self, alist):
        for i in range(len(alist)):
            alist[i] = -alist[i]
        self.heap.buildHeap(alist)

    def findMax(self):
        return -self.heap.findMin()

    def __len__(self):
        return self.heap.size

    def __iter__(self):
        for i in range(1, self.heap.size+1):
            yield -self.heap.list[i]


def median_maintenance(textfile):

    min_heap = MinHeap()  # > medium
    max_heap = MaxHeap()  # < medium

    medians = []
    count = 0

    with open(textfile) as infile:
        for line in infile:
            item = int(line)
            count += 1

            # Step 1: Add next item to one of the hepas
            # special case: initialize
            if count == 1:
                max_heap.insert(item)
            else:
                if item < max_heap.findMax():
                    max_heap.insert(item)
                else:
                    min_heap.insert(item)

            # Step2: Balance the heap
            if abs(len(max_heap) - len(min_heap)) > 1:
                if len(max_heap) > len(min_heap):
                    min_heap.insert(max_heap.delMax())
                else:
                    max_heap.insert(min_heap.delMin())

            # Step3: calculate median
            if len(max_heap) == len(min_heap):
                median = max_heap.findMax()
            else:
                if len(max_heap) > len(min_heap):
                    median = max_heap.findMax()
                else:
                    median = min_heap.findMin()

            medians.append(median)

            # test
            #for element in max_heap:
            #    print(element, end=' ')
            #for element in min_heap:
            #    print(element, end=' ')
            #print('total elem:',len(max_heap)+len(min_heap))


    return medians

if __name__ == '__main__':
    # doctest.testmod(verbose=True)
    #textfile = 'SmallTest.txt'
    textfile = 'Median.txt'
    medians = median_maintenance(textfile)
    answer = sum(medians)%10000
    print(answer)









