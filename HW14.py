import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)

episodes = 0
total_steps = 0
steps = 0

for _ in range(2500):
    env.render()

    pole_angle = observation[2]
    action = 1 if pole_angle > 0 else 0

    observation, reward, terminated, truncated, info = env.step(action)
    steps += 1

    if terminated or truncated:
        print("Episode steps:", steps)
        episodes += 1
        total_steps += steps
        observation, info = env.reset()
        steps = 0

env.close()
print("Average steps per episode:", total_steps // episodes)
