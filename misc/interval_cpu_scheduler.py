# CPU single process scheduler for tasks with (start_time, duration_time)

import heapq

def schedule_processes(procs):
    # base case
    if not procs:
        return []
    
    # order of process id
    res = []

    # sort the procs
    triples = sorted ([ (st,dt,i) for i, (st, dt) in enumerate(procs) ], key = lambda x: (x[0], x[1]))
    print(triples)

    hq = []
    i, n = 0, len(triples)
    curr_end = triples[0][0]
    while len(res) < n:
       # push the procs less than the current time into heap
        while i < n and triples[i][0] <= curr_end:
            heapq.heappush(hq, (triples[i][1], triples[i][2]))
            i += 1    

       # pop one and add it to order, update curr_time
        if hq:
            duration, index = heapq.heappop(hq)
            res.append(index)
            curr_end += duration
        elif i < n:
            curr_end = triples[i][0]

    return res

procs = [ [0,2], [4,6], [8,10], [1,9], [1,5], [5,9] ]
print(schedule_processes(procs))

