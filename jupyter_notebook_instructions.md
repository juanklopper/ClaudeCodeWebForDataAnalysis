---
name: "Jupyter notebook"
description: "Instructions for adding content to a Jupyter notebook"
---

# Notebook Instructions

- Start all notebooks with the Python code `%config InlineBackend.figure_format = 'retina'` to enable high DPI plotting.
- Use a clear and descriptive title for the notebook. Ask me for the title is required.
- Use markdown section cells to organize the notebook into sections.
- Import all necessary libraries at the beginning of the notebook.
- Use code cells for executable code.
    - Ensure that the code is well-commented and easy to understand.
    - Do not create excessively long code cells.
    - Break code cells into shorter, manageable chunks.
    - Do not use `print` statements to comment on the results of code. Rather use text and LaTeX in markdown cells after each code cell is executed to explain and interpret the code output.
- Use markdown cells with text and LaTeX for results, interpretations, explanations, comments, and documentation. For instance if the code cell contained the code `df.Data.mean()` and the result is 42, use a markdown cell to write: The sample mean $\bar{X}=42$ beats per minute.
- Use consistent formatting throughout the notebook for a professional appearance.