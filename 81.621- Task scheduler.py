class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-count for count in counts.values()]
        heapq.heapify(heap)
        time = 0
        queue = deque()

        while heap or queue:
            time += 1
            if heap:
                count = 1 + heapq.heappop(heap)
                if count < 0:
                    queue.append((count, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        
        return time
        
