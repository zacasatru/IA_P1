# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# Autores: Victor Perez Cano (victor.perezcano@estudiante.uam.es)
#          Ignacio Bernardez Toral (ignacio.bernardez@estudiante.uam.es)
"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class Node:

    def __init__(self, problem, gameState=None, pathToState=[]):
        self.problem = problem
        if (gameState is None):
            self.position = self.problem.getStartState()
            self.path = []
            self.cost = 0
        else:
            self.position = gameState[0]
            self.path = pathToState + [gameState[1]]
            self.cost = self.problem.getCostOfActions(pathToState) + gameState[2]
        
    def isGoalState(self):
        return self.problem.isGoalState(self.position)

    def getSuccessors(self):
        successors = self.problem.getSuccessors(self.position)
        return map(lambda successor: Node(self.problem, successor, self.path), successors)

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def _graphSearch(problem, openList):
    closeList = [] # Iniciar lista cerrados como lista vacia
    openList.push(Node(problem)) # Iniciar lista abiertos con el nodo raiz
    while not openList.isEmpty():
        currentNode = openList.pop()
        if currentNode.isGoalState():
            return currentNode.path
        if currentNode.position not in closeList:
            closeList.append(currentNode.position)
            successors = currentNode.getSuccessors()
            for successor in successors:
                openList.push(successor)
    return []


def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    return _graphSearch(problem, util.Stack())

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    return _graphSearch(problem, util.Queue())

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    return _graphSearch(problem, util.PriorityQueueWithFunction(lambda node : node.cost))
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    heuristicEvaluation = lambda node: node.cost + heuristic(node.position, problem)
    return _graphSearch(problem, util.PriorityQueueWithFunction(heuristicEvaluation))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
