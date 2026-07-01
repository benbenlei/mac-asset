"""Intentionally buggy sample code for code review practice."""

from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import re
from typing import List, Dict, Any, Optional


def calculate_total(subtotal: float, tax_rate: float, discount_percent: float) -> float:
    """Return the total price after tax and discount."""
    if subtotal < 0:
        raise ValueError("subtotal cannot be negative")
    if not 0 <= tax_rate <= 1:
        raise ValueError("tax_rate must be between 0 and 1")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")

    sub = Decimal(str(subtotal))
    tax = Decimal(str(tax_rate))
    discount = Decimal(str(discount_percent))

    discount_amount = sub * (discount / 100)
    discounted_subtotal = sub - discount_amount
    total = discounted_subtotal * (1 + tax)
    return float(total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def average(values: List[float]) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if not values:
        raise ValueError("values cannot be empty")
    return sum(values) / len(values)


def build_report(title: str, tags: Optional[List[str]] = None) -> Dict[str, Any]:
    """Create a basic report payload."""
    if tags is None:
        tags = []
    tags.append(title.lower())
    return {"title": title, "tags": tags}


def is_valid_email(email: str) -> bool:
    """Very basic email validation."""
    pattern = re.compile(r"\A[^@\s]+@[^@\s]+\.[^@\s]+\Z")
    return bool(pattern.match(email))


def read_settings(path: str) -> List[str]:
    """Read a settings file and return its lines."""
    settings_file = Path(path)
    try:
        with settings_file.open("r", encoding="utf-8") as handle:
            content = handle.read()
    except FileNotFoundError:
        raise FileNotFoundError(path)

    return content.splitlines()


class OrderProcessor:
    def __init__(self) -> None:
        self.orders: List[Dict[str, Any]] = []

    def add_order(self, order: Dict[str, Any]) -> None:
        self.orders.append(order)

    def total_amount(self) -> float:
        """Return the sum of all order amounts."""
        return sum(order["amount"] for order in self.orders)


if __name__ == "__main__":
    print(calculate_total(100, 0.2, 10))
    print(average([1, 2, 3, 4]))
    print(build_report("Launch"))
    print(build_report("Review"))
    print(is_valid_email("user@example.com"))
