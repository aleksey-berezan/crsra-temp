# python3

from queue import Queue

def last_finish_time(q):
    return q.queue[0]

# main
size, count = map(int, input().strip().split())

# parse
requests = []
for i in range(count):
    arrival_time, process_time = map(int, input().strip().split())
    requests.append((arrival_time, process_time))

q = Queue(size)
responses = []
current_time = 0
last_arrival = -1
finish_time = 0

# simualte
for arrival, size in requests:
    same_arrival = last_arrival != -1 and last_arrival == arrival
    last_arrival = arrival
    if q.full() and last_finish_time(q) == 0:
        q.get_nowait()
    # read
    if same_arrival:
        if q.full():
            responses.append(-1)
        else:
            finish_time = max(finish_time, arrival) #idle
            responses.append(finish_time)
            finish_time += size
            q.put_nowait(finish_time)
        continue

    # process
    while not q.empty():
        if last_finish_time(q) <= arrival:
            q.get_nowait()
        else:
            break

    if q.full():
        responses.append(-1)
    else:
        finish_time = max(finish_time, arrival) #idle
        responses.append(finish_time)
        finish_time += size
        q.put_nowait(finish_time)
    continue

# output
for response in responses:
    print(response)
