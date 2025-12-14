"""
Data structure learning tool - main interface
---------------------------------------------
Interactive command-line interface for exploring data structures,
analyzing complexity, and comparing performance.

Author: Kaitlyn McCormick
Course: CSC506 - Design and Analysis of Algorithms
Module: 1 - Data Structures and Algorithm Complexity
"""

import os
import sys
from typing import Optional

from data_structures import Stack, Queue, LinkedList, demonstrate_stack, demonstrate_queue, demonstrate_linked_list
from complexity_analyzer import ComplexityAnalyzer
from performance_tester import PerformanceTester
from visualizer import DataStructureVisualizer

class DataStructureLearningTool:
    """
    Main interface for the Data Structure Learning Tool.
    
    Provides an interactive menu-driven interface for: 
    1. Exploring data structure operations
    2. Analyzing Big-O complexity
    3. Running performance benchmarks
    4. Generating visualizations
    """
    
    def __init__(self):
        """Initialize the learning tool."""
        self.stack = Stack()
        self.queue = Queue()
        self.linked_list = LinkedList()
        self.tester = PerformanceTester(iterations=5)
        self.visualizer = DataStructureVisualizer(output_dir="/home/data_structure_learning_tool/output")
        
        # Ensure output directory exists
        os.makedirs("/home/data_structure_learning_tool/output", exist_ok=True)
        
    def print_header(self, title: str):
        """Print a formatted section header."""
        print("\n" + "=" * 70)
        print(f"  {title}")
        print("=" * 70)
        
    def print_menu(self, title: str, options: list):
        """Print a formatted menu."""
        self.print_header(title)
        for i, option in enumerate(options, 1):
            print(f"   {i}. {option}")
        print(f"  0. Back/Exit")
        print("-" * 70)
    
    def get_choice(self, max_choice: int) -> int:
        """Get user menu choice."""
        while True:
            try:
                choice = int(input("\nEnter choice: "))
                if 0 <= choice <= max_choice:
                    return choice
                print(f"Please enter a number between 0 and {max_choice}")
            except ValueError:
                print("Please enter a valid number.")
    
    def get_value(self, prompt: str = "Enter value: ") -> str:
        """Get a value from user."""
        return input(prompt)
    
    #=================================================================
    # MAIN MENU
    #=================================================================
    
    def run(self):
        """Run the main application loop."""
        print("\n" + "=" * 70)
        print("  WELCOME TO THE DATA STRUCTURE LEARNING TOOL")
        print(" CSC506 - Design and Analysis of Algorithms")
        print("=" * 70)
        print("\nThis tool demonstrates fundamental data structures and helps you")
        print("understand algorithm complexity through interactive exploration.")
        
        while True:
            options = [
                "Interactive Data Structure Demo",
                "Complexity Analyzer",
                "Performance Benchmarks",
                "Generate Visualizations",
                "View Use Case Recommendations",
                "Run Complete Demo (All Features)"
            ]
            self.print_menu("MAIN MENU", options)
            
            choice = self.get_choice(len(options))
            
            if choice == 0:
                print("\nThank you for using the Data Structure Learning Tool!")
                break
            elif choice == 1:
                self.interactive_demo_menu()
            elif choice == 2:
                self.complexity_menu()
            elif choice == 3:
                self.benchmark_menu()
            elif choice == 4:
                self.visualization_menu()
            elif choice == 5:
                self.use_case_menu()
            elif choice == 6:
                self.run_complete_demo()
    #=================================================================
    # INTERACTIVE DEMO MENU
    #=================================================================
                
    def interactive_demo_menu(self):
        """Interactive data structure demonstrations."""
        while True:
            options = [
                "Stack Operations (LIFO)",
                "Queue Operations (FIFO)",
                "Linked List Operations",
                "View All Demonstrations"
            ]
            self.print_menu("INTERACTIVE DATA STRUCTURE DEMO", options)
        
            choice = self.get_choice(len(options))
            
            if choice == 0:
                break
            elif choice == 1:
                self.stack_demo()
            elif choice == 2:
                self.queue_demo()
            elif choice == 3:
                self.linked_list_demo()
            elif choice == 4:
                demonstrate_stack()
                demonstrate_queue()
                demonstrate_linked_list()
    
    def stack_demo(self):
        """Interactive stack demonstration."""
        stack = Stack()
        
        while True:
            self.print_header("STACK OPERATIONS")
            print(f"\nCurrent stack: {stack.display()}")
            print(f"Size: {len(stack)}")
            
            options = [
                "Push (add to top)",
                "Pop (remove from top)",
                "Peek (view top)",
                "Search for value",
                "Clear stack"
            ]
            self.print_menu("Stack Menu", options)
            
            choice = self.get_choice(len(options))
            
            if choice == 0:
                break
            elif choice == 1:
                value = self.get_value("Value to push: ")
                stack.push(value)
                print(f"Pushed '{value}' - 0(1) operation")
            elif choice == 2:
                value = stack.pop()
                if value is not None:
                    print(f"Popped '{value}' - 0(1) operation")
                else:
                    print("x Stack is empty")
            elif choice == 3:
                value = stack.peek()
                if value is not None:
                    print(f"Top element: '{value} - 0(1) operation")
                else:
                    print("Stack is empty")
            elif choice == 4:
                target = self.get_value("Value to search: ")
                result = stack.search(target)
                if result != -1:
                    print(f" Found at distance {result} from top - 0(n) operation")
                else:
                    print(f"x '{target}' not found - 0(n) operation")
            elif choice == 5:
                stack = Stack()
                print(" Stack cleared")
    
    def queue_demo(self):
        """Interactive queue demonstration"""
        queue = Queue()
        
        while True:
            self.print_header("QUEUE OPERATIONS")
            print(f"\nCurrent queue: {queue.display()}")
            print(f"Size: {len(queue)}")
            
            options = [
                "Enqueue (add to rear)",
                "Dequeue (remove from front)",
                "Peek (view front)",
                "Search for value",
                "Clear queue"
            ]
            self.print_menu("Queue Menu", options)
            
            choice = self.get_choice(len(options))
            
            if choice == 0:
                break
            elif choice == 1:
                value = self.get_value("Value to enqueue: ")
                queue.enqueue(value)
                print(f" Enqueued '{value}' - 0(1) operation")
            elif choice == 2:
                value = queue.dequeue()
                if value is not None:
                    print(f" Dequeued '{value}' - 0(1) operation")
                else:
                    print("x Queue is empty")
            elif choice == 3:
                value = queue.peek()
                if value is not None:
                    print(f"Front element: '{value}' - 0(1) operation")
                else:
                    print("Queue is empty")
            elif choice == 4:
                target = self.get_value("Value to search: ")
                result = queue.search(target)
                if result != -1:
                    print(f" Found at position {result} from front 0(n) operation")
                else:
                    print(f"x '{target}' not found 0(n) operation")
            elif choice == 5:
                queue = Queue()
                print(" Queue cleared")
    
    def linked_list_demo(self):
        """Interactive linked list demonstration."""
        ll = LinkedList()
        
        while True:
            self.print_header("LINKED LIST OPERATIONS")
            print(f"\nCurrent list: {ll.display()}")
            print(f"Size: {len(ll)}")
            
            options = [
                "Insert at head",
                "Insert at tail",
                "Insert at position",
                "Delete value",
                "Search for value",
                "Access by index",
                "Clear list"
            ]
            self.print_menu("Linked List Menu", options)
            
            choice = self.get_choice(len(options))
            
            if choice == 0:
                break
            elif choice == 1:
                value = self.get_value("Value to insert: ")
                ll.insert_at_head(value)
                print(f" Inserted '{value}' at head - 0(1) operation")
            elif choice == 2:
                value = self.get_value("Value to insert: ")
                ll.insert_at_tail(value)
                print(f"  Inserted '{value}' at tail - 0(1) with tail pointer")
            elif choice == 3:
                value = self.get_value("Value to insert: ")
                try:
                    pos = int(self.get_value("Position (0-based): "))
                    if ll.insert_at_position(value, pos):
                        print(f" Inserted '{value}' at position {pos} - 0(n) operation")
                    else:
                        print("x Invalid position")
                except ValueError:
                    print("Invalid position number")
            elif choice == 4:
                target = self.get_value("Value to delete: ")
                if ll.delete(target):
                    print(f" Deleted '{target}' - 0(n) operation")
                else:
                    print(f"x '{target}' not found")
            elif choice == 5:
                target = self.get_value("Value to search: ")
                result = ll.search(target)
                if result != -1:
                    print(f" Found at index {result} - 0(n) operation")
                else:
                    print(f"x '{target}' not found - 0(n) operation")
            elif choice == 6:
                try:
                    idx = int(self.get_value("Index to access: "))
                    value = ll.get(idx)
                    if value is not None:
                        print(f"Value at index {idx}: '{value}' - 0(n) operation")
                    else:
                        print("x Invalid index")
                except ValueError:
                    print("Invalid index number")
            elif choice == 7:
                ll = LinkedList()
                print(" List cleared")
    
    #=================================================================
    # COMPLEXITY MENU
    #=================================================================
    
    def complexity_menu(self):
        """Complexity analysis menu."""
        while True:
            options = [
                "View Stack Complexity",
                "View Queue Complexity",
                "View Linked List Complexity",
                "Compare All Structures",
                "Predict Operations for Input Size"
            ]
            self.print_menu("COMPLEXITY ANALYZER", options)
            
            choice = self.get_choice(len(options))
            
            if choice == 0:
                break
            elif choice == 1:
                print(ComplexityAnalyzer.format_complexity_table("stack"))
                self._show_explanations("stack")
            elif choice == 2:
                print(ComplexityAnalyzer.format_complexity_table("queue"))
                self._show_explanations("queue")
            elif choice == 3:
                print(ComplexityAnalyzer.format_complexity_table("linked_list"))
                self._show_explanations("linked_list")
            elif choice == 4:
                for op in ["insert", "delete", "search"]:
                    print(ComplexityAnalyzer.format_comparison_table(op))
            elif choice == 5:
                self._predict_operations()
    
    def _show_explanations(self, structure: str):
        """Show detailed explanations for a structure's complexities."""                
        print("\nDetailed Explanations:")
        print("-" * 70)
        complexities = ComplexityAnalyzer.get_all_complexities(structure)
        for op_name, analysis in complexities.items():
            print(f"\n{op_name.upper()}:")
            print(f"   {analysis.explanation}")
    
    def _predict_operations(self):
        """Predict operations for a given input size."""
        print("\nSelect data structure:")
        structures = ["stack", "queue", "linked_list"]
        for i, s in enumerate(structures, 1):
            print(f"  {i}. {s}")
        
        try:
            struct_choice = int(input("Choice: ")) - 1
            structure = structures[struct_choice]
            
            operations = list(ComplexityAnalyzer.get_all_complexities(structure).keys())
            print(f"\nSelect operation for {structure}:")
            for i, op in enumerate(operations, 1):
                print(f  {i}. {op})
            
            op_choice = int(input("Choice: ")) - 1
            operation = operations[op_choice]
            
            n = int(input("Input size (n): "))
            
            prediction = ComplexityAnalyzer.predict_operations(structure, n, operation)
            
            self.print_header(f"PREDICTION: {structure}.{operation}(n={n})")
            print(f"\nBest case:    {prediction['best_case']['complexity']:10} ~ {prediction['best_case']['estimated_ops']:,} operations")
            print(f"Average case: {prediction['average_case']['complexity']:10} ~ {prediction['average_case']['estimated_ops']:,} operations")
            print(f"Worst case:   {prediction['worst_case']['complexity']:10} ~ {prediction['worst_case']['estimated_ops']:,} operations")
            print(f"Space:    {prediction['space']}")
        except (ValueError, IndexError):
            print("Invalid selection")
    
    #=================================================================
    # BENCHMARK MENU
    #=================================================================
    
    def benchmark_menu(self):
        """Performance benchmark menu."""
        while True:
            options = [
                "Run Quick Benchmark (small sizes)",
                "Run Full Benchmark (larger sizes)",
                "Run Custom Benchmark",
                "View Last Results",
                "View Growth Ratio Analysis"
            ]
            self.print_menu("PERFORMANCE BENCHMARKS", options)
            
            choice = self.get_choice(len(options))
            
            if choice == 0:
                break
            elif choice == 1:
                self.tester = PerformanceTester(iterations=3)
                self.tester.run_all_benchmarks([100, 500, 1000])
                print(self.tester.generate_report())
            elif choice == 2:
                self.tester = PerformanceTester(iterations=5)
                self.tester.run_all_benchmarks([100, 500, 1000, 5000, 10000])
                print(self.tester.generate_report())
            elif choice == 3:
                self._custom_benchmark()
            elif choice == 4:
                if self.tester.results:
                    print(self.tester.generate_report())
                else:
                    print("No benchmark results yet. Run a benchmark first.")
            elif choice == 5:
                self._show_growth_analysis()
    
    def _custom_benchmark(self):
        """Run custom benchmark with user-specified parameters."""
        try:
            iterations = int(input("Number of iterations per test (default: 5): ") or "5")
            sizes_str = input("Input sizes (comma-separated, e.g., 100,500,1000): ")
            sizes = [int(s.strip()) for s in sizes_str.split(",")]
            
            self.tester = PerformanceTester(iterations=iterations)
            self.tester.run_all_benchmarks(sizes)
            print(self.tester.generate_report())
        except ValueError:
            print("Invalid input")
            
    def _show_growth_analysis(self):
        """Show growth ratio analysis for benchmarks."""
        if not self.tester.results:
            print("No benchmark results yet. Run a benchmark first.")
            return
        
        self.print_header("GROWTH RATIO ANALYSIS")
        print("\nGrowth ratios help verify complexity predictions:")
        print("   - 0(1): ratio ~ 1 (constant)")
        print("   - 0(n): ratio ~ size_ratio (linear)")
        print("   - 0(n^2): ratio ~ size_ratio^2 (quadratic)")
        print("-" * 70)
        
        for benchmark in self.tester.results.keys():
            print(f"\n{benchmark.upper()}:")
            ratios = self.tester.calculate_growth_ratios(benchmark)
            for r in ratios:
                print(f"  n={r['from_size']:>5} -> n={r['to_size']:>5}"
                      f"size*{r['size_ratio']:.1f}, time*{r['time_ratio']:.2f} "
                      f"({r['implied_complexity']})")
    
    #=================================================================
    # VISUALIZATION MENU
    #=================================================================
    
    def visualization_menu(self):
        """Visualization generation menu."""
        while True:
            options = [
                "Generate Complexity Curves Chart",
                "Generate Performance Comparison Charts",
                "Generate Data Structure Diagrams",
                "Generate All Charts",
                "List Generated Files"
            ]
            self.print_menu("VISUALIZATION GENERATOR", options)
            
            choice = self.get_choice(len(options))
            
            if choice == 0:
                break
            elif choice == 1:
                path = "/home/data_structure_learning_tool/output/complexity_curves.png"
                self.visualizer.plot_complexity_curves(save_path=path)
            elif choice == 2:
                if not self.tester.results:
                    print("Running benchmark first...")
                    self.tester.run_all_benchmarks([100, 500, 1000, 2000])
                    
                path = "/home/data_structure_learning_tool/output/performance_comparison.png"
                self.visualizer.plot_all_operations(self.tester, save_path=path)
            elif choice == 3:
                for struct in ["stack", "queue", "linked_list"]:
                    path = f"/home/data_structure_learning_tool/output/{struct}_diagram.png"
                    self.visualizer.plot_structure_diagram(struct, save_path=path)
            elif choice == 4:
                if not self.tester.results:
                    print("Running benchmark first...")
                    self.tester.run_all_benchmarks([100, 500, 1000, 2000])
                
                files = self.visualizer.generate_all_charts(self.tester)
                print(f"\nGenerated {len(files)} files")
            elif choice == 5:
                self._list_output_files()
    
    def _list_output_files(self):
        """List files in output directory."""
        output_dir = "/home/data_structure_learning_tool/output"
        if os.path.exists(output_dir):
            files = os.listdir(output_dir)
            if files:
                print(f"\nFiles in {output_dir}:")
                for f in sorted(files):
                    print(f"  - {f}")
            else:
                print("No files generated yet")
        else:
            print("Output directory not created yet")
    
    #=================================================================
    # USE CASE MENU
    #=================================================================
    
    def use_case_menu(self):
        """Use case recommendations menu."""
        while True:
            options = [
                "Get Recommendation for Custom Use Case",
                "View Common Use Cases",
                "Compare Structures for Operation"
            ]
            self.print_menu("USE CASE RECOMMENDATIONS", options)
            
            choice = self.get_choice(len(options))
            
            if choice == 0:
                break
            elif choice == 1:
                use_case = input("\nDescribe your use case: ")
                recs = ComplexityAnalyzer.get_recommendations(use_case)
                print(f"\nRecommendations for: '{use_case}")
                print("-" * 50)
                for i, (struct, reason) in enumerate(recs, 1):
                    print(f"\n{i}. {struct}")
                    print(f"  {reason}")
            elif choice == 2:
                self._show_common_use_cases()
            elif choice == 3:
                self._compare_for_operation()
    def _show_common_use_cases(self):
        """Show common use cases for each structure."""
        self.print_header("COMMON USE CASES")
        
        use_cases = {
            "STACK (LIFO)": [
                "Function call stack management",
                "Undo/Redo operations in editors",
                "Expression evaluation (postfix/prefix)",
                "Syntax parsing and bracket matching",
                "Backtracking algorithms (maze solving, DFS)",
                "Browser history (back button)"
            ],
            "QUEUE (FIFO)": [
                "Task scheduling (CPU, print queue)",
                "Breadth-First Search (BFS)",
                "Message queues in distributed systems",
                "Request handling in web servers",
                "Data buffering in ETL pipelines",
                "Order processing systems"
            ],
            "LINKED LIST": [
                "Dynamic memory allocation needs",
                "Frequent insertions/deletions",
                "Implementation of stacks and queues",
                "Hash table collision handling (chaining)",
                "Music playlist management",
                "Polynomial arithmetic"
            ]
        }
        
        for struct, cases in use_cases.items():
            print(f"\n{struct}:")
            for case in cases:
                print(f"  - {case}")
    
    def _compare_for_operation(self):
        """Compare structures for a specific operation."""
        print("\nSelect operation to compare:")
        ops = ["insert", "delete", "search"]
        for i, op in enumerate(ops, 1):
            print(f"  {i}. {op}")
        
        try:
            choice = int(input("Choice: ")) - 1
            operation = ops[choice]
            print(ComplexityAnalyzer.format_comparison_table(operation))
        except (ValueError, IndexError):
            print("Invalid selection")
    
    #=================================================================
    # COMPLETE DEMO
    #=================================================================
    
    def run_complete_demo(self):
        """Run a complete demonstration of all features."""
        self.print_header("RUNNING COMPLETE DEMONSTRATION")
        
        print("\n" + "-" * 70)
        print("PART 1: DATA STRUCTURE DEMONSTRATIONS")
        print("-" * 70)
        
        demonstrate_stack()
        demonstrate_queue()
        demonstrate_linked_list()
        
        print("\n" + "-" * 70)
        print("PART 2: COMPLEXITY ANALYSIS")
        print("-" * 70)
        
        for structure in ["stack", "queue", "linked_list"]:
            print(ComplexityAnalyzer.format_complexity_table(structure))
        
        print("\n" + "-" * 70)
        print("PART 3: PERFORMANCE BENCHMARKS")
        print("-" * 70)
        
        self.tester = PerformanceTester(iterations=3)
        self.tester.run_all_benchmarks([100, 500, 1000, 2000])
        print(self.tester.generate_report())
        
        print("\n" + "-" * 70)
        print("PART 4: GROWTH RATIO ANALYSIS")
        print("-" * 70)
        
        for benchmark in ["stack_search", "queue_search", "linkedList_search"]:
            print(f"\n{benchmark.upper()}:")
            ratios = self.tester.calculate_growth_ratios(benchmark)
            for r in ratios:
                print(f"  n={r['from_size']:>5} -> n={r['to_size']:>5}: "
                      f"time*{r['time_ratio']:.2f} ({r['implied_complexity']})")
        print("\n" + "-" * 70)
        print("PART 5: GENERATING VISUALIZATIONS")
        print("-" * 70)
        
        files = self.visualizer.generate_all_charts(self.tester)
        print(f"\nGenerated {len(files)} visualization files")
        
        print("\n" + "=" * 70)
        print("COMPLETE DEMONSTRATION FINISHED")
        print("=" * 70)
        
def  main():
    """Main entry point."""
    tool = DataStructureLearningTool()
    tool.run()
    
if __name__ == "__main__":
    main()
                