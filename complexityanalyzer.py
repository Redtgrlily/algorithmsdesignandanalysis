"""
Complexity Analyzer Module
==========================
Provides Big-O complexity predictions for data structure operations
and theoretical analysis tools.

Author: Kaitlyn McCormick
Course: CSC506 - Design and Analysis of Algorithms
Module: 1 - Data Structures and Algorithm Complexity
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple
from enum import Enum


class ComplexityClass(Enum):
    """Big-O complexity classifications."""
    O_1 = "O(1)"           # Constant
    O_LOG_N = "O(log n)"   # Logarithmic
    O_N = "O(n)"           # Linear
    O_N_LOG_N = "O(n log n)"  # Linearithmic
    O_N_SQUARED = "O(n²)"  # Quadratic
    O_N_CUBED = "O(n³)"    # Cubic
    O_2_N = "O(2ⁿ)"        # Exponential
    O_N_FACTORIAL = "O(n!)"  # Factorial


@dataclass
class ComplexityAnalysis:
    """
    Represents the complexity analysis for an operation.
    
    Attributes:
        operation: Name of the operation
        time_best: Best-case time complexity
        time_average: Average-case time complexity
        time_worst: Worst-case time complexity
        space: Space complexity
        explanation: Detailed explanation of why
    """
    operation: str
    time_best: str
    time_average: str
    time_worst: str
    space: str
    explanation: str


class ComplexityAnalyzer:
    """
    Analyzes and predicts Big-O complexity for data structure operations.
    
    This tool provides:
    1. Theoretical complexity for standard operations
    2. Explanations of why each complexity applies
    3. Comparison across data structures
    4. Recommendations for use cases
    """
    
    # Complexity data for each data structure
    COMPLEXITY_DATA: Dict[str, Dict[str, ComplexityAnalysis]] = {
        "stack": {
            "push": ComplexityAnalysis(
                operation="push",
                time_best="O(1)",
                time_average="O(1)",
                time_worst="O(1)*",
                space="O(1)",
                explanation="Push adds element at top with direct pointer access. "
                           "*Worst case O(n) occurs if underlying array needs resizing."
            ),
            "pop": ComplexityAnalysis(
                operation="pop",
                time_best="O(1)",
                time_average="O(1)",
                time_worst="O(1)",
                space="O(1)",
                explanation="Pop removes element from top with direct pointer access. "
                           "No traversal required as we maintain reference to top."
            ),
            "peek": ComplexityAnalysis(
                operation="peek",
                time_best="O(1)",
                time_average="O(1)",
                time_worst="O(1)",
                space="O(1)",
                explanation="Peek simply returns top element without modification. "
                           "Direct access via maintained top pointer."
            ),
            "search": ComplexityAnalysis(
                operation="search",
                time_best="O(1)",
                time_average="O(n)",
                time_worst="O(n)",
                space="O(1)",
                explanation="Search requires traversing stack elements. Best case O(1) "
                           "if element is at top; worst case O(n) if at bottom or not present."
            ),
        },
        "queue": {
            "enqueue": ComplexityAnalysis(
                operation="enqueue",
                time_best="O(1)",
                time_average="O(1)",
                time_worst="O(1)",
                space="O(1)",
                explanation="Enqueue adds to rear using maintained tail pointer. "
                           "Using deque ensures O(1) even for list-based implementation."
            ),
            "dequeue": ComplexityAnalysis(
                operation="dequeue",
                time_best="O(1)",
                time_average="O(1)",
                time_worst="O(1)",
                space="O(1)",
                explanation="Dequeue removes from front. Using deque (double-ended queue) "
                           "ensures O(1). Note: naive list implementation would be O(n)."
            ),
            "peek": ComplexityAnalysis(
                operation="peek",
                time_best="O(1)",
                time_average="O(1)",
                time_worst="O(1)",
                space="O(1)",
                explanation="Peek returns front element via direct index access. "
                           "No modification or traversal required."
            ),
            "search": ComplexityAnalysis(
                operation="search",
                time_best="O(1)",
                time_average="O(n)",
                time_worst="O(n)",
                space="O(1)",
                explanation="Search requires linear traversal through queue. "
                           "Best case if element at front; worst case at rear or not present."
            ),
        },
        "linked_list": {
            "insert_head": ComplexityAnalysis(
                operation="insert_head",
                time_best="O(1)",
                time_average="O(1)",
                time_worst="O(1)",
                space="O(1)",
                explanation="Insert at head creates new node and updates head pointer. "
                           "No traversal needed regardless of list size."
            ),
            "insert_tail": ComplexityAnalysis(
                operation="insert_tail",
                time_best="O(1)",
                time_average="O(1)",
                time_worst="O(1)",
                space="O(1)",
                explanation="With tail pointer maintained, insert at tail is O(1). "
                           "Without tail pointer, would require O(n) traversal."
            ),
            "insert_position": ComplexityAnalysis(
                operation="insert_position",
                time_best="O(1)",
                time_average="O(n)",
                time_worst="O(n)",
                space="O(1)",
                explanation="Must traverse to position before inserting. "
                           "Best case O(1) at head; average/worst case O(n) for middle/end."
            ),
            "delete": ComplexityAnalysis(
                operation="delete",
                time_best="O(1)",
                time_average="O(n)",
                time_worst="O(n)",
                space="O(1)",
                explanation="Must search for element before deletion. "
                           "Best case O(1) if at head; worst case O(n) for traversal."
            ),
            "search": ComplexityAnalysis(
                operation="search",
                time_best="O(1)",
                time_average="O(n)",
                time_worst="O(n)",
                space="O(1)",
                explanation="Linear search through nodes required. No random access. "
                           "Best case if at head; worst case at tail or not present."
            ),
            "access": ComplexityAnalysis(
                operation="access",
                time_best="O(1)",
                time_average="O(n)",
                time_worst="O(n)",
                space="O(1)",
                explanation="Must traverse from head to reach index. Unlike arrays, "
                           "linked lists don't support O(1) random access."
            ),
        }
    }
    
    # Comparison with arrays for context
    ARRAY_COMPLEXITY: Dict[str, ComplexityAnalysis] = {
        "access": ComplexityAnalysis(
            operation="access",
            time_best="O(1)",
            time_average="O(1)",
            time_worst="O(1)",
            space="O(1)",
            explanation="Arrays provide direct index calculation: address = base + (index * size). "
                       "Constant time regardless of array size."
        ),
        "insert_end": ComplexityAnalysis(
            operation="insert_end",
            time_best="O(1)",
            time_average="O(1)",
            time_worst="O(n)",
            space="O(1)",
            explanation="Amortized O(1) with dynamic arrays. Worst case O(n) when "
                       "array needs resizing (copy all elements to new allocation)."
        ),
        "insert_beginning": ComplexityAnalysis(
            operation="insert_beginning",
            time_best="O(n)",
            time_average="O(n)",
            time_worst="O(n)",
            space="O(1)",
            explanation="Must shift all existing elements right. Always O(n) "
                       "regardless of array implementation."
        ),
        "search": ComplexityAnalysis(
            operation="search",
            time_best="O(1)",
            time_average="O(n)",
            time_worst="O(n)",
            space="O(1)",
            explanation="Unsorted array requires linear search. Sorted array can use "
                       "binary search for O(log n), but standard search is O(n)."
        ),
    }
    
    @classmethod
    def get_complexity(cls, structure: str, operation: str) -> ComplexityAnalysis:
        """
        Get complexity analysis for a specific operation.
        
        Args:
            structure: Name of data structure (stack, queue, linked_list)
            operation: Name of operation
            
        Returns:
            ComplexityAnalysis object with full analysis
            
        Raises:
            ValueError: If structure or operation not found
        """
        structure = structure.lower().replace(" ", "_")
        operation = operation.lower().replace(" ", "_")
        
        if structure not in cls.COMPLEXITY_DATA:
            raise ValueError(f"Unknown data structure: {structure}")
        
        if operation not in cls.COMPLEXITY_DATA[structure]:
            raise ValueError(f"Unknown operation '{operation}' for {structure}")
        
        return cls.COMPLEXITY_DATA[structure][operation]
    
    @classmethod
    def get_all_complexities(cls, structure: str) -> Dict[str, ComplexityAnalysis]:
        """Get all operation complexities for a data structure."""
        structure = structure.lower().replace(" ", "_")
        if structure not in cls.COMPLEXITY_DATA:
            raise ValueError(f"Unknown data structure: {structure}")
        return cls.COMPLEXITY_DATA[structure]
    
    @classmethod
    def compare_structures(cls, operation: str) -> Dict[str, ComplexityAnalysis]:
        """
        Compare how different structures perform the same operation type.
        
        Args:
            operation: Type of operation (insert, delete, search)
            
        Returns:
            Dict mapping structure names to their complexity for that operation
        """
        results = {}
        operation_map = {
            "insert": {
                "stack": "push",
                "queue": "enqueue",
                "linked_list": "insert_head",
            },
            "delete": {
                "stack": "pop",
                "queue": "dequeue",
                "linked_list": "delete",
            },
            "search": {
                "stack": "search",
                "queue": "search",
                "linked_list": "search",
            }
        }
        
        operation = operation.lower()
        if operation not in operation_map:
            # Try direct operation lookup
            for struct, ops in cls.COMPLEXITY_DATA.items():
                if operation in ops:
                    results[struct] = ops[operation]
            return results
        
        for struct, op_name in operation_map[operation].items():
            results[struct] = cls.COMPLEXITY_DATA[struct][op_name]
        
        return results
    
    @classmethod
    def predict_operations(cls, structure: str, n: int, operation: str) -> Dict[str, any]:
        """
        Predict number of operations for a given input size.
        
        Args:
            structure: Data structure name
            n: Input size
            operation: Operation to analyze
            
        Returns:
            Dict with predictions for best, average, and worst cases
        """
        import math
        
        analysis = cls.get_complexity(structure, operation)
        
        def complexity_to_count(complexity: str, n: int) -> int:
            """Convert Big-O notation to estimated operation count."""
            complexity = complexity.replace("*", "").strip()
            
            if complexity == "O(1)":
                return 1
            elif complexity == "O(log n)":
                return max(1, int(math.log2(n)))
            elif complexity == "O(n)":
                return n
            elif complexity == "O(n log n)":
                return int(n * math.log2(n)) if n > 1 else 1
            elif complexity in ["O(n²)", "O(n^2)"]:
                return n * n
            else:
                return n  # Default to linear
        
        return {
            "structure": structure,
            "operation": operation,
            "input_size": n,
            "best_case": {
                "complexity": analysis.time_best,
                "estimated_ops": complexity_to_count(analysis.time_best, n)
            },
            "average_case": {
                "complexity": analysis.time_average,
                "estimated_ops": complexity_to_count(analysis.time_average, n)
            },
            "worst_case": {
                "complexity": analysis.time_worst,
                "estimated_ops": complexity_to_count(analysis.time_worst, n)
            },
            "space": analysis.space
        }
    
    @classmethod
    def get_recommendations(cls, use_case: str) -> List[Tuple[str, str]]:
        """
        Get data structure recommendations based on use case.
        
        Args:
            use_case: Description of the use case
            
        Returns:
            List of (structure, reason) tuples ranked by suitability
        """
        use_case = use_case.lower()
        
        recommendations = []
        
        # LIFO patterns - Stack
        if any(word in use_case for word in ["undo", "redo", "backtrack", "reverse", 
                                              "nested", "recursive", "dfs", "depth"]):
            recommendations.append((
                "Stack",
                "LIFO (Last-In-First-Out) pattern matches undo/redo and backtracking needs. "
                "O(1) push/pop operations ideal for state management."
            ))
        
        # FIFO patterns - Queue
        if any(word in use_case for word in ["schedule", "buffer", "bfs", "breadth",
                                              "order", "first come", "fifo", "request"]):
            recommendations.append((
                "Queue",
                "FIFO (First-In-First-Out) pattern matches scheduling and buffering needs. "
                "O(1) enqueue/dequeue ideal for processing items in arrival order."
            ))
        
        # Dynamic insertion patterns - Linked List
        if any(word in use_case for word in ["insert", "delete", "dynamic", "unknown size",
                                              "frequent add", "frequent remove", "middle"]):
            recommendations.append((
                "Linked List",
                "Dynamic memory allocation and O(1) insertion at head make it ideal "
                "for frequent modifications. No shifting required like arrays."
            ))
        
        # If nothing specific matched, provide general guidance
        if not recommendations:
            recommendations = [
                ("Stack", "Use when you need LIFO access pattern (most recent first)."),
                ("Queue", "Use when you need FIFO access pattern (first come, first served)."),
                ("Linked List", "Use when you need dynamic size and frequent insertions/deletions."),
            ]
        
        return recommendations
    
    @classmethod
    def format_complexity_table(cls, structure: str) -> str:
        """Generate a formatted complexity table for a data structure."""
        complexities = cls.get_all_complexities(structure)
        
        lines = [
            f"\n{'=' * 70}",
            f"COMPLEXITY ANALYSIS: {structure.upper().replace('_', ' ')}",
            f"{'=' * 70}",
            f"{'Operation':<18} {'Best':^10} {'Average':^10} {'Worst':^10} {'Space':^10}",
            f"{'-' * 70}"
        ]
        
        for op_name, analysis in complexities.items():
            lines.append(
                f"{op_name:<18} {analysis.time_best:^10} {analysis.time_average:^10} "
                f"{analysis.time_worst:^10} {analysis.space:^10}"
            )
        
        lines.append(f"{'=' * 70}")
        return "\n".join(lines)
    
    @classmethod
    def format_comparison_table(cls, operation: str) -> str:
        """Generate a comparison table across all structures for an operation."""
        comparisons = cls.compare_structures(operation)
        
        lines = [
            f"\n{'=' * 70}",
            f"COMPLEXITY COMPARISON: {operation.upper()} OPERATION",
            f"{'=' * 70}",
            f"{'Structure':<15} {'Best':^10} {'Average':^10} {'Worst':^10} {'Space':^10}",
            f"{'-' * 70}"
        ]
        
        for struct, analysis in comparisons.items():
            lines.append(
                f"{struct:<15} {analysis.time_best:^10} {analysis.time_average:^10} "
                f"{analysis.time_worst:^10} {analysis.space:^10}"
            )
        
        lines.append(f"{'=' * 70}")
        return "\n".join(lines)


def demonstrate_analyzer():
    """Demonstrate the complexity analyzer features."""
    print("\n" + "=" * 70)
    print("COMPLEXITY ANALYZER DEMONSTRATION")
    print("=" * 70)
    
    # Show complexity tables
    for structure in ["stack", "queue", "linked_list"]:
        print(ComplexityAnalyzer.format_complexity_table(structure))
    
    # Show comparison
    for op in ["insert", "delete", "search"]:
        print(ComplexityAnalyzer.format_comparison_table(op))
    
    # Show predictions
    print("\n" + "=" * 70)
    print("OPERATION COUNT PREDICTIONS")
    print("=" * 70)
    
    for n in [100, 1000, 10000]:
        pred = ComplexityAnalyzer.predict_operations("linked_list", n, "search")
        print(f"\nLinked List Search with n={n}:")
        print(f"  Best case:    {pred['best_case']['complexity']} = ~{pred['best_case']['estimated_ops']} operations")
        print(f"  Average case: {pred['average_case']['complexity']} = ~{pred['average_case']['estimated_ops']} operations")
        print(f"  Worst case:   {pred['worst_case']['complexity']} = ~{pred['worst_case']['estimated_ops']} operations")
    
    # Show recommendations
    print("\n" + "=" * 70)
    print("USE CASE RECOMMENDATIONS")
    print("=" * 70)
    
    use_cases = [
        "undo/redo functionality in text editor",
        "task scheduler for batch processing",
        "dynamic playlist with frequent additions"
    ]
    
    for use_case in use_cases:
        print(f"\nUse case: '{use_case}'")
        recs = ComplexityAnalyzer.get_recommendations(use_case)
        for struct, reason in recs:
            print(f"  → {struct}: {reason}")


if __name__ == "__main__":
    demonstrate_analyzer()