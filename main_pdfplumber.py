import pdfplumber

# Open PDF file
with pdfplumber.open("input.pdf") as pdf:
    # Extract tables from all pages
    tables = []
    for page in pdf.pages:
        table = page.extract_table()
        tables.append(table)

# Convert tables to pandas dataframes
dfs = [pd.DataFrame(table[1:], columns=table[0]) for table in tables]
