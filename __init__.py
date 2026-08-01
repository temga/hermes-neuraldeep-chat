"""NeuralDeep provider profile.

NeuralDeep -- self-hosted OpenAI-compatible AI hub on own GPUs in Russia.
Base endpoint: https://api.neuraldeep.ru/v1
Docs: https://neuraldeep.ru/docs

API is fully OpenAI Chat Completions compatible, so a basic
ProviderProfile without hook overrides is sufficient.
"""

from __future__ import annotations

from providers import register_provider
from providers.base import ProviderProfile

neuraldeep = ProviderProfile(
    name="neuraldeep",
    aliases=("nd",),
    env_vars=("NEURALDEEP_API_KEY",),
    display_name="NeuralDeep",
    description="NeuralDeep -- gpt-oss, qwen3.6, Gemma 4 on own GPUs in Russia (152-FZ)",
    signup_url="https://neuraldeep.ru/app",
    base_url="https://api.neuraldeep.ru/v1",
    fallback_models=(
        "gpt-oss-120b",
        "qwen3.6-35b-a3b",
        "gemma-4-31b",
    ),
    default_aux_model="qwen3.6-35b-a3b",
    supports_vision=True,
)

register_provider(neuraldeep)
