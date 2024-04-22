from pacman_module.game import Agent, Directions
from heapq import heappush, heappop


class PacmanAgent(Agent):
    """Pacman agent based on Greedy Best-First Search."""

    def __init__(self):
        super().__init__()

    def get_action(self, state):
        """Return a legal move based on the current Pacman game state.

        Args:
            state: A game state. See API or class `pacman.GameState`.

        Returns:
            A legal move as defined in `game.Directions`.
        """
        def heuristic(state):
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

        # Initialization of the search
        open_list = []
        closed_set = set()
        came_from = {}

        # Push initial state with heuristic value
        heappush(open_list, (heuristic(state), state, Directions.STOP))

        while open_list:
            _, current_state, action = heappop(open_list)

            if current_state.isWin():
                # Trace back the path to the root
                while came_from[current_state][0] != state:
                    current_state, action = came_from[current_state]
                return action

            if current_state not in closed_set:
                closed_set.add(current_state)

                for successor, move in current_state.generatePacmanSuccessors():
                    if successor not in closed_set:
                        heappush(open_list, (heuristic(successor), successor, move))
                        if successor not in came_from:
                            came_from[successor] = (current_state, move)

        # Fallback if no solution is found
        return Directions.STOP