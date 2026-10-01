from mini_projects.commerceops_agent.tools import (
    get_inventory,
    get_inventory_report,
    get_total_revenue,
    get_top_product,
)

def test_get_inventory():
    result = get_inventory("iPhone 16")

    assert result is not None

def test_get_inventory():
    result = get_inventory("iPhone 16")
    assert result == 42

def test_inventory_report():
    result = get_inventory_report()

    assert result is not None

def test_total_revenue():
    result = get_total_revenue()

    assert result is not None

def test_top_product():
    result = get_top_product()

    assert result is not None