from gymnasium.envs.registration import register # type: ignore

register(
    id="gymnasium_env/Conj1349-v0",
    entry_point="gymnasium_env.envs:conj1349env",
)