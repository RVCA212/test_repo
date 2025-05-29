def prime_factorization(n):
    """
    Perform prime factorization and return a detailed breakdown.
    
    Args:
        n (int): Number to factorize
    
    Returns:
        dict: Dictionary of prime factors and their frequencies
    """
    factors = {}
    divisor = 2
    
    while divisor * divisor <= n:
        if n % divisor == 0:
            # Count frequency of this prime factor
            if divisor not in factors:
                factors[divisor] = 0
            factors[divisor] += 1
            n //= divisor
        else:
            divisor += 1
    
    # If n is a prime number greater than 1
    if n > 1:
        factors[n] = 1
    
    return factors

def visualize_factorization(n):
    """
    Create a visual representation of prime factorization.
    
    Args:
        n (int): Number to factorize
    
    Returns:
        str: String representation of prime factorization
    """
    factors = prime_factorization(n)
    
    # Create factorization string
    factorization_str = ' × '.join(
        [f"{prime}^{power}" if power > 1 else str(prime) 
         for prime, power in factors.items()]
    )
    
    return f"{n} = {factorization_str}"

# Example usage
if __name__ == "__main__":
    print(visualize_factorization(84))