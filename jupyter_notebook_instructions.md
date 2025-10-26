---
applyTo: "notebook"
---
# Notebook Instructions

- Install required Python packages.
- Run the code cells sequentially from top to bottom as they are created using the Python kernel.
- Use markdown cells to organize the notebook into sections.
- Use a clear and descriptive title for the notebook in the first markdown cell, for example `# <TITLE>`. Ask me for the value of <TITLE> if required.
- Add a markdown cell immediately after the title cell using the markdown section `## Import packages` and add all required Python packages in this section
- Insert a code cell at the end of the section on importing packages and enter the code  `%config InlineBackend.figure_format = 'retina'` to enable high DPI plotting.
- The next section must be `## Data import and cleaning` where you import and clean the data.
- Follow this with a section `## Data analysis and visualization` where you perform the main analysis and visualization.
- End the notebook with a section `## Conclusions` where you summarize the main findings.
- Use code cells for executable code.
- Ensure that the code is well-commented and easy to understand.
  - Do not create excessively long code cells.
  - Break code cells into shorter, manageable chunks.
- Do not use `print` statements to comment on the results of code. Rather use text and LaTeX in markdown cells after each code cell is executed to explain and interpret the code output.
- Use markdown cells with text and LaTeX for results, interpretations, explanations, comments, and documentation. For instance if the code cell contained the code `df.Data.mean()` and the result is 42, use a markdown cell to write: The sample mean $\bar{X}=42$ beats per minute.
- Use consistent formatting throughout the notebook for a professional appearance.