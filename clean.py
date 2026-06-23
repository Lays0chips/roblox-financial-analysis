import pandas as pd
from pathlib import Path

base = Path(__file__).parent / "Dataset"

income_statement_25 = pd.read_excel(base / "Q12025.xls", sheet_name="INCOME_STATEMENT", header=16)

income_statement_25 = income_statement_25.drop(columns=["Unnamed: 0"])
income_statement_25.columns = ["Item", "Q1_2025", "Q1_2024"]
income_statement_25 = income_statement_25.dropna(how="all")

data_25 = (
    income_statement_25
    .dropna(subset=["Q1_2025", "Q1_2024"], how="all")
)
data_25.loc[20, "Item"] = "Weighted-average shares outstanding"

income_statement_26 = pd.read_excel(base / "Q12026.xls", sheet_name="INCOME_STATEMENT", header=17)

income_statement_26 = income_statement_26.drop(columns=["Unnamed: 0"])
income_statement_26.columns = ["Item", "Q1_2026", "Q1_2025"]
income_statement_26 = income_statement_26.dropna(how="any")



non_dollar = [18, 20]
mask = ~income_statement_26.index.isin(non_dollar)
income_statement_26.loc[mask, ["Q1_2026", "Q1_2025"]] *= 1000
income_statement_26.loc[20, "Item"] = "Weighted-average shares outstanding"


data_25 = data_25.reset_index(drop=True)
income_statement_26 = income_statement_26.reset_index(drop=True)

print(data_25.to_string())
print(income_statement_26.to_string())