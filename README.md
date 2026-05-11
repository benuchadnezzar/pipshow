# pipshow

Prints a random Python package name and description each time you open your terminal.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run `query.py` once to build the package list:

```bash
python3 query.py
```

Then add `main.py` to your shell config:

```bash
# ~/.zshrc or ~/.bashrc
python3 /path/to/pipshow/main.py
```

## Refreshing the package list

`query.py` pulls the top 15k PyPI packages from [hugovk/top-pypi-packages](https://github.com/hugovk/top-pypi-packages), which updates on the 1st of each month. Run it on the 2nd via cron:

```
# 2nd of the month at 9am
0 9 2 * * /path/to/pipshow/.venv/bin/python3 /path/to/pipshow/query.py

# First Monday of the month at 9:30am (fallback if machine was off on the 2nd)
30 9 1-7 * 1 /path/to/pipshow/.venv/bin/python3 /path/to/pipshow/query.py
```
