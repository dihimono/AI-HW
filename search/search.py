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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

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

def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Stack
    import copy
    st = Stack()
    st.push(problem.getStartState())
    st.push([])
    route = list()
    visited = dict()
    while st.isEmpty() == False:
        route = st.pop()
        cur = st.pop()
        visited[cur] = True
        if problem.isGoalState(cur) == True:
            print "Route Length:", len(route)
            return route
        suc = problem.getSuccessors(cur)
        for state in suc:
            if state[0] not in visited:
                st.push(state[0])
                route.append(state[1])
                x = copy.deepcopy(route)
                st.push(x)
                route.pop()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Queue
    import copy
    st = Queue()
    st.push(problem.getStartState())
    st.push([])
    route = list()
    visited = dict()
    visited[problem.getStartState()] = True;
    while st.isEmpty() == False:
        cur = st.pop()
        route = st.pop()
        if problem.isGoalState(cur) == True:
            print "Route Length:", len(route)
            return route
        suc = problem.getSuccessors(cur)
        for state in suc:
            if state[0] not in visited:
                st.push(state[0])
                route.append(state[1])
                x = copy.deepcopy(route)
                st.push(x)
                route.pop()
                visited[state[0]] = True

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import PriorityQueue
    import copy
    visited = dict()
    st = PriorityQueue()
    st.push([problem.getStartState(), [], 0], 0)
    visited[problem.getStartState()] = 0;
    while st.isEmpty() == False:
        cst = st.pop()
        cur = cst[0]
        route = cst[1]
        ccst = cst[2]

        if cur in visited and visited[cur] != ccst:
            continue

        if problem.isGoalState(cur) == True:
            return route

        suc = problem.getSuccessors(cur)
        for state in suc:
            if state[0] not in visited or visited[state[0]] > state[2] + ccst:
                route.append(state[1])
                x = copy.deepcopy(route)
                st.push([state[0], x, state[2] + ccst], state[2] + ccst)
                route.pop()
                visited[state[0]] = state[2] + ccst

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from game import PriorityQueue
    import copy
    visited = dict()
    st = PriorityQueue()
    st.push([problem.getStartState(), [], 0], 0)
    visited[problem.getStartState()] = 0;
    while st.isEmpty() == False:
        cst = st.pop()
        cur = cst[0]
        route = cst[1]
        ccst = cst[2]

        if cur in visited and visited[cur] != ccst:
            continue

        if problem.isGoalState(cur) == True:
            return route

        suc = problem.getSuccessors(cur)
        for state in suc:
            if state[0] not in visited or visited[state[0]] > state[2] + ccst:
                route.append(state[1])
                x = copy.deepcopy(route)
                st.push([state[0], x, state[2] + ccst], state[2] + ccst + heuristic(state[0], problem))
                route.pop()
                visited[state[0]] = state[2] + ccst
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
