"""
BUAD449 Module 3 — Environment Check
Run this script to verify your setup is correct.
"""

packages = {
    "cvxpy": "cvxpy",
    "openpyxl": "openpyxl",
}

import sys

print(f"Python ............ ", end="")
v = sys.version_info
if v.major == 3 and v.minor >= 10:
    print(f"OK ({v.major}.{v.minor}.{v.micro})")
else:
    print(f"WRONG VERSION ({v.major}.{v.minor}.{v.micro}) — need 3.10+")

all_ok = True
for display_name, import_name in packages.items():
    print(f"{display_name:.<18} ", end="")
    try:
        __import__(import_name)
        print("OK")
    except ImportError:
        print("MISSING")
        all_ok = False

print()
if all_ok:
    print("All good! You're ready for BUAD449 Module 3.")
else:
    print("Some packages are missing. Run: pip install -r requirements.txt")
