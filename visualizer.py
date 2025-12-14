"""
Visualizer Module
========================
Creates visual demonstrations and charts for data structure operations
and performance comparisons. 

Author: Kaitlyn McCormick
Course: CSC506 - Design and Analysis of Algorithms
Module: 1 - Data Structures and Algorithm Complexity
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from typing import Dict, List, Optional, Tuple
from performance_tester import PerformanceTester, TimingResult

class DataStructureVisualizer:
    """
    Creates visualizations for data structure education.
    
    Provides: 
    1. Performance comparison charts
    2. Complexity growth curves
    3. Data structure state diagrams
    4. Predicted vs. actual performance charts
    """
    
    def __init__(self, output_dir: str = "."):
        """
        Initialize visualizer.
        
        Arguments: 
            output_dir: Directory to save generated charts.
        """
        self.output_dir = output_dir
        plt.style.use('seaborn-v0_8-whitegrid')
        self.colors = {
            'stack': '#2E86AB', #blue
            'queue': '#A23B72', #pink
            'linked_list': '#F18F01', #Orange
            'predicted': '#C73E1D', #red for predictions
            'actual': '#3B1F2B' # dark for actual
        }
    
    def plot_performance_comparison(self,
                                    tester: PerformanceTester,
                                    operation_type: str = "search",
                                    save_path: Optional[str] = None) -> None:
        """
        Create a comparison chart of operation performance across structures.
        
        Arguments: 
           tester: PerformanceTester with results
           operation_type: Type of oepration to compare (search, insert, etc.)
           save_path: Path to save chart (displays if None)
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        #map operation types to benchmark names
        operation_map = {
            "search": ["stack_search", "queue_search", "linkedlist_search"],
            "insert": ["stack_push", "queue_enqueue", "linkedlist_insert_head"],
            "delete": ["stack_pop", "queue_dequeue", "linkedlist_delete"]
        }
        
        benchmarks = operation_map.get(operation_type, [])
        plot_data = tester.get_data_for_plotting()
        
        for benchmark in benchmarks:
            if benchmark in plot_data:
                data = plot_data[benchmark]
                structure = benchmark.split("_")[0]
                label = f"{structure.title()} ({data['complexity']})"
                
                ax.errorbar(
                    data['sizes'],
                    data['times'],
                    yerr=data['errors'],
                    label=label,
                    marker='o',
                    capsize=3,
                    linewidth=2,
                    color=self.colors.get(structure, 'gray')
                )
        ax.set_xlabel('Input size (n)', fontsize=12)
        ax.set_ylabel('Time (seconds)', fontsize=12)
        ax.set_title(f'{operation_type.title()} Operation Performance Comparison', fontsize=14)
        ax.legend(loc='upper left')
        ax.set_xscale('linear')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"Saved chart to {save_path}")
        else:
            plt.show()
        
        plt.close()
    
    def plot_all_operations(self,
                            tester: PerformanceTester,
                            save_path: Optional[str] = None) -> None:
        """
        Create a multi-panel chart showing all operation comparisons.
        
        Arguments: 
           tester: PerformanceTester with results
           save_path: Path to save chart
        """
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        plot_data = tester.get_data_for_plotting()
        
        #Define panels
        panels = [
            ("Insert Operations", ["stack_push", "queue_enqueue", "linkedlist_insert_head"]),
            ("Remove Operations", ["stack_pop", "queue_dequeue", "linkedlist_delete"]),
            ("Search Operations", ["stack_search", "queue_search", "linkedlist_search"]),
            ("Linked List Insert Comparison", ["linkedlist_insert_head", "linkedlist_insert_tail"])
        ]
        
        for ax, (title, benchmarks) in zip(axes.flat, panels):
            for benchmark in benchmarks:
                if benchmark in plot_data:
                    data = plot_data[benchmark]
                    structure = benchmark.replace("linkedlist_", "ll_").replace("_", " ").title()
                    
                    #Determine color
                    if "stack" in benchmark:
                        color = self.colors['stack']
                    elif "queue" in benchmark:
                        color = self.colors['queue']
                    else:
                        color = self.colors['linked_list']
                    
                    ax.plot(
                        data['sizes'],
                        data['times'],
                        label=structure,
                        marker='o',
                        linewidth=2,
                        color=color,
                        alpha=0.8
                    )
        
            ax.set_xlabel('Input Size (n)')
            ax.set_ylabel('Time (seconds)')
            ax.set_title(title)
            ax.legend(loc='upper left', fontsize=8)
        
        plt.suptitle('Data Structure Performance Analysis', fontsize=16, y=1.02)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches="tight")
            print(f"Saved chart to {save_path}")
        else:
            plt.show()
        
        plt.close()
        
    def plot_complexity_curves(self,
                               max_n: int = 1000,
                               save_path: Optional[str] = None) -> None:
        """
        Plot theoretical complexity growth curves for reference.
        
        Arguments: 
           max_n: Maximum input size to plot
           save_path: Path to save chart
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        n = np.linspace(1, max_n, 100)
        
        #Theoretical curves (normalized for visualization)
        curves = {
            '0(1)': np.ones_like(n),
            '0(log n)': np.log2(n),
            '0(n)': n,
            '0(n log n)': n * np.log2(n),
            '0(n^2)': n ** 2
        }
        
        colors_complexity = ['#2E86AB', '#28A745', '#FFC107', '#DC3545', '#6F42C1']
        
        for (name, values), color in zip(curves.items(), colors_complexity):
            #Normalize to 0-100 range for visualization
            normalized = 100 * values / values[-1]
            ax.plot(n, normalized, label=name, linewidth=2, color=color)
            
        ax.set_xlabel('Input Size (n)', fontsize=12)
        ax.set_ylabel('Relative Operations (normalized)', fontsize=12)
        ax.set_title('Big-O Complexity Growth Comparison', fontsize=14)
        ax.legend(loc='upper left')
        ax.set_xlim(0, max_n)
        ax.set_ylim(0, 110)
        
        #Add annotations
        ax.annotate('Constant time\n(ideal)', xy=(max_n*0.8, 5), fontsize=9, color='#2E86AB')
        ax.annotate('Linear growth', xy=(max_n*0.6, 55), fontsize=9, color='#FFC107')
        ax.annotate('Quadratic growth\n(avoid for large n)', xy=(max_n*0.3, 85), fontsize=9, color='#6F42C1')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"Saved chart to {save_path}")
        else:
            plt.show()
        
        plt.close()
    
    def plot_predicted_vs_actual(self,
                                 tester: PerformanceTester,
                                 benchmark_name: str,
                                 save_path: Optional[str] = None) -> None:
        """
        Compare predicted complexity growth with actual measured times.
        
        Arguments: 
           tester: PerformanceTester with results
           benchmark_name: Name of benchmark to analyze
           save_path: Path to save chart
        """
        if benchmark_name not in tester.results:
            print(f"Benchmark {benchmark_name} not found")
            return
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14,5))
        
        results = tester.results[benchmark_name]
        sizes = [r.input_size for r in results]
        times = [r.mean_time for r in results]
        
        #Determine expected complexity
        complexity = results[0].predicted_complexity
        
        #Generated predicted curve (normalized to match actual data scale)
        n = np.array(sizes)
        if "0(1)" in complexity:
            predicted = np.ones_like(n, dtype=float) * times[0]
        elif "0(n)" in complexity:
            #Linear - fit to data
            predicted = n * (times[-1] / sizes[-1])
        else:
            predicted = n * (times[-1] / sizes[-1])
        
        #Left plot: actual times with error bars
        ax1.errorbar(sizes, times, yerr=[r.std_dev for r in results],
                     marker='o', capsize=3, linewidth=2,
                     color=self.colors['actual'], label='Actual')
        ax1.plot(sizes, predicted, '--', linewidth=2,
                 color=self.colors['predicted'], label=f'Predicted ({complexity})')
        
        ax1.set_xlabel('Input Size(n)')
        ax1.set_ylabel('Time (seconds)')
        ax1.set_title(f'{benchmark_name}: Predicted vs Actual')
        ax1.legend()
        
        #Right plot: Growth ratios
        ratios = tester.calculate_growth_ratios(benchmark_name)
        if ratios:
            x_labels = [f"{r['from_size']}->{r['to_size']}" for r in ratios]
            time_ratios = [r['time_ratio'] for r in ratios]
            size_ratios = [r['size_ratio'] for r in ratios]
            
            x = np.arrange(len(x_labels))
            width = 0.35
            
            bars1 = ax2.bar(x - width/2, size_ratios, width, label='Size Ratio',
                            color=self.colors['predicted'], alpha=0.7)
            bars2 = ax2.bar(x + width/2, time_ratios, width, label="Time Ratio",
                            color=self.colors['actual'], alpha=0.7)
            
            ax2.set_ylabel('Ratio')
            ax2.set_title('Growth Ratio Analysis')
            ax2.set_xticks(x)
            ax2.set_xticklabels(x_labels, rotation=45, ha='right')
            ax2.legend()
            
            #Add 0(n) reference line
            ax2.axhline(y=size_ratios[0], color='green', linestyle='--',
                        alpha=0.5, label='Expected for 0(n)')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"Saved chart to {save_path}")
        else:
            plt.show()
        
        plt.close()
    
    def plot_structure_diagram(self,
                               structure_type: str,
                               data: List = None,
                               save_path: Optional[str] = None) -> None:
        """
        Create a visual diagram of a data structure's state.
        
        Arguments: 
           structure_type: Type of structure (stack, queue, linked_list)
           data: Data to display in structure (default sample data)
           save_path: Path to save diagram
        """
        if data is None: 
            data = ['A', 'B', 'C', 'D', 'E']
        
        fig, ax = plt.subplots(figsize=(12, 4))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 4)
        ax.axis('off')
        
        if structure_type.lower() == 'stack':
            self._draw_stack(ax, data)
        elif structure_type.lower() == 'queue':
            self._draw_queue(ax, data)
        elif structure_type.lower() in ['linked_list', 'linkedlist']:
            self._draw_linked_list(ax, data)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"Saved diagram to {save_path}")
        else:
            plt.show()
            
        plt.close()
        
    def _draw_stack(self, ax, data):
        """Draw a stack diagram."""
        ax.set_title('Stack (LIFO - Last In, First Out)', fontsize=14, pad=20)
        
        #Draw stack container
        x_start = 5
        y_start = 0.5
        width = 2
        height = 0.5
        
        for i, item in enumerate(reversed(data)):
            rect = mpatches.FancyBboxPatch(
                (x_start, y_start + i * height), width, height,
                boxstyle="round,pad=0.02",
                facecolor=self.colors['stack'],
                edgecolor='black',
                alpha=0.7
            )
            ax.add_patch(rect)
            ax.text(x_start + width/2, y_start + i * height + height/2,
                    str(item), ha='center', va='center', fontsize=12, color='white')
        
        ax.annotate('TOP', xy=(x_start + width + 0.3, y_start + (len(data)-1) * height + height/2),
                    fontsize=10, color='red', fontweight='bold')
        ax.annotate('BOTTOM', xy=(x_start + width + 0.3, y_start + height/2),
                    fontsize=10, color='blue')
        
        #Operations
        ax.text(1, 3, 'Push: 0(1)', fontsize=11, color='green')
        ax.text(1, 2.5, 'Pop: 0(1)', fontsize=11, color='green')
        ax.text(1, 2, 'Peek: 0(1)', fontsize=11, color='green')
        ax.text(1, 1.5, 'Search: 0(n)', fontsize=11, color='orange')
    
    def _draw_queue(self, ax, data):
        """Draw a queue diagram."""
        ax.set_title('Queue (FIFO - First In, First Out)', fontsize=14, pad=20)
        
        #Draw queue elements horizontally
        x_start = 1
        y_start = 1.5
        width = 1.5
        height = 1
        
        for i, item in enumerate(data):
            rect = mpatches.FancyBboxPatch(
                (x_start + i * width, y_start), width, height,
                boxstyle="round,pad=0.02",
                facecolor=self.colors['queue'],
                edgecolor='black',
                alpha=0.7
            )
            ax.add_patch(rect)
            ax.text(x_start + i * width + width/2, y_start + height/2,
                    str(item), ha='center', va='center', fontsize=12, color='white')
            
            #Draw arrows between elements
            if i < len(data) - 1:
                ax.annotate('', xy=(x_start + (i+1) *  width, y_start + height/2),
                            xytext=(x_start + i * width + width, y_start + height/2),
                            arrowprops=dict(arrowstyle='->', color='gray'))
        
        #Labels
        ax.annotate('FRONT\n(dequeue)', xy=(x_start + width/2, y_start - 0.5),
                    ha='center', fontsize=10, color='red', fontweight='bold')
        ax.annotate('REAR\n(enqueue)', xy=(x_start + (len(data)-0.5) * width, y_start - 0.5),
                    ha='center', fontsize=10, color='blue', fontweight='bold')
        
        #Operations
        ax.text(1, 3.5, 'Enqueue: 0(1)', fontsize=11, color='green')
        ax.text(4, 3.5, 'Dequeue: 0(1)', fontsize=11, color='green')
        ax.text(7, 3.5, 'Search: 0(n)', fontsize=11, color='orange')
    
    def _draw_linked_list(self, ax, data):
        """Draw a linked list diagram"""
        ax.set_title('Singly Linked List', fontsize=14, pad=20)
        
        x_start = 0.5
        y_start = 1.5
        node_width = 1.5
        pointer_width = 0.5
        
        for i, item in enumerate(data):
            x = x_start + i * (node_width + pointer_width + 0.3)
            
            #Data part
            rect = mpatches.FancyBboxPatch(
                (x, y_start), node_width, 1,
                boxstyle="round,pad=0.02",
                facecolor=self.colors['linked_list'],
                edgecolor='black',
                alpha=0.7
            )
            ax.add_patch(rect)
            ax.text(x + node_width/2, y_start + 0.5,
                    str(item), ha='center', va='center', fontsize=12, color='white')
            
            #Pointer part
            if i < len(data) - 1:
                ptr_rect = mpatches.Rectangle(
                    (x + node_width, y_start), pointer_width, 1,
                    facecolor='lightgray',
                    edgecolor='black'
                )
                ax.add_patch(ptr_rect)
                ax.annotate('', xy=(x + node_width + pointer_width + 0.5, y_start + 0.5),
                            xytext=(x + node_width + pointer_width/2, y_start + 0.5),
                            arrowprops=dict(arrowstyle='->', color='black', lw=2))
            else:
                #NULL pointer
                ptr_rect = mpatches.Rectangle(
                    (x + node_width, y_start), pointer_width, 1,
                    facecolor='lightgray',
                    edgecolor='black'
                )
                ax.add_patch(ptr_rect)
                ax.text(x + node_width + pointer_width/2, y_start + 0.5,
                        '∅', ha='center', va='center', fontsize=14)
        
        #HEAD Label
        ax.annotate('HEAD', xy=(x_start + node_width/2, y_start + 1.3),
                    ha='center', fontsize=10, color='red', fontweight='bold')
        
        #Operations
        ax.text(0.5, 3.5, 'Insert Head: 0(1)', fontsize=10, color='green')
        ax.text(3.5, 3.5, 'Insert Tail: 0(1)*', fontsize=10, color='green')
        ax.text(6.5, 3.5, 'Search: 0(n)', fontsize=10, color='orange')
        ax.text(9, 3.5, 'Delete: 0(n)', fontsize=10, color='orange')
        ax.text(3.5, 0.3, '*with tail pointer', fontsize=9, style='italic')
        
    def generate_all_charts(self, tester: PerformanceTester, prefix: str = "chart") -> List[str]:
        """
        Generate all charts and save to files.
        
        Arguments: 
           tester: PerformanceTester with results
           prefix: Prefix for output filenames
        
        Returns: 
           List of saved files paths
        """
        saved_files = []
        
        #Complexity curves
        path = f"{self.output_dir}/{prefix}_complexity_curves.png"
        self.plot_complexity_curves(save_path=path)
        saved_files.append(path)
        
        #All operations comparison
        path = f"{self.output_dir}/{prefix}_all_operations.png"
        self.plot_all_operations(tester, save_path=path)
        saved_files.append(path)
        
        #Individual operation comparisons
        for op in ["search", "insert"]:
            path = f"{self.output_dir}/{prefix}_{op}_comparison.png"
            self.plot_performance_comparison(tester, op, save_path=path)
            saved_files.append(path)
            
        #Predicted vs actual for search operations
        for bench in ["stack_search", "queue_search", "linkedlist_search"]:
            if bench in tester.results:
                path = f"{self.output_dir}/{prefix}_{bench}_analysis.png"
                self.plot_predicted_vs_actual(tester, bench, save_path=path)
                saved_files.append(path)
        
        #Structure diagrams
        for struct in ["stack", "queue", "linked_list"]:
            path = f"{self.output_dir}/{prefix}_{struct}_diagram.png"
            self.plot_structure_diagram(struct, save_path=path)
            saved_files.append(path)
        
        return saved_files
    
    def demonstrate_visualizer():
        """Demonstrate visualization capabilities."""
        print("\n"+ "=" * 70)
        print("VISUALIZER DEMONSTRATION")
        print("=" * 70)
        
        #Run benchmarks first
        tester = PerformanceTester(iterations=3)
        sizes = [100, 500, 1000, 2000]
        tester.run_all_benchmarks(sizes)
        
        #Create visualizer
        viz = DataStructureVisualizer(output_dir="/home/data_structure_learning_tool")
        
        #Generate all charts
        print("\nGenerating charts...")
        saved = viz.generate_all_charts(tester)
        
        print(f"\nGenerated {len(saved)} charts:")
        for path in saved:
            print(f"  - {path}")

if __name__ == "__main__":
    demonstrate_visualizer()