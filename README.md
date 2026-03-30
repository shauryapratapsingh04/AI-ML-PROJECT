# Project
Shaurya Pratap Singh 25BAI10518 Vityarthi Project

## Smart City Navigator
A Python-based command-line City navigation application that uses knowledge representation , BFS , DFS and A* to find the best route in a city.



## Description

This project focuses on finding the best route in a city where rules change based on Knowledge Representation , BFS , DFS , A* path. Most GPS apps are great at finding the shortest distance, but they aren't very "smart" when it comes to the complex rules of a living city. I built the Smart City Navigator to bridge that gap.

This project is a functional AI agent that doesn't just calculate distances—it reasons through city logic. By combining classical search algorithms with a custom Knowledge Base, the navigator can adapt to real-world scenarios like rush-hour closures, one-way streets, or emergency roadblocks.
## Smart City
The Smart City Navigator is functional via 7 functions:

### 1. __init__(self)
- This is the constructor. It initializes the "World" the AI lives in.
- It sets up three things, the graph , the knowledge base and the heuristics
- Represents Knowledge Representation and State Space Setup.

### 2. is_path_valid(self, u, v, conditions)
- Acts as a "Security Guard" or "Logic Gate."
- Before any algorithm moves from point A to point B, it calls this function. It check to see if that specific road is blocked under current conditions (like Rush Hour).
- Represents Logical Inference and Constraint Satisfaction.

### 3. bfs(self, start, goal)
- Finds the path with the fewest number of intersections.
- It uses a Queue to explore the map layer-by-layer. It doesn't care about the miles/weight; it only cares about reaching the goal in the minimum number of "hops."
- Represents Uninformed Search (Breadth-First).

### 4. dfs(self, start, goal, path=None)
- Checks if a destination is reachable by diving deep into one direction.
- It uses Recursion (a Stack) to follow one path until it hits a dead end, then backtracks. It is "blind" and often finds very long, inefficient paths.
- Represents Uninformed Search (Depth-First).

### 5. a_star(self, start, goal, conditions=[])
- Finds the mathematically optimal (shortest) path while respecting logic.
- It uses a Priority Queue to always pick the node with the lowest f(n) = g(n) + h(n).
- Represents Informed Search.

### 6. interactive_menu()
- Provides the User Interface (UI).
- It handles input() and print() statements. It gathers the user's start point, destination, and environmental conditions (Rush Hour), then triggers the AI algorithms to show the results.
- Represents Human-Computer Interaction and Simulation.

### 7. if __name__ == "__main__":
- The "Ignition Switch" of the program.
- It ensures the code only runs if you execute this specific file. It contains a while True loop so you can run multiple simulations without restarting the script.

## Installation
Download files in FUNDAMENTAL OF AI & ML-VITYARTHI.

## Usage
Run smartcity.py in Visual Studio Code , Jupyter Notebook , Python IDLE

## Features

- Knowledge Representation (KR): A rule-based engine that defines the "state of the world" (e.g., "If Rush Hour = True, then Route C->D is Blocked").

- Uninformed Search: Implementation of BFS (Breadth-First Search) for shortest hop count and DFS (Depth-First Search) for exhaustive exploration.

- *Informed Search (A):** A heuristic-driven search using the cost function:
                        f(n) = g(n) + h(n)
Where g(n) is the path cost and h(n) is the estimated distance to the goal.

## Contact
Shaurya Pratap Singh 25BAI10518
