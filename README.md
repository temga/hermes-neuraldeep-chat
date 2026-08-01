# Плагин NeuralDeep для Hermes Agent

[![GitHub](https://img.shields.io/badge/GitHub-temga%2Fhermes--neuraldeep--plugin-blue)](https://github.com/temga/hermes-neuraldeep-plugin)

[NeuralDeep](https://neuraldeep.ru/) — self-hosted AI-хаб на собственных GPU в России (152-ФЗ). OpenAI-совместимый API к LLM, эмбеддингам, реранку, STT, vision, OCR, image generation и поиску — всё по одному `sk-` ключу.

## Установка

    hermes plugins install temga/hermes-neuraldeep-plugin --enable

Или через [hermes-ru-ecosystem](https://github.com/temga/hermes-ru-ecosystem):

    curl -fsSL https://raw.githubusercontent.com/temga/hermes-ru-ecosystem/main/install.sh | bash

## Настройка

Hermes хранит секреты в `~/.hermes/.env`. Добавьте туда:

    NEURALDEEP_API_KEY=ваш-api-ключ

Или запустите `hermes setup` — мастер настройки запросит ключ автоматически.

Получить ключ: https://neuraldeep.ru/app

## Использование

Запустите Hermes и выберите NeuralDeep в качестве провайдера:

    hermes model

Выберите `neuraldeep` из списка, затем выберите модель. Переключать модели в любой момент:

    /model neuraldeep:gpt-oss-120b

## Доступные модели

| Модель | Контекст | Особенности |
|---|---|---|
| `gpt-oss-120b` | 131k | Tools, reasoning, MXFP4 на 2×RTX 4090 |
| `qwen3.6-35b-a3b` | 256k | MoE 35B/3B-active, tools, vision (1 img/req), BF16 |
| `gemma-4-31b` | 262k | Tools, multimodal (image/video) |

Полный список: https://neuraldeep.ru/models

## Тарифы

Free (150 запросов / 3 часа), Coder, Starter, Pro. Подробнее: https://neuraldeep.ru/pricing

## Как это работает

Плагин регистрирует `ProviderProfile` в реестре провайдеров Hermes Agent. Поскольку API NeuralDeep полностью совместим с форматом OpenAI Chat Completions, дополнительные хуки или переопределения не требуются — базовый профиль обрабатывает всё автоматически.

## Репозиторий

- **GitHub:** https://github.com/temga/hermes-neuraldeep-plugin

## Лицензия

MIT
