# yacape - Yet Another Clean Architecture Python Example

## Layers

| Layer | Name                                             | Path         |
| ----- | ------------------------------------------------ | ------------ |
| 1     | Entities (Domain Models & Domain Business Logic) | `/entities`  |
| 2     | Use Cases (App Business Logic)                   | `/use_cases` |
| 3     | Interface Adapters                               | `/adapters`  |
| 4     | Frameworks & Drivers                             | `/externals` |

## Installation

```bash
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Run App

```bash
source ./venv/bin/activate
python main.py
```

## Run Tests

```bash
python -m unittest
```
