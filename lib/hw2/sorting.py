# 1. selection sort
# 2. insertion sort
# 3. shell sort
# 4. heap sort
# 5. merge sort
# 6. quick sort

import time
import random
import matplotlib.pyplot as plt


class Sorting(object):
    """Sorting class

    """

    def __init__(self):
        self.id = []
        self.helper = []

    def sort_init(self, N):
        """initialize the data structure

        """
        try:
            self.id = random.sample(range(1, N ** 3), N)
        except ValueError:
            print('Sample size exceeded population size.')

        self.id = [random.randint(0, N - 1) for i in range(N)]
        self.helper = [0] * N

    def get_id(self):
        """initialize the data structure

        """

        return self.id

    def selection_sort(self):
        """Selection sort algorithm is an
        in-place comparison sort. It has O(n^2) time complexity, making it
        inefficient on large lists, and generally performs worse than the
        similar insertion sort

        """
        for i_idx, i_item in enumerate(self.id):
            min = i_idx

            for j_idx in range(i_idx+1, len(self.id)):

                if self.id[j_idx] < self.id[min]:
                    min = j_idx

            # swap
            temp = self.id[i_idx]
            self.id[i_idx] = self.id[min]
            self.id[min] = temp

        return self.id

    def insertion_sort(self):
        """Insertion sort is a simple sorting algorithm that builds the final
        sorted array (or list) one item at a time. More efficient in practice
        than most other simple quadratic (i.e., O(n^2)) algorithms such as
        selection sort or bubble sort specifically an

        """
        for i_indx in range(len(self.id)):
            key = self.id[i_indx]

            j_indx = i_indx - 1

            while j_indx >= 0 and key < self.id[j_indx]:
                self.id[j_indx + 1] = self.id[j_indx]
                j_indx -= 1
                self.id[j_indx + 1] = key

        return self.id

    def shell_sort(self):
        """Shell sort also known as  or Shell's method, is an in-place comparison sort.
        It can be seen as either a generalization of sorting by exchange (bubble sort)
        or sorting by insertion (insertion sort).

        """
        size = len(self.id)
        leap = size//2

        while leap > 0:

            for i_indx in range(leap, size):
                temp = self.id[i_indx]
                j_indx = i_indx

                while j_indx >= leap and self.id[j_indx - leap] > temp:
                    self.id[j_indx] = self.id[j_indx - leap]
                    j_indx -= leap
                self.id[j_indx] = temp

            leap //= 2

        return self.id

    def heap_setup(self, n, index):

        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and self.id[index] < self.id[left]:
            largest = left

        if right < n and self.id[largest] < self.id[right]:
            largest = right

        if largest != index:
            self.id[index], self.id[largest] = self.id[largest], self.id[index]
            self.heap_setup(n, largest)

        return self.get_id()

    def heap_sort(self):
        """Heapsort is an improved selection sort: it divides its input into a sorted
        and an unsorted region, and it iteratively shrinks the unsorted region by
        extracting the largest element and moving that to the sorted region.

        """
        size = len(self.id)
        for i in range(size, -1, -1):
            self.heap_setup(size, i)

        for i in range(size - 1, 0, -1):
            self.id[i], self.id[0] = self.id[0], self.id[i]           # for the swap
            self.heap_setup(i, 0)

        return self.id

    def sort(self, low, high):
        if high <= low:
            return
        mid = low + (high - low)//2
        self.sort(low, mid)
        self.sort(mid + 1, high)
        self.merge(low, mid, high)

        return self.id

    def merge(self, low, mid, high):
        i = low
        j = mid + 1
        k = low
        while k <= high:
            self.helper[k] = self.id[k]
            k += 1
        k = low
        while k <= high:
            if i > mid:
                self.id[k] = self.helper[j]
                j += 1
            elif j > high:
                self.id[k] = self.helper[i]
                i += 1
            elif self.helper[j] < self.helper[i]:
                self.id[k] = self.helper[j]
                j += 1
            else:
                self.id[k] = self.helper[i]
                i += 1
            k += 1
        return self.id

    def merge_sort(self):
        """Merge sort is a divide and conquer algorithm that was invented
        by John von Neumann in 1945. Most implementations produce a stable
        sort, which means that the implementation preserves the input order
        of equal elements in the sorted output.
        """
        self.sort(0, len(self.id) - 1)
        return self.id

    def partition(self, low, high):
        index = (low - 1)
        pivot = self.id[high]

        for j in range(low, high):
            if self.id[j] <= pivot:
                index = index + 1
                self.id[index], self.id[j] = self.id[j], self.id[index]

        self.id[index + 1], self.id[high] = self.id[high], self.id[index + 1]
        return index + 1

    def quick(self, low, high):
        if low < high:
            partit = self.partition(low, high)
            self.quick(low, partit - 1)
            self.quick(partit + 1, high)
        return self.id

    def quick_sort(self):
        """Quicksort (sometimes called partition-exchange sort) is an efficient
        sorting algorithm. Developed by Tony Hoare in 1959. It is still a commonly
        used algorithm for sorting. When implemented well, it can be about two or
        three times faster than its main competitors, merge sort and heapsort.

        """
        random.shuffle(self.id)
        self.quick(0, len(self.id) - 1)

        return self.id


