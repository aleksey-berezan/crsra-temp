# python3

from queue import Queue

Test = False
# main
# 13
size, count = 2,3
requests = [(0,1),(0,1),(0,1)]

# 15
# size, count = 1,3
# requests = [(0,2),(1,4),(5,3)]

# 18
size, count = 2,3
requests = [(0,1),(3,1),(10,1)]

Test = False

# main
if not Test:
    size, count = map(int, input().strip().split())
    # parse
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append((arrival_time, process_time))

def last(q):
    return q.queue[q.qsize() - 1]

# process
# if len(requests) == 0:
#     return

q = Queue(size)
responses = []# finish_time
finish_time = 0
last_arrival = -1
current_time = 0
i = 0
for arrival_time, process_time in requests:
    i += 1
    # if process_time == 0:# and not q.empty() and last(q)[1] == 0:
    #     finish_time = max(arrival_time, finish_time)
    #     responses.append(finish_time)
    #     continue
    if q.full() and last(q)[1] == 0:
        q.get_nowait()
    read_same = last_arrival == arrival_time
    if read_same:
        if q.full():
            responses.append(-1)
        else:
            finish_time = max(arrival_time, finish_time)
            responses.append(finish_time)
            finish_time += process_time
            q.put_nowait((finish_time, process_time))
        continue

    last_arrival = arrival_time

    if q.full() and arrival_time < finish_time:
        responses.append(-1)
        continue

    while not q.empty():
        start_time, packet_process_time = last(q)
        if finish_time <= start_time:# active processing
            q.get_nowait()
        elif arrival_time > finish_time:# idle processing
            q.get_nowait()
        else:
            break

    if q.full():
        responses.append(-1)
        continue

    finish_time = max(arrival_time, finish_time)
    responses.append(finish_time)
    finish_time += process_time
    q.put_nowait((finish_time, process_time))

for response in responses:
    print(response)