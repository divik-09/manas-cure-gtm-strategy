import pandas as pd
import matplotlib.pyplot as plt
import os

def create_financial_model_csv():
    """Generates a structured market-entry financial growth matrix with integrated charting."""
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
            "2500000", "50000", "4200", "2500", "10500000", "0"
        ],
        "Year 2 (Phased Expansion Run)": [
            "2750000", "150000", "26200", "2500", "65500000", "524.0"
        ],
        "Scenario Framework Pillar": [
            "Total addressable segment", "Access-constrained focal points", "Active acquisition run", "Affordability pricing tier", "Calculated Gross Intake", "Target Milestone Vector"
        ]
    }
    
    df = pd.DataFrame(growth_matrix)
    os.makedirs("financial_model", exist_ok=True)
    df.to_csv("financial_model/financial_scenario_projections.csv", index=False)
    print(" Successfully exported financial model matrix to 'financial_model/financial_scenario_projections.csv'.")

    # --- FINANCIAL CHART GENERATOR ---
    print("Generating strategic growth curve line graph...")
    
    timelines = ['Year 1 Baseline', 'Year 2 Expansion Run']
    subscribers = [4200, 26200] 

    plt.figure(figsize=(8, 4.5))
    plt.plot(timelines, subscribers, marker='o', color='#e67e22', linewidth=3, markersize=8, label='Paying Subscribers')
    
    plt.title('Target Milestone Scale Profile (524% YoY Growth Curve)', fontsize=13, fontweight='bold', pad=12)
    plt.ylabel('Active Premium Subscribers', fontsize=11)
    plt.grid(True, linestyle=':', alpha=0.6)
    
    for i, txt in enumerate(subscribers):
        plt.annotate(f"{txt:,} Users", (timelines[i], subscribers[i]), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig('subscriber_growth_chart.png', dpi=300)
    print(" Successfully saved visual asset as 'subscriber_growth_chart.png'.")

if __name__ == "__main__":
    create_financial_model_csv()