if __name__ == "__main__":

        # iteration
        set_sz = [10]
        timing = [[], [], [], [], [], [], []]
        x = [10 ** i for i in range(0, 5)]

        for set_sz in x:
            sort = Sorting()
            sort.sort_init(set_sz)
            t0 = time.time()
            sort.selection_sort()
            t1 = time.time()
            tot_time = t1 - t0
            timing[0].append(tot_time)
            print(tot_time)

        for set_sz in x:
            sort = Sorting()
            sort.sort_init(set_sz)
            t0 = time.time()
            sort.insertion_sort()
            t1 = time.time()
            tot_time = t1 - t0
            timing[1].append(tot_time)
            print(tot_time)

        for set_sz in x:
            sort = Sorting()
            sort.sort_init(set_sz)
            t0 = time.time()
            sort.shell_sort()
            t1 = time.time()
            tot_time = t1 - t0
            timing[2].append(tot_time)
            print(tot_time)

        for set_sz in x:
            sort = Sorting()
            sort.sort_init(set_sz)
            t0 = time.time()
            sort.heap_sort()
            t1 = time.time()
            tot_time = t1 - t0
            timing[3].append(tot_time)
            print(tot_time)

        for set_sz in x:
            sort = Sorting()
            sort.sort_init(set_sz)
            t0 = time.time()
            sort.merge_sort()
            t1 = time.time()
            tot_time = t1 - t0
            timing[4].append(tot_time)
            print(tot_time)

        for set_sz in x:
            sort = Sorting()
            sort.sort_init(set_sz)
            t0 = time.time()
            sort.quick_sort()
            t1 = time.time()
            tot_time = t1 - t0
            timing[5].append(tot_time)
            print(tot_time)

        for set_sz in x:
            sort = Sorting()
            sort.sort_init(set_sz)
            t0 = time.time()
            x.sort()
            t1 = time.time()
            tot_time = t1 - t0
            timing[6].append(tot_time)
            print(tot_time)

    # this plots things in log scale (pls google it), you need to add matplotlib
    # to your virtualenv first!

    # plot also python's sorted() function to see how well you do.

        plt.plot(x, timing[0], label="Selection Sort")
        plt.plot(x, timing[1], label="Insertion Sort")
        plt.plot(x, timing[2], label="Shell Sort")
        plt.plot(x, timing[3], label="Heap Sort")
        plt.plot(x, timing[4], label="Merge Sort")
        plt.plot(x, timing[5], label="Selection Sort")
        plt.plot(x, timing[6], label="Python Sort")
        plt.legend()
        plt.xscale('log')
        plt.yscale('log')
        plt.title('log')
        plt.ylabel('Timing')
        plt.xlabel('Set Size')
        plt.show()
