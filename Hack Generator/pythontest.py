import random

def create_advanced_hack(a, b, n, cluster_size=16, fill_ratio=0.1, seed=None):
    """
    Generates integers that target Python dict/hash table internals.
    
    Parameters:
        a (int): Minimum value (inclusive).
        b (int): Maximum value (exclusive).
        n (int): Total number of values to generate.
        cluster_size (int): Number of elements to cluster into same hash bucket.
        fill_ratio (float): Percentage of values that should be 'non-colliding' noise.
        seed (int): Random seed for reproducibility.
    
    Returns:
        list[int]: Generated list.
    """
    if seed is not None:
        random.seed(seed)

    # Compute mask used by CPython (2^k) table size
    pow2 = 2 ** ((b - a - 1).bit_length() - 1)
    start = 858993459 % pow2  # arbitrary "start" hash position

    def probe_sequence(x, CPython=False):
        i = perturb = hash(x)
        i %= pow2
        yield i
        while True:
            if CPython:
                perturb >>= 5
            i = (5 * i + perturb + 1) % pow2
            yield i
            if not CPython:
                perturb >>= 5

    # Construct one "cluster" of values that hash to same slots
    def build_cluster():
        s = set()
        for i in probe_sequence(start, True):
            val = i + (a + 1 - i + pow2 - 1) // pow2 * pow2
            if val >= b:
                break
            s.add(val)
            if len(s) >= cluster_size:
                break
        return list(s)

    result = []
    clusters_needed = int(n * (1 - fill_ratio) // cluster_size)
    for _ in range(clusters_needed):
        result.extend(build_cluster())

    # Add filler values (non-colliding randoms)
    filler_needed = n - len(result)
    result.extend(random.sample(range(a, b), filler_needed))

    random.shuffle(result)
    return result[:n]
if __name__ == "__main__":
    n = 2 * 10**5
    MX = 10**9
    A = create_advanced_hack(1, MX, n, cluster_size=20, fill_ratio=0.05, seed=42)
    
    print(1)
    print(n, n)
    print(*A, sep=' ')
