import sys
from typing import List, Callable

# Set recursion limit higher for DFS in case of large N
sys.setrecursionlimit(2000)

def solve():
    """
    Reads race data, builds a directed graph based on the condition,
    finds the maximum bipartite matching (Max Flow / Min Path Cover), 
    and prints the result (n - max_matching).
    """
    try:
        # Fast input reading
        # The input format implies N is on the first line, 
        # followed by N lines of (x, y, d)
        
        # Read N
        n_line = sys.stdin.readline()
        if not n_line:
            return
        n = int(n_line.strip())
        
        # Define a class or tuple structure for Race data
        # Using a list of tuples (x, y, d) is simplest in Python
        races: List[tuple] = []
        for _ in range(n):
            line = sys.stdin.readline().split()
            if not line:
                break
            # Convert to integers: x, y, d
            races.append(tuple(map(int, line)))
    
    except EOFError:
        return
    except Exception:
        # Handle potential empty input or format errors
        return

    # Helper function to calculate Manhattan distance
    # The C++ lambda `dist(a, b)`:
    def dist(a: int, b: int) -> int:
        """Calculates Manhattan distance between two races a and b."""
        x1, y1, _ = races[a]
        x2, y2, _ = races[b]
        return abs(x1 - x2) + abs(y1 - y2)

    # Build the adjacency list 'g' (the graph)
    # g[i] contains j if race i can "precede" race j
    g: List[List[int]] = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # races[i].d < races[j].d
            if races[i][2] < races[j][2]:
                # races[j].d - races[i].d >= dist(i, j)
                # The difference in required distance must be at least the travel distance
                travel_distance = dist(i, j)
                distance_diff = races[j][2] - races[i][2]
                
                if distance_diff >= travel_distance:
                    g[i].append(j)

    # --- Maximum Bipartite Matching (using Hopcroft-Karp algorithm via DFS) ---
    # `match[v]` stores the node 'u' that node 'v' is matched to.
    match: List[int] = [-1] * n

    # The C++ recursive DFS function for finding an augmenting path:
    # `dfs(u, seen)` tries to find a match for node `u`.
    def dfs(u: int, seen: List[bool]) -> bool:
        """
        DFS to find an augmenting path starting from u.
        Returns True if a match is found for u.
        """
        for v in g[u]:
            if not seen[v]:
                seen[v] = True
                # If v is unmatched, OR we can find a new match for match[v] (re-routing)
                if match[v] == -1 or dfs(match[v], seen):
                    match[v] = u
                    return True
        return False

    # Main matching loop
    used = 0
    for i in range(n):
        # 'seen' array must be reset for each DFS call from the main loop
        # It tracks nodes visited ONLY during the current augmenting path search
        seen: List[bool] = [False] * n
        if dfs(i, seen):
            used += 1

    # The result is N - Max Matching (Minimum Path Cover)
    # Min Path Cover = N - Max Matching in a DAG
    print(n - used)

if __name__ == "__main__":
    solve()