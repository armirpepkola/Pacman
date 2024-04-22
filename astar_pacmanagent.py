from pacman_module.game import Agent, Directions
from heapq import heappush, heappop
import math


class PacmanAgent(Agent):
    """A* search based Pacman agent implementing heuristic search."""

    def __init__(self):
        super().__init__()

    def get_action(self, state):
        """Given a Pacman game state, returns a legal move."""
        return self.a_star_search(state)

    def heuristic(self, state):
        """Calculate Manhattan distance from Pacman to nearest food dot."""
        pacman_pos = state.getPacmanPosition()
        food_grid = state.getFood()
        min_distance = float('inf')

        for x in range(food_grid.width):
            for y in range(food_grid.height):
                if food_grid[x][y]:
                    dist = abs(x - pacman_pos[0]) + abs(y - pacman_pos[1])
                    if dist < min_distance:
                        min_distance = dist

        return min_distance

    def a_star_search(self, state):
        """Perform A* search to find the optimal path to the goal."""
        open_list = []
        closed_set = set()
        came_from = {}

        heappush(open_list, (self.heuristic(state), state, Directions.STOP, 0))
        came_from[state] = None

        while open_list:
            _, current_state, action, cost = heappop(open_list)

            if current_state.isWin():
                return self.trace_path(state, came_from, current_state)

            if current_state not in closed_set:
                closed_set.add(current_state)

                for successor, move in current_state.generatePacmanSuccessors():
                    if successor not in closed_set:
                        new_cost = cost + 1  # Assume each move has a cost of 1
                        priority = new_cost + self.heuristic(successor)
                        heappush(open_list, (priority, successor, move, new_cost))
                        if successor not in came_from:
                            came_from[successor] = (current_state, move)

        return Directions.STOP

    def trace_path(self, start_state, came_from, current_state):
        """Trace back the path from goal to start state."""
        while came_from[current_state][0] != start_state:
            current_state, action = came_from[current_state]
        return action