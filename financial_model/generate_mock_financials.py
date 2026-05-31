import pandas as pd
import os

def create_financial_model_csv():
    """Generates a structured market-entry financial growth matrix."""
    growth_matrix = {
        "Metric Category": [
            "Target Patient Universe (TAM)", 
            "Serviceable Obtainable Market (SOM)", 
            "Paying Subscriber Base", 
            "Blended ARPU (INR/Year)",
            "Gross Projected Revenue (INR)", 
            "YoY Growth Rate %"
        ],
        "Year 1 (Baseline Verification)": [
            "2,500,000", "50,000", "4,200", "2,500", "1,05,00,000", "N/A"
        ],
        "Year 2 (Phased Expansion Run)": [
            "2,750,000", "1,50,000", "26,200", "2,500", "6,55,0,000", "524.0%"
        ],
        "Scenario Framework Pillar": [
            "Total addressable segment", "Access-constrained focal points", "Active acquisition run", "Affordability pricing tier", "Calculated Gross Intake", "Target Milestone Vector"
        ]
    }
    
    df = pd.DataFrame(growth_matrix)
    os.makedirs("financial_model", exist_ok=True)
    df.to_csv("financial_model/financial_scenario_projections.csv", index=False)
    print(" Successfully exported financial model matrix to 'financial_model/financial_scenario_projections.csv'.")

if __name__ == "__main__":
    create_financial_model_csv()