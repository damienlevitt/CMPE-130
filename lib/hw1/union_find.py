

# 1. quick-find
# 2. quick-union
# 3. weighted QU
# 4. QU + path compression
# 5. weighted QU + path compression

import time
import random
import matplotlib.pyplot as plt


class UF(object):
    """Union Find class

    """
    def __init__(self):
        self.id = []

    def qf_init(self, N):
        """initialize the data structure

        """
        for x in range(N):
            self.id.append(x)

    def qf_union(self, p, q):
        """Union operation for Quick-Find Algorithm.

        connect p and q. You need to
        change all entries with id[p] to id[q]
        (linear number of array accesses)

        """
        pid = self.id[p]
        qid = self.id[q]

        for x in range(len(self.id)):
                if self.id[x] == pid:           # if the id at x is equal to the id at p then x and p are connected
                    self.id[x] = qid            # there for you can set x to q

    def qf_connected(self, p, q):
        """Find operation for Quick-Find Algorithm.
        simply test whether p and q are connected
        """
        return self.id[p] == self.id[q]

    def get_root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def qu_union(self, p, q):
        """Union operation for Quick-Union Algorithm.
         connect p and q.

         """
        root_p = self.get_root(p)
        self.id[root_p] = self.get_root(q)

    def qu_connected(self, p, q):
        """Find operation for Quick-Union Algorithm.
         test whether p and q are connected

         """
        return self.get_root(p) == self.get_root(q)

    def wqu_union(self, p, q):
        """Union operation for Weighted Quick-Union Algorithm.
         connect p and q.

         """
        if self.id[self.get_root(p)] < self.id[self.get_root(q)]:
            self.id[self.get_root(p)] = self.get_root(q)
            self.id[self.get_root(q)] += self.id[self.get_root(p)]
        else:
            self.id[self.get_root(q)] = self.get_root(p)
            self.id[self.get_root(p)] += self.id[self.get_root(q)]

    def wqu_connected(self, p, q):
        """Find operation for Weighted Quick-Union Algorithm.
         test whether p and q are connected

         """
        return self.get_root(p) == self.get_root(q)

    def pqu_union(self, p, q):
        """Union operation for path compressed Quick-Union Algorithm.
         connect p and q.

         """
        root_of_p = self.get_root(p)
        self.id[root_of_p] = self.get_root(q)

    def pqu_connected(self, p, q):
        """Find operation for path compressed Quick-Union Algorithm.
         test whether p and q are connected

         """

        return self.get_root(p) == self.get_root(q)

    def wpqu_union(self, p, q):
        """Union operation for Weighted path compressed Quick-Union Algorithm.
         connect p and q.

         """

        if self.id[self.get_root(p)] < self.id[self.get_root(q)]:
            self.id[self.get_root(p)] = self.get_root(q)
            self.id[self.get_root(q)] += self.id[self.get_root(p)]
        else:
            self.id[self.get_root(q)] = self.get_root(p)
            self.id[self.get_root(p)] += self.id[self.get_root(q)]

    def wpqu_connected(self, p, q):
        """Find operation for Weighted path compressed Quick-Union Algorithm.
         test whether p and q are connected

         """

        return self.get_root(p) == self.get_root(q)


if __name__ == "__main__":

    # iteration
    set_szs = [10]
    timing = []

    # gives the timing for union operation only, you might want to do this for all functions you wrote.

    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            inodes.qf_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    # this plots things in log scale (pls google it), you need to add matplotlib to your virtualenv first!
    plt.plot(set_szs, timing)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('log')
    plt.ylabel('some numbers')
    plt.show()
