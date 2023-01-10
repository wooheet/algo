from heapq import heappush, heappop


def qheapq(queries):
    q = []
    removed = set()

    for query in queries:
        if query[0] == '3':
            while True:
                if q[0] in removed:
                    heappop(q)
                else:
                    yield q[0]
                    break
        else:
            query_type, value = query.split()
            if query_type == '1':
                heappush(q, int(value))
                removed.discard(value)
            elif query_type == '2':
                removed.add(value)

Q = int(input())
queries = []

for _ in range(Q):
    queries.append(input())

result = qheapq(queries)

for r in result:
    print(r)