#!/usr/bin/env python
import os
import warnings

from datetime import datetime

from financial_researcher.crew import FinancialResearcher

os.makedirs('output', exist_ok=True)

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'company' : 'Asian Paints'
    }
    
    # Create and run the crew
    result = FinancialResearcher().crew().kickoff(inputs=inputs)
    
    # print the result
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)
    
    print("\n\nReport has been saved to output/report.md")

if __name__ == "__main__":
    run()