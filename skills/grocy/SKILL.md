---
name: grocy
description: Use grocy-py to read and manage Grocy data (stock, shopping lists, chores, tasks, batteries, meal plans, recipes, users, files, and system info).
---

# grocy

Use this skill when you need to interact with a Grocy instance from Python using `grocy-py`.

## Required Environment Variables

Set these before running code that creates `Grocy()` without explicit credentials:

```bash
export GROCY_BASE_URL="https://your-grocy-instance.com"
export GROCY_API_KEY="YOUR_API_KEY"
```

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

- Passing credentials directly still works: `Grocy(base_url, api_key)`.
- `Grocy()` raises a `ValueError` if `GROCY_BASE_URL` or `GROCY_API_KEY` is missing.
