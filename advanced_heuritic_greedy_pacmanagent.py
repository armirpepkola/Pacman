from pacman_module.game import Agent, Directions
from heapq import heappush, heappop


class PacmanAgent(Agent):
    """Greedy Best-First Search based Pacman agent using an advanced heuristic."""

    def __init__(self):
        super().__init__()

    def get_action(self, state):
        """Given a Pacman game state, returns a legal move."""
        # Calculate the heuristic and return action
        open_list = []
        closed_set = set()
        came_from = {}

        heappush(open_list, (self.advanced_heuristic(state), state, Directions.STOP))

        while open_list:
            _, current_state, action = heappop(open_list)

            if current_state.isWin():
                while came_from[current_state][0] != state:
                    current_state, action = came_from[current_state]
                return action

            if current_state not in closed_set:
                closed_set.add(current_state)

                for successor, move in current_state.generatePacmanSuccessors():
                    if successor not in closed_set:
                        heappush(open_list, (self.advanced_heuristic(successor), successor, move))
                        if successor not in came_from:
                            came_from[successor] = (current_state, move)

        return Directions.STOP

    def advanced_heuristic(self, state):
        """Calculate advanced heuristic based on food proximity and clustering."""
        pacman_pos = state.getPacmanPosition()
        food_grid = state.getFood()
        food_positions = [(x, y) for x in range(food_grid.width)
                          for y in range(food_grid.height) if food_grid[x][y]]

        if not food_positions:
            return 0

        distances = [abs(x - pacman_pos[0]) + abs(y - pacman_pos[1]) for x, y in food_positions]
        min_distance = min(distances)
        nearest_food = food_positions[distances.index(min_distance)]

        cluster_radius = 5
        cluster_count = sum(1 for x, y in food_positions
                            if abs(x - nearest_food[0]) + abs(y - nearest_food[1]) <= cluster_radius)
        max_cluster_count = (2 * cluster_radius + 1) ** 2 - 1
        normalized_cluster_bonus = cluster_count / max_cluster_count

        return min_distance - normalized_cluster_bonus