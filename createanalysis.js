const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
    Header, Footer, AlignmentType, BorderStyle, WidthType,
    HeadingLevel, ShadingType, PageNumber, LevelFormat } = require('docx');
const fs = require('fs');

// Create the analysis document
const doc = new Document({
    styles: {
      default: { document: { run: { font: "Arial", size: 22 } } },
      paragraphStyles: [
        { id: "Title", name: "Title", basedOn: "Normal",
          run: { size: 48, bold: true, color: "1a365d", font: "Arial" },
          paragraph: { spacing: { before: 0, after: 200 }, alignment: AlignmentType.CENTER } },
        { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { size: 26, bold: true, color: "2c5282", font: "Arial" },
          paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 0 } },
        { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { size: 24, bold: true, color: "2d3748", font: "Arial" },
          paragraph: { spacing: { before: 180, after: 80 }, outlineLevel: 1 } }
      ]
    },
    numbering: {
      config: [
        { reference: "bullet-list",
          levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
        { reference: "numbered-list",
          levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] }
      ]
    },
    sections: [{
      properties: {
        page: { margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 } }
      },
      headers: {
        default: new Header({ children: [new Paragraph({ 
          alignment: AlignmentType.RIGHT,
          children: [new TextRun({ text: "CSC506 - Design and Analysis of Algorithms | Module 1", size: 18, italics: true, color: "666666" })]
        })] })
      },
      footers: {
        default: new Footer({ children: [new Paragraph({ 
          alignment: AlignmentType.CENTER,
          children: [new TextRun({ text: "Kaitlyn | Colorado State University Global", size: 18, color: "666666" })]
        })] })
      },
      children: [
        // Title
        new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun("Data Structure Importance and Selection Criteria")] }),
        
        // Course info
        new Paragraph({ 
          alignment: AlignmentType.CENTER,
          spacing: { after: 300 },
          children: [new TextRun({ text: "A Critical Analysis of Fundamental Data Structures for Software Design", italics: true, size: 22 })]
        }),
  
        // Introduction
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Introduction")] }),
        new Paragraph({ 
          spacing: { after: 120 },
          children: [new TextRun("Data structures are the fundamental building blocks of efficient software systems. They provide organized methods for storing, accessing, and manipulating data, directly impacting application performance, scalability, and maintainability. This analysis examines three fundamental structures—Stack, Queue, and Linked List—and establishes selection criteria based on algorithmic complexity and use case requirements.")]
        }),
  
        // Why Data Structures Matter
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Why Data Structure Selection Matters")] }),
        new Paragraph({ 
          spacing: { after: 80 },
          children: [new TextRun("Selecting the appropriate data structure is crucial because it determines the efficiency of operations that may execute millions of times in production systems. Consider the difference between O(1) and O(n) operations: at scale (n = 1,000,000), a constant-time operation completes in microseconds while a linear operation may take seconds. In real-time systems like fraud detection or ETL pipeline orchestration, this difference determines system viability.")]
        }),
        new Paragraph({ 
          spacing: { after: 120 },
          children: [new TextRun("The Abstract Data Type (ADT) concept separates "), new TextRun({ text: "what", italics: true }), new TextRun(" operations are available from "), new TextRun({ text: "how", italics: true }), new TextRun(" they are implemented. Understanding ADTs enables engineers to reason about performance guarantees without implementation details, facilitating better architectural decisions.")]
        }),
  
        // Complexity comparison table
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Complexity Comparison")] }),
        createComparisonTable(),
        new Paragraph({ spacing: { after: 120 }, children: [] }),
  
        // Selection Criteria
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Selection Criteria")] }),
        new Paragraph({ 
          numbering: { reference: "numbered-list", level: 0 },
          children: [new TextRun({ text: "Access Pattern: ", bold: true }), new TextRun("LIFO (Stack), FIFO (Queue), or sequential traversal (Linked List)")]
        }),
        new Paragraph({ 
          numbering: { reference: "numbered-list", level: 0 },
          children: [new TextRun({ text: "Operation Frequency: ", bold: true }), new TextRun("Optimize for most common operations—if insertions dominate, linked lists excel")]
        }),
        new Paragraph({ 
          numbering: { reference: "numbered-list", level: 0 },
          children: [new TextRun({ text: "Memory Constraints: ", bold: true }), new TextRun("Linked lists use extra memory for pointers; arrays offer cache locality")]
        }),
        new Paragraph({ 
          numbering: { reference: "numbered-list", level: 0 },
          children: [new TextRun({ text: "Size Predictability: ", bold: true }), new TextRun("Dynamic sizing favors linked structures; known sizes favor arrays")]
        }),
  
        // Industry Application
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Industry Application")] }),
        new Paragraph({ 
          spacing: { after: 120 },
          children: [new TextRun("In fintech data engineering, these structures solve concrete problems. ETL pipeline scheduling uses queues for FIFO job processing, ensuring data integrity. Dependency graphs between scripts (modeled with linked structures) enable cascade failure prediction. Stack-based approaches support undo/rollback functionality essential for data validation workflows. Benchmarking in this project confirmed theoretical complexity predictions: search operations scaled linearly (time doubled when input doubled), validating O(n) complexity and demonstrating that algorithm study provides accurate performance predictions for system design.")]
        }),
  
        // Conclusion
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Conclusion")] }),
        new Paragraph({ 
          children: [new TextRun("Mastery of data structures and complexity analysis transforms software engineering from trial-and-error coding to principled design. By understanding the performance characteristics of fundamental structures—and empirically validating those predictions—engineers can make informed decisions that directly impact system performance, scalability, and reliability. This foundation is essential for both technical interviews and production system architecture.")]
        })
      ]
    }]
  });
  
  function createComparisonTable() {
    const tableBorder = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
    const cellBorders = { top: tableBorder, bottom: tableBorder, left: tableBorder, right: tableBorder };
    const headerShading = { fill: "2c5282", type: ShadingType.CLEAR };
    const altRowShading = { fill: "f7fafc", type: ShadingType.CLEAR };
  
    return new Table({
      columnWidths: [2000, 1800, 1800, 1800, 2340],
      rows: [
        // Header row
        new TableRow({
          tableHeader: true,
          children: [
            new TableCell({ borders: cellBorders, width: { size: 2000, type: WidthType.DXA }, shading: headerShading,
              children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Structure", bold: true, color: "FFFFFF", size: 20 })] })] }),
            new TableCell({ borders: cellBorders, width: { size: 1800, type: WidthType.DXA }, shading: headerShading,
              children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Insert", bold: true, color: "FFFFFF", size: 20 })] })] }),
            new TableCell({ borders: cellBorders, width: { size: 1800, type: WidthType.DXA }, shading: headerShading,
              children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Delete", bold: true, color: "FFFFFF", size: 20 })] })] }),
            new TableCell({ borders: cellBorders, width: { size: 1800, type: WidthType.DXA }, shading: headerShading,
              children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Search", bold: true, color: "FFFFFF", size: 20 })] })] }),
            new TableCell({ borders: cellBorders, width: { size: 2340, type: WidthType.DXA }, shading: headerShading,
              children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Best Use Case", bold: true, color: "FFFFFF", size: 20 })] })] })
          ]
        }),
        // Stack row
        new TableRow({
          children: [
            new TableCell({ borders: cellBorders, width: { size: 2000, type: WidthType.DXA },
              children: [new Paragraph({ children: [new TextRun({ text: "Stack", bold: true, size: 20 })] })] }),
            new TableCell({ borders: cellBorders, width: { size: 1800, type: WidthType.DXA },
              children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "O(1)", size: 20, color: "38a169" })] })] }),
            new TableCell({ borders: cellBorders, width: { size: 1800, type: WidthType.DXA },
              children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "O(1)", size: 20, color: "38a169" })] })] }),
            new TableCell({ borders: cellBorders, width: { size: 1800, type: WidthType.DXA },
              children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "O(n)", size: 20, color: "dd6b20" })] })] }),
            new TableCell({ borders: cellBorders, width: { size: 2340, type: WidthType.DXA },
              children: [new Paragraph({ children: [new TextRun({ text: "Undo/Redo, DFS", size: 20 })] })] })
          ]
        }),
        // Queue row
        new TableRow({
          children: [
            new TableCell({ borders: cellBorders, width: { size: 2000, type: WidthType.DXA }, shading: altRowShading,
              children: [new Paragraph({ children: [new TextRun({ text: "Queue", bold: true, size: 20 })] })] }),
            new TableCell({ borders: cellBorders, width: { size: 1800, type: WidthType.DXA }, shading: altRowShading,
              children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "O(1)", size: 20, color: "38a169" })] })] }),
            new TableCell({ borders: cellBorders, width: { size: 1800, type: WidthType.DXA }, shading: altRowShading,
              children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "O(1)", size: 20, color: "38a169" })] })] }),
            new TableCell({ borders: cellBorders, width: { size: 1800, type: WidthType.DXA }, shading: altRowShading,
              children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "O(n)", size: 20, color: "dd6b20" })] })] }),
            new TableCell({ borders: cellBorders, width: { size: 2340, type: WidthType.DXA }, shading: altRowShading,
              children: [new Paragraph({ children: [new TextRun({ text: "Scheduling, BFS", size: 20 })] })] })
          ]
        }),
        // Linked List row
        new TableRow({
          children: [
            new TableCell({ borders: cellBorders, width: { size: 2000, type: WidthType.DXA },
              children: [new Paragraph({ children: [new TextRun({ text: "Linked List", bold: true, size: 20 })] })] }),
            new TableCell({ borders: cellBorders, width: { size: 1800, type: WidthType.DXA },
              children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "O(1)*", size: 20, color: "38a169" })] })] }),
            new TableCell({ borders: cellBorders, width: { size: 1800, type: WidthType.DXA },
              children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "O(n)", size: 20, color: "dd6b20" })] })] }),
            new TableCell({ borders: cellBorders, width: { size: 1800, type: WidthType.DXA },
              children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "O(n)", size: 20, color: "dd6b20" })] })] }),
            new TableCell({ borders: cellBorders, width: { size: 2340, type: WidthType.DXA },
              children: [new Paragraph({ children: [new TextRun({ text: "Dynamic data", size: 20 })] })] })
          ]
        })
      ]
    });
  }
  
  // Generate the document
  Packer.toBuffer(doc).then(buffer => {
    fs.writeFileSync("/home/claude/data_structure_learning_tool/output/Data_Structure_Analysis.docx", buffer);
    console.log("Analysis document created successfully!");
  });  