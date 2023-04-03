import numpy as np

# Define the environment
n_states = 3
n_actions = 3
R = np.array([[-1, -1, 0], [-1, -1, 100], [0, 100, -1]])
Q = np.zeros((n_states, n_actions))
gamma = 0.9
alpha = 0.1
n_episodes = 5000

# Q-Learning algorithm
for episode in range(n_episodes):
    state = np.random.randint(0, n_states)
    while True:
        action = np.random.randint(0, n_actions)
        next_state = action
        reward = R[state, action]
        Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
        state = next_state
        if state == 1:  # Terminal state
            break

print("Q-values:", Q)

