def newton(n, estimate=None, tolerance=1e-10):
    if estimate is None:
        estimate = n / 2  # Initial guess

    # Calculate a better estimate
    better_estimate = 0.5 * (estimate + n / estimate)

    # Check if the difference is within the tolerance
    if abs(better_estimate - estimate) < tolerance:
        return better_estimate
    else:
        # Recursive call with the new estimate
        return newton(n, better_estimate, tolerance)


