import tabula

# Read PDF file and extract tables
tables = tabula.read_pdf("./test.pdf", pages="all")

# Save tables as CSV files
for i, table in enumerate(tables):
    table.to_csv(f"test_result.csv", index=False)
    
# Convert tables to pandas dataframes
dfs = [table for table in tables]