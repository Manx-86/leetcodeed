from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        incoming_edges = [0] * numCourses
        queue = deque([])
        course_order = []
        for pre in prerequisites:
            course, prereq = pre
            adj_list[prereq].append(course)
            incoming_edges[course] += 1
        for i in range(numCourses):
            if incoming_edges[i] == 0:
                queue.append(i)                
        while queue:
            current_course = queue.popleft()
            course_order.append(current_course)
            for dependent_course in adj_list[current_course]:
                incoming_edges[dependent_course] -= 1
                if incoming_edges[dependent_course] == 0:
                    queue.append(dependent_course)
        return course_order if len(course_order) == numCourses else []
