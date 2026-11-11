"""
checkout.py
Exercise 2: Collaborative Software Development
Checkout functionality with a 10% student discount.
"""

STUDENT_DISCOUNT_RATE = 0.10  # 10% off for eligible students


def apply_student_discount(total, is_student):
    """Return the final payable amount.

    Eligible students receive a 10% discount; non-students pay the
    original price unchanged.
    """
    if is_student:
        return round(total * (1 - STUDENT_DISCOUNT_RATE), 2)
    return total


def checkout(total, is_student):
    """Calculate the discount and final total, then print a receipt."""
    discount = 0.0
    if is_student:
        discount = round(total * STUDENT_DISCOUNT_RATE, 2)
    final_total = round(total - discount, 2)

    print("=== Checkout Receipt ===")
    print(f"Original total: GBP {total:.2f}")
    if is_student:
        print("Student discount: 10%")
        print(f"Discount amount: GBP {discount:.2f}")
    else:
        print("Student discount: not applied")
    print(f"Final total: GBP {final_total:.2f}")
    return final_total


def run_tests():
    """Verify discount calculation for students and non-students."""
    # Students receive a 10% discount.
    assert apply_student_discount(100, is_student=True) == 90.0
    assert apply_student_discount(50, is_student=True) == 45.0
    # Non-students pay the original price.
    assert apply_student_discount(100, is_student=False) == 100
    assert apply_student_discount(50, is_student=False) == 50
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()

    print("\n[Test 1] Student, original total GBP 100")
    checkout(100, is_student=True)

    print("\n[Test 2] Non-student, original total GBP 100")
    checkout(100, is_student=False)
