# leetcode 997 Find the Town Judge problem solve by step by step
from typing import List
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        trust_count = [0] * (N + 1)
        for a, b in trust:
            trust_count[a] -= 1
            trust_count[b] += 1
        for i in range(1, N  + 1):
            if trust_count[i] == N - 1:
                return i
        return -1
# Example usage:  
# solution = Solution()
# print(solution.findJudge(2, [[1, 2]]))  # Output: 2
# print(solution.findJudge(3, [[1, 3], [2, 3]]))  # Output: 3
# print(solution.findJudge(3, [[1, 3], [2, 3], [3, 1]]))  # Output: -1
#         self.graph[u].append(v)ttttttttttt 
#         self.graph[v].append(u)  # For undirected graph
#     def display(self):
#         for u in self.graph:
#             print(f"{u} -> {', '.join(map(str, self.graph[u]))}")
# adjency input
# what is defaultd dictionary

def adjency_input():
    n = int(input("Enter number of vertices: "))
    graph = {}
    for i in range(n):
        edges = input(f"Enter edges for vertex {i} (space-separated, or 'done' to finish): ")
        if edges.lower() == 'done':
            break
        graph[i] = list(map(int, edges.split()))
    return graph
# leet code 997 whole code
def find_town_judge(N: int, trust: List[List[int]]) -> int:
    if N == 1:
        return 1
    trust_count = [0] * (N + 1)
    for a, b in trust:
        trust_count[a] -= 1
        trust_count[b] += 1
    for i in range(1, N + 1):
        if trust_count[i] == N - 1:
            return i
    return -1

n = int(input("Enter number of people: "))
trust = lis