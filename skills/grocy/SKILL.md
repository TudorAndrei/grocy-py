---
name: grocy
description: Use grocy-py to read and manage Grocy data (stock, shopping lists, chores, tasks, batteries, meal plans, recipes, users, files, and system info).
---

# grocy

Use this skill when you need to interact with a Grocy instance from Python using `grocy-py`.

## Required Environment Variables

This skill expects `GROCY_BASE_URL` and `GROCY_API_KEY` to already be configured in the environment.

Do not ask the user to set them again; just use `Grocy()`.

## Quick Start

```python
from grocy import Grocy

grocy = Grocy()

for product in grocy.stock.current():
    print(product.name, product.available_amount)
```

## Common Tasks

- **Stock:** `grocy.stock.current()`, `grocy.stock.add(...)`, `grocy.stock.consume(...)`
- **Shopping list:** `grocy.shopping_list.items()`, `grocy.shopping_list.add_product(...)`
- **Chores:** `grocy.chores.list()`, `grocy.chores.execute(...)`
- **Tasks:** `grocy.tasks.list()`, `grocy.tasks.complete(...)`
- **System checks:** `grocy.system.info()`, `grocy.system.time()`, `grocy.system.config()`

## Notes

- `Grocy()` raises a `ValueError` if `GROCY_BASE_URL` or `GROCY_API_KEY` is missing.
