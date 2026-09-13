# Build: 0340ed40f8c1a24c4d22028cd070bcc6

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
