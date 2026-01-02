def calc_kdv_exclusive(amount, rate):
    tax = amount * (rate / 100)
    total = amount + tax
    return amount, tax, total

def calc_kdv_inclusive(amount, rate):
    net = amount / (1 + (rate / 100))
    tax = amount - net
    return net, tax, amount

def test_kdv():
    # Scenario 1: 1000 TL + 20% KDV (Exclusive)
    # Expected: Net 1000, Tax 200, Total 1200
    net, tax, total = calc_kdv_exclusive(1000, 20)
    print(f"Exclusive 1000 + 20%: Net={net:.2f}, Tax={tax:.2f}, Total={total:.2f}")
    assert abs(total - 1200) < 0.01

    # Scenario 2: 1200 TL includes 20% KDV (Inclusive)
    # Expected: Net 1000, Tax 200, Total 1200
    net, tax, total = calc_kdv_inclusive(1200, 20)
    print(f"Inclusive 1200 (20%): Net={net:.2f}, Tax={tax:.2f}, Total={total:.2f}")
    assert abs(net - 1000) < 0.01

    # Scenario 3: 100 TL + 1% KDV (Exclusive) -> 101
    net, tax, total = calc_kdv_exclusive(100, 1)
    print(f"Exclusive 100 + 1%: Net={net:.2f}, Tax={tax:.2f}, Total={total:.2f}")
    assert abs(total - 101) < 0.01

    # Scenario 4: 101 TL includes 1% KDV (Inclusive) -> 100
    net, tax, total = calc_kdv_inclusive(101, 1)
    print(f"Inclusive 101 (1%): Net={net:.2f}, Tax={tax:.2f}, Total={total:.2f}")
    assert abs(net - 100) < 0.01

if __name__ == "__main__":
    test_kdv()
