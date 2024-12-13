import jsbgym
import gymnasium as gym


def attempt(environment):
    environment.reset()
    environment.render()
    done = False
    reward_sum = 0.0
    while not done:
        action = environment.action_space.sample()
        observation, reward, done, truncated, info = environment.step(action)
        reward_sum += reward
    return reward_sum


def main():
    environment = gym.make('C172-HeadingControlTask-Shaping.STANDARD-FG-v0', render_mode='flightgear')

    for _ in range(10):
        reward_sum = attempt(environment)
        print(reward_sum)

    environment.close()


if __name__ == "__main__":
    main()
