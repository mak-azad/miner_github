import re

# Define regex patterns for Python performance categories
api_misuse_patterns = re.compile(r'(incorrect use|deprecated|redundant calls|inefficient library usage|pandas|numpy|requests)', re.IGNORECASE)
memory_inefficiency_patterns = re.compile(r'(memory leak|gc\.collect\(\)|over allocation|memory_profiler)', re.IGNORECASE)
concurrency_control_patterns = re.compile(r'(thread contention|deadlock|race condition|threading|asyncio|multiprocessing)', re.IGNORECASE)
io_inefficiency_patterns = re.compile(r'(blocking I/O|excessive disk operations|inefficient caching|logging|os|logging|aiofiles)', re.IGNORECASE)
network_bottlenecks_patterns = re.compile(r'(excessive network calls|inefficient data transfer|high latency|socket|requests)', re.IGNORECASE)
algorithm_data_structures_patterns = re.compile(r'(suboptimal algorithm|inefficient loops|expensive operations|data structure|list|set|dict)', re.IGNORECASE)
parallelization_patterns = re.compile(r'(missing parallelism|inefficient parallelism|GPU|Numba|Dask|concurrent\.futures)', re.IGNORECASE)
micro_architectural_patterns = re.compile(r'(data locality|compiler optimizations|CPU cache|vectorization|Cython|PyPy)', re.IGNORECASE)
other_performance_issues_patterns = re.compile(r'(unclassified|miscellaneous inefficiencies|unique cases)', re.IGNORECASE)

def get_domain_vector(text, src):
    performance_domain_vector = [0] * 9  # Assume 9 categories as previously defined

    # Check each pattern in both text and src, and update the vector to 1 if any match is found
    if api_misuse_patterns.search(text) or api_misuse_patterns.search(src):
        performance_domain_vector[0] = 1
    if memory_inefficiency_patterns.search(text) or memory_inefficiency_patterns.search(src):
        performance_domain_vector[1] = 1
    if concurrency_control_patterns.search(text) or concurrency_control_patterns.search(src):
        performance_domain_vector[2] = 1
    if io_inefficiency_patterns.search(text) or io_inefficiency_patterns.search(src):
        performance_domain_vector[3] = 1
    if network_bottlenecks_patterns.search(text) or network_bottlenecks_patterns.search(src):
        performance_domain_vector[4] = 1
    if algorithm_data_structures_patterns.search(text) or algorithm_data_structures_patterns.search(src):
        performance_domain_vector[5] = 1
    if parallelization_patterns.search(text) or parallelization_patterns.search(src):
        performance_domain_vector[6] = 1
    if micro_architectural_patterns.search(text) or micro_architectural_patterns.search(src):
        performance_domain_vector[7] = 1
    if other_performance_issues_patterns.search(text) or other_performance_issues_patterns.search(src):
        performance_domain_vector[8] = 1

    # Convert list to string without separators
    result_vector_str = ''.join(map(str, performance_domain_vector))
    return result_vector_str


# Example usage
text = "Fixed memory leak in data structure using numpy"
src = "asyncio"
result_vector_str = get_domain_vector(text,src)
print("Performance Domain Vector as String:", result_vector_str)
