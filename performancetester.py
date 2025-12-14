"""
Performance Testing Module
==============================================
Measures actual execution times for data structure operations and compares
predicted vs. actual performance characteristics.

Author: Kaitlyn McCormick
Course: CSC506 - Design and Analysis of Algorithms
Module: 1 - Data Structures and Algorithm Complexity

"""

import time
import statistics
import random
from typing import Dict, List, Tuple, Callable, Any
from dataclasses import dataclass
from data_structures import Stack, Queue, LinkedList
from complexity_analyzer import ComplexityAnalyzer

@dataclass
class TimingResult:
    """Stores timing results for an operation."""
    operation: str
    input_size: int
    times: List[float] #individual run times
    mean_time: float
    std_dev: float
    min_time: float
    max_time: float
    predicted_complexity: str
    
    def __str__(self):
        return (f"{self.operation} (n={self.input_size}): "
                f"mean={self.mean_time:.6f}s, std={self.std_dev:.6f}s")

class PerformanceTester:
    """
    Tests actual performance of data structure operations.
    
    Measures execution times across various input sizes to: 
    1. Verify theoretical complexity predictions
    2. Compare performance across data structures
    3. Demonstrate growth rate patterns
    """
    
    def __init__(self, iterations: int = 10):
        """
        Initialize performance tester.
        
        Arguments: 
           iterations: Number of times to repeat each test for averaging
        """
        self.iterations = iterations
        self.results: Dict[str, List[TimingResult]] = {}
    
    def time_operation(self, operation: Callable, *args, **kwargs) -> float:
        """
        Time a single operation execution.
        
        Arguments: 
           operation: Function to time
           *args, **kwargs: Arguments to pass to function
           
        Returns:
           Execution time in seconds
        """
        start = time.perf_counter()
        operation(*args, **kwargs)
        end = time.perf_counter()
        return end - start
    
    def benchmark_operation(self,
                            operation: Callable,
                            setup: Callable,
                            operation_name: str,
                            input_size: int,
                            predicted_complexity: str = "0(?)") -> TimingResult:
        """
        Benchmark an operation multiple times.
        
        Arguments: 
           operation: Function to benchmark
           setup: Function that returns args for operation (called before each run)
           operation_name: Name for reporting
           input_size: Size of input data
           predicted_complexity: Expected Big-O complexity
        
        Returns: 
           TimingResult with statistics
        """
        times = []
        
        for _ in range(self.iterations):
            args = setup()
            elapsed = self.time_operation(operation, *args)
            times.append(elapsed)
        
        return TimingResult(
            operation=operation_name,
            input_size=input_size,
            times=times,
            mean_time=statistics.mean(times),
            std_dev=statistics.stdev(times) if len(times) > 1 else 0,
            min_time=min(times),
            max_time=max(times),
            predicted_complexity=predicted_complexity
        )
    
    #====================================================================
    # STACK BENCHMARKS
    #====================================================================
    
    def benchmark_stack_push(self, sizes: List[int]) -> List[TimingResult]:
        """Benchmark stack push operation across different sizes."""
        results = []
        
        for n in sizes: 
            def setup():
                stack = Stack()
                data = list(range(n))
                return (stack, data)
            
            def operation(stack, data):
                for item in data:
                    stack.push(item)
            
            result = self.benchmark_operation(
                operation, setup, "stack_push_n_items", n, "0(n) total, 0(1) per item"
            )
            results.append(result)
            
        self.results["stack_push"] = results
        return results
    
    def benchmark_stack_pop(self, sizes: List[int]) -> List[TimingResult]:
        """Benchmark stack pop operation across different sizes."""
        results = []
        
        for n in sizes:
            def setup():
                stack = Stack()
                for i in range(n):
                    stack.push(i)
                return (stack,)
            
            def operation(stack):
                while not stack.is_empty():
                    stack.pop()
                    
            result = self.benchmark_operation(
                operation, setup, "stack_pop_n_items", n, "0(n) total, 0(1) per item"
            )
            results.append(result)
        
        self.results["stack_pop"] = results
        return results
    
    def benchmark_stack_search(self, sizes: List[int]) -> List[TimingResult]:
        """Benchmark stack search operation (worst case - element at bottom)."""
        results = []
        
        for n in sizes: 
            def setup():
                stack = Stack()
                for i in range(n):
                    stack.push(i)
                target = 0 # Bottom element - worst case
                return (stack, target)
            
            def operation(stack, target):
                stack.search(target)
            
            result = self.benchmark_operation(
                operation, setup, "stack_search_worst", n, "0(n)"
            )
            results.append(result)
        
        self.results["stack_search"] = results
        return results
    
    #====================================================================
    # QUEUE BENCHMARKS
    #====================================================================
    
    def benchmark_queue_enqueue(self, sizes: List[int]) -> List[TimingResult]:
        """Benchmark queue enqueue operation across different sizes."""
        results = []
        
        for n in sizes: 
            def setup(): 
                queue = Queue()
                data = list(range(n))
                return (queue, data)
            
            def operation(queue, data):
                for item in data: 
                    queue.enqueue(item)
            
            result = self.benchmark_operation(
                operation, setup, "queue_enqueue_n_items", n, "0(n) total, 0(1) per item"
            )
            results.append(result)
        self.results["queue_enqueue"] = results
        return results
    
    def benchmark_queue_dequeue(self, sizes: List[int]) -> List[TimingResult]:
        """Benchmark queue dequeue operation across different sizes."""
        results = []
        
        for n in sizes: 
            def setup():
                queue = Queue()
                for i in range(n):
                    queue.enqueue(i)
                return (queue,)
            def operation(queue):
                while not queue.is_empty():
                    queue.dequeue()
                    
            result = self.benchmark_operation(
                operation, setup, "queue_dequeue_n_items", n, "0(n) total, 0(1) per item"
            )
            results.append(result)
            
        self.results["queue_dequeue"] = results
        return results
    
    def benchmark_queue_search(self, sizes: List[int]) -> List[TimingResult]:
        """Benchmark queue search operation ( worst case - element at rear). """
        results = []
        
        for n in sizes:
            def setup():
                queue = Queue()
                for i in range(n):
                    queue.enqueue(i)
                target = n - 1 #Last element - worst case
                return (queue, target)
            
            def operation(queue, target):
                queue.search(target)
                
            result = self.benchmark_operation(
                operation, setup, "queue_search_worst", n, "0(n)"
            )
            results.append(result)
            
        self.results["queue_search"] = results
        return results
    
    #====================================================================
    # LINKED LIST BENCHMARKS
    #====================================================================
    
    def benchmark_linkedlist_insert_head(self, sizes: List[int]) -> List[TimingResult]:
        """"Benchmark linked list insert at head operation."""
        results = []
        
        for n in sizes: 
            def setup():
                ll = LinkedList()
                data = list(range(n))
                return (ll, data)
            
            def operation(ll, data):
                for item in data:
                    ll.insert_at_head(item)
                    
            result = self.benchmark_operation(
                operation, setup, "linkedlist_insert_head_n", n, "0(n) total, 0(1) per item."
            )
            results.append(result)
        self.results["linkedlist_insert_head"] = results
        return results
    
    def benchmark_linkedlist_insert_tail(self, sizes: List[int]) -> List[TimingResult]:
        """Benchmark linked list insert at tail operation"""
        results = []
        
        for n in sizes:
            def setup():
                ll = LinkedList()
                data = list(range(n))
                return (ll, data)
            
            def operation(ll, data):
                for item in data:
                    ll.insert_at_tail(item)
                    
            result = self.benchmark_operation(
                operation, setup, "linkedlist_insert_tail_n", n, "0(n) total, 0(1) per item."
            )
            results.append(result)
        self.results["linkedlist_insert_tail"] = results
        return results
    
    def benchmark_linkedlist_search(self, sizes: List[int]) -> List[TimingResult]:
        """Benchmark linked list search operation (worst case - element at tail)."""
        results = []
        
        for n in sizes:
            def setup():
                ll = LinkedList()
                for i in range(n):
                    ll.insert_at_tail(i)
                target = n - 1 #Last element - worst case
                return (ll, target)
            
            def operation(ll, target):
                ll.search(target)
                
            result = self.benchmark_operation(
                operation, setup, "linkedlist_search_worst", n, "0(n)"
            )
            results.append(result)
        
        self.results["linkedlist_search"] = results
        return results
    
    def benchmark_linkedlist_delete(self, sizes: List[int]) -> List[TimingResult]:
        """Benchmark linked list delete operation (worst case - element at tail)."""
        results = []
        
        for n in sizes:
            def setup():
                ll = LinkedList()
                for i in range(n):
                    ll.insert_at_tail(i)
                target = n - 1 # Last element - worst case
                return (ll, target)
            
            def operation(ll, target):
                ll.delete(target)
                
            result = self.benchmark_operation(
                operation, setup, "linkedlist_delete_worst", n, "0(n)"
            )
            results.append(result)
        
        self.results["linkedlist_delete"] = results
        return results
    
    #====================================================================
    # COMPREHENSIVE BENCHMARKS
    #====================================================================
    
    def run_all_benchmarks(self,sizes: List[int] = None) -> Dict[str, List[TimingResult]]:
        """
        Run all benchmarks for all data structures.
        
        Arguments: 
           sizes: List of input sizes to test (default: [100,500,1000,5000,10000])
           
        Returns:
           Dictionary mapping benchmark names to results
        """
        if sizes is None:
            sizes = [100, 500, 1000, 5000, 10000]
        
        print("\n" + "=" + 70)
        print("RUNNING COMPREHENSIVE PERFORMANCE BENCHMARKS")
        print("=" * 70)
        print(f"Input sizes: {sizes}")
        print(f"Iterations per test: {self.iterations}")
        print("-" * 70)
        
        #Stack benchmarks
        print("\n[STACK BENCHMARKS]")
        print("  Running push benchmark...")
        self.benchmark_stack_push(sizes)
        print("  Running pop benchmark...")
        self.benchmark_stack_pop(sizes)
        print("  Running search benchmark...")
        self.benchmark_stack_search(sizes)
        
        #Queue benchmarks
        print("\n[QUEUE BENCHMARKS]")
        print("  Running enqueue benchmark...")
        self.benchmark_queue_enqueue(sizes)
        print("  Running dequeue benchmark...")
        self.benchmark_queue_dequeue(sizes)
        print("  Running search benchmark...")
        self.benchmark_queue_search(sizes)
        
        # Linked List benchmarks
        print("\n[LINKED LIST BENCHMARKS]")
        print("  Running insert_head benchmark...")
        self.benchmark_linkedlist_insert_head(sizes)
        print("  Running insert_tail benchmark...")
        self.benchmark_linkedlist_insert_tail(sizes)
        print("  Running search benchmark...")
        self.benchmark_linkedlist_search(sizes)
        print("  Running delete benchmark...")
        self.benchmark_linkedlist_delete(sizes)
        
        print("\n" + "=" * 70)
        print("BENCHMARKS COMPLETE")
        print("=" * 70)
        
        return self.results
    
    def generate_report(self) -> str:
        """Generate a text report of all benchmark results."""
        lines = [
            "\n" + "=" * 80,
            "PERFORMANCE BENCHMARK REPORT",
            "=" * 80,
            f"Iterations per test: {self.iterations}",
            ""
        ]
        
        for benchmark_name, results in self.results.items():
            lines.append(f"\n--- {benchmark_name.upper().replace('_', ' ')} ---")
            lines.append(f"{'Size':<10} {'Mean (s)':<15} {'Std Dev':<15} {'Complexity':<20}")
            lines.append("-" * 60)
            
            for result in results:
                lines.append(
                    f"{result.input_size:<10} {result.mean_time:<15.6f} "
                    f"{result.std_dev:<15.6f} {result.predicted_complexity:<20}"
                )
        return "\n".join(lines)
    
    def calculate_growth_ratios(self, benchmark_name: str) -> List[Dict]:
        """
        Calculate growth growth ratios between consecutive sizes.
        
        Helps verify complexity: 
        - 0(1): ratio ~ 1
        - 0(n): ratio ~ size_ratio
        - 0(n^2): ratio ~ size_ratio^2
        """
        if benchmark_name not in self.results:
            return []
        
        results = self.results[benchmark_name]
        ratios = []
        
        for i in range(1, len(results)):
            prev = results[i - 1]
            curr = results[i]
            
            size_ratio = curr.input_size / prev.input_size
            time_ratio = curr.mean_time / prev.mean_time if prev.mean_time > 0 else float('inf')
            
            #Determine implied complexity
            if time_ratio < 1.5:
                implied = "~ 0(1) or 0(log n)"
            elif 0.8 * size_ratio <= time_ratio <= 1.5 * size_ratio:
                implied = "~ 0(n)"
            elif 0.8 * (size_ratio ** 2) <= time_ratio <= 1.5 * (size_ratio ** 2):
                implied = "~ 0(n^2)"
            else:
                implied = f"ratio={time_ratio:.2f}"
            
            ratios.append({
                "from_size": prev.input_size,
                "to_size": curr.input_size,
                "size_ratio": size_ratio,
                "time_ratio": time_ratio,
                "implied_complexity": implied
            })
        return ratios
    
    def get_data_for_plotting(self) -> Dict[str, Dict[str, List]]:
        """
        Get benchmark data formatted for plotting.
        
        Returns: 
           Dictionary with structure: {benchmark_name: {"sizes": [...], "times": [...], "errors": [...]}}
           
        """
        plot_data = {}
        
        for benchmark_name, results in self.results.items():
            plot_data[benchmark_name] = {
                "sizes": [r.input_size for r in results],
                "times": [r.mean_time for r in results],
                "errors": [r.std_dev for r in results],
                "complexity": results[0].predicted_complexity if results else "0(?)"
            }
        return plot_data
    
    def demonstrate_performance_testing():
        """Demonstrate performance testing capabilities."""
        print("\n" + "=" * 70)
        print("PERFORMANCE TESTING DEMONSTRATION")
        print("=" * 70)
        
        #Use smaller sizes for demo
        tester = PerformanceTester(iterations=5)
        sizes = [100, 500, 1000, 2000]
        
        #Run benchmarks
        tester.run_all_benchmarks(sizes)
        
        #Print report
        print(tester.generate_report())
        
        #Show growth ratios for search operations
        print("\n" + "=" * 70)
        print("GROWTH RATIO ANALYSIS")
        print("=" * 70)
        
        for benchmark in ["stack_search", "queue_search", "linkedlist_search"]:
            print(f"\n{benchmark.upper()}:")
            ratios = tester.calculate_growth_ratios(benchmark)
            for r in ratios:
                print(f" n={r['from_size']} -> n={r['to_size']}: "
                      f"size*{r['size_ratio']:.1f}, time*{r['time_ratio']:.2f} "
                      f"({r['implied_complexity']})")
        return tester
    
    
    if __name__ == "__main__":
        demonstrate_performance_testing()