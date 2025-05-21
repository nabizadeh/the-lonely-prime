import math
from typing import List

def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    max_check = int(math.sqrt(n))
    for i in range(3, max_check + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_number_sentences(limit: int = 50) -> List[str]:
    """Generate sentences describing numbers as prime/composite and even/odd."""
    sentences: List[str] = []

    for num in range(1, limit + 1):
        prime_sentence = (
            f"{num} is a prime number." if is_prime(num)
            else f"{num} is a composite number."
        )

        odd_even_sentence = (
            f"{num} is an even number." if num % 2 == 0
            else f"{num} is an odd number."
        )

        sentences.append(prime_sentence)
        sentences.append(odd_even_sentence)

    return sentences

def save_sentences_to_file(sentences: List[str], path: str) -> None:
    """Save a list of sentences to a text file."""
    with open(path, "w") as f:
        for sentence in sentences:
            f.write(sentence + "\n")

