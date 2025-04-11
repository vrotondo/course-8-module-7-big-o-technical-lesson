# Big O Performance Analysis in Python

## What You'll Learn

- Understand how to analyze time complexity using Big O notation.
- Compare a single loop (O(n)) to a nested loop (O(n²)).
- Use print statements and counters to measure loop execution.
- Use `time.perf_counter()` to measure runtime.
- Interpret performance trends for different input sizes.

---

## Project Structure

```
.
├── big_o_demo.py
├── lib/
│   ├── __init__.py
│   └── sum_algorithms.py
├── test_sum_algorithms.py
├── Pipfile
├── Pipfile.lock
├── pytest.ini
└── README.md
```

---

## How to Start

1. Install dependencies:

**Using Pipenv:**
```bash
pipenv install
pipenv shell
```

---

## Your Task

- Implement `sum_list(numbers)` to use a single loop and count iterations.
- Implement `sum_list_nested(numbers)` to include a nested loop and track total iterations.
- Use `print()` to show the number of iterations for both.
- Use `big_o_demo.py` to compare execution time for different input sizes.
- Run `pytest` and pass all the tests in `test_sum_algorithms.py`.

---

## Running the Demo

Use the demo script to explore performance:

```bash
python big_o_demo.py
```

You’ll see iteration counts and execution times printed for various input sizes.

---

## Running Tests

Use pytest to validate your logic:

```bash
pytest
```

Tests will initially fail. Complete the functions to make them pass.

---

## Tips

- Start small: test with 5–10 items before scaling up.
- Use `range(n)` to generate test lists.
- Expect the nested loop to grow **much** faster than the single loop.
