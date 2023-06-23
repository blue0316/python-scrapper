import camelot

# Set the file path of the PDF document
pdf_path = "./test.pdf"

# Set the output file path for the CSV file
csv_path = "./test_result.csv"

# Extract the tables from the PDF using Camelot
# You can set the flavor to "stream" for tables with no clear boundaries or "lattice" for tables with clear boundaries
tables = camelot.read_pdf(pdf_path, flavor="stream", pages="all")

# Loop through each table and save it as a CSV file
for i, table in enumerate(tables):
    table.to_csv(f"{csv_path}_{i}.csv")