# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

class Hashset:
    def __init__(self, capacity):
        self.capacity = capacity
        self.p = 1000000007
        self.x = 263
        self.buckets = [None] * self.capacity

    def hash_code(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self.x + ord(c)) % self.p
        return ans % self.capacity

    def find_internal(self, s):
        h = self.hash_code(s)
        bucket_index = h % self.capacity

        bucket = self.buckets[bucket_index]
        if bucket == None:
            return (None, bucket_index)

        for item in bucket:
            if item == s:
                return (item, bucket_index)
        return (None, bucket_index)

    def find(self, s):
        (item, _) = self.find_internal(s)
        return item != None

    def add(self, s):
        (item, bucket_index) = self.find_internal(s)
        bucket = self.buckets[bucket_index]
        if bucket == None:
            bucket = []
            self.buckets[bucket_index] = bucket

        if item == None:
            bucket.append(s)
            return True

        return False

    def remove(self, s):
        (item, bucket_index) = self.find_internal(s)
        bucket = self.buckets[bucket_index]
        if bucket == None:
            return False
        if item == None:
            return False

        bucket.remove(item)
        if len(bucket) == 0:
            self.buckets[bucket_index] = None

        return True

    def get_bucket(self, bucket_index):
        return self.buckets[bucket_index]

class QueryProcessor:

    def __init__(self, bucket_count):
        self.hashset = Hashset(bucket_count)
        self.elems = []

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            bucket = self.hashset.get_bucket(query.ind)
            if bucket == None:
                print()
            else:
                print(' '.join(reversed(bucket)))
        else:
            # try:
            #     ind = self.elems.index(query.s)
            # except ValueError:
            #     ind = -1
            if query.type == 'find':
                found = self.hashset.find(query.s)
                print("yes" if found else "no")
            elif query.type == 'add':
                self.hashset.add(query.s)
            elif query.type == "del":
                self.hashset.remove(query.s)
            else:
                raise ValueError("Unexpected query {0}: {1}".format(query.type, query.s))

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

bucket_count = int(input())
proc = QueryProcessor(bucket_count)
proc.process_queries()
