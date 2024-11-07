def is_adult(age: int) -> bool:
    """Checks if a person is an adult.

    Args:
        age (int): The age to check.
    Raises:
        ValueError: If the age is negative
    Returns:
        bool: True if the age is 18 or above, False otherwise
    """
    if age < 0:
        raise ValueError(f"Age must be a positive integer, but got {age}")

    return age >= 18
