from gym.envs.registration import register

register(
    id = 'Hanoi-v0',
    entry_point = 'hanoi_gym.envs:HanoiEnv',
)
