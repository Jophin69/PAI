def minimax_alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    if maximizing_player:
        value = float('-inf')
        for child in node.generate_children():
            value = max(value, minimax_alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # Beta cutoff
        return value
    else:
        value = float('inf')
        for child in node.generate_children():
            value = min(value, minimax_alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break  # Alpha cutoff
        return value

# Example usage
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def is_terminal(self):
        return not self.children
    
    def evaluate(self):
        return self.value
    
    def generate_children(self):
        return self.children

# Define the game tree
root = Node(3)
root.children = [Node(2), Node(5), Node(8)]
root.children[0].children = [Node(1), Node(7)]
root.children[1].children = [Node(4), Node(6)]
root.children[2].children = [Node(9), Node(1)]

# Call the alpha-beta pruning function
score = minimax_alpha_beta(root, 2, float('-inf'), float('inf'), True)

print("Optimal score:", score)
