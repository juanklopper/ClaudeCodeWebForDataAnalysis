# Quick Start Guide

Get up and running with data analysis in 5 minutes!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Run Your First Analysis

Navigate to the scripts directory and run the data loading script:

```bash
cd scripts
python 01_data_loading.py
```

This will load and display basic information about the datasets.

## Step 3: Try Data Visualization

```bash
python 04_visualization.py
```

This creates several plots in the `outputs/` directory. Check them out!

## Step 4: Explore the Jupyter Notebook

```bash
cd ../notebooks
jupyter notebook data_analysis_tutorial.ipynb
```

This opens an interactive notebook where you can run all analyses step by step.

## Step 5: Try Machine Learning

```bash
cd ../examples
python ml_prediction_example.py
```

This trains models to predict customer purchase frequency.

## What's Next?

- Modify the scripts to analyze your own data
- Experiment with different visualization styles
- Try additional statistical tests
- Build more sophisticated ML models
- Ask Claude Code to help you extend the analysis!

## Common Issues

**Issue:** Module not found error  
**Solution:** Make sure you've installed all requirements: `pip install -r requirements.txt`

**Issue:** No outputs directory  
**Solution:** The scripts create it automatically, but you can manually create it: `mkdir outputs`

**Issue:** Data files not found  
**Solution:** Make sure you're running scripts from the correct directory. Check the relative paths in the scripts.

## Need Help?

- Check the main README.md for detailed documentation
- Review the code comments for explanations
- Open an issue in the repository
- Ask Claude Code for assistance!

---

Happy analyzing! 🎉
