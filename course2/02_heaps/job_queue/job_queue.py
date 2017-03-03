# python3

class Worker:
    def __init__(self, index):
        self.index = index
        self.next_free_time = 0
        self.arr_index = index

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def get_next_worker(self, workers):
        return workers[0]

    def is_earlier(self, left, right):
        if left.next_free_time == right.next_free_time:
            return left.index < right.index
        return left.next_free_time < right.next_free_time

    def swap(self, workers, left_arr_index, right_arr_index):
        workers[left_arr_index], workers[right_arr_index] = workers[right_arr_index], workers[left_arr_index]
        workers[left_arr_index].arr_index = left_arr_index
        workers[right_arr_index].arr_index = right_arr_index

    def sift_worker_down(self, workers, worker):
        count = len(workers)

        while worker != None:

            w_arr_index = worker.arr_index
            min_arr_index = w_arr_index

            lc_arr_index = (w_arr_index + 1) * 2 - 1
            rc_arr_index = (w_arr_index + 1) * 2

            if lc_arr_index < count and self.is_earlier(workers[lc_arr_index], workers[min_arr_index]):
                min_arr_index = lc_arr_index

            if rc_arr_index < count and self.is_earlier(workers[rc_arr_index], workers[min_arr_index]):
                min_arr_index = rc_arr_index

            if min_arr_index != w_arr_index:
                worker = workers[w_arr_index]
                self.swap(workers, min_arr_index, w_arr_index)
            else:
                worker = None

    def assign_jobs(self):
        self.assigned_workers = [0] * len(self.jobs)
        self.start_times = [0] * len(self.jobs)
        workers = [None] * self.num_workers
        for i in range(0, self.num_workers):
            workers[i] = Worker(i)

        for i in range(len(self.jobs)):
          worker = self.get_next_worker(workers)
          self.assigned_workers[i] = worker.index
          self.start_times[i] = worker.next_free_time

          worker.next_free_time += self.jobs[i]
          self.sift_worker_down(workers, worker)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

# main
job_queue = JobQueue()
job_queue.solve()

