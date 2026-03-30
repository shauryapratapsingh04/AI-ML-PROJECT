import heapq

class SmartCityNavigator:
    def __init__(self):

        self.graph = {
            'A': [('B', 4), ('C', 2)],
            'B': [('A', 4), ('C', 5), ('D', 10)],
            'C': [('A', 2), ('B', 5), ('D', 3)],
            'D': [('B', 10), ('C', 3)]
        }
        self.kb = {
            "rush_hour": {"blocked_edges": [('C', 'D')]}
        }
        self.heuristics = {'A': 7, 'B': 6, 'C': 2, 'D': 0}

    def is_path_valid(self, u, v, conditions):
        """Logic check: Returns False if rules in KB forbid this path."""
        for condition in conditions:
            if condition in self.kb:
                if (u, v) in self.kb[condition]["blocked_edges"]:
                    return False
        return True

    def dfs(self, start, goal, path=None):
        if path is None: path = [start]
        if start == goal: return path
        for (neighbor, _) in self.graph.get(start, []):
            if neighbor not in path:
                result = self.dfs(neighbor, goal, path + [neighbor])
                if result: return result
        return None

    def bfs(self, start, goal):
        queue = [[start]]
        visited = set()
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == goal: return path
            if node not in visited:
                for (neighbor, _) in self.graph.get(node, []):
                    queue.append(list(path) + [neighbor])
                visited.add(node)
        return None

    def a_star(self, start, goal, conditions=[]):
        priority_queue = [(0 + self.heuristics[start], 0, start, [start])]
        visited = {}
        while priority_queue:
            f, g, current, path = heapq.heappop(priority_queue)
            if current == goal: return path, g
            if current in visited and visited[current] <= g:
                continue
            visited[current] = g
            for (neighbor, weight) in self.graph.get(current, []):
                if self.is_path_valid(current, neighbor, conditions):
                    new_g = g + weight
                    new_f = new_g + self.heuristics[neighbor]
                    heapq.heappush(priority_queue, (new_f, new_g, neighbor, path + [neighbor]))
        return None, float('inf')



def interactive_menu():
         navigator = SmartCityNavigator()
         print("---  Welcome to the Smart City Logic Navigator ---")
         print(f"Available Locations: {', '.join(navigator.graph.keys())}")
         start_node = input("\nEnter Start Location (e.g., A): ").upper()
         goal_node = input("Enter Destination (e.g., D): ").upper()
         if start_node not in navigator.graph or goal_node not in navigator.graph:
             print(" Invalid locations. Please restart.")
             return
         is_rush_hour = input("Is it currently Rush Hour? (yes/no): ").lower()
         conditions = ["rush_hour"] if is_rush_hour == 'yes' else []
         print("\n---  AI Processing Paths ---")
         bfs_path = navigator.bfs(start_node, goal_node)
         print(f" BFS (Fewest Stops): {bfs_path}")
         astar_path, cost = navigator.a_star(start_node, goal_node, conditions)
         if astar_path:
             status = "(Traffic Logic Applied)" if conditions else "(Clear Traffic)"
             print(f" A* Optimal Path {status}: {astar_path} | Total Cost: {cost}")
         else:
             print("No valid path found! The Knowledge Base has blocked all routes.")

if __name__ == "__main__":
    while True:
        interactive_menu()
        if input("\nTry another route? (y/n): ").lower() != 'y':
            print("Goodbye! Safe travels.")
            break

