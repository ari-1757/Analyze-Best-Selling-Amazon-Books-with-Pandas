# Step 1: Import necessary libraries
import pandas as pd

# Step 2: Load the dataset
df = pd.read_csv("bestsellers.csv")

# Step 3: Exploratory Data Analysis (EDA)
print("First 5 rows of the dataset:\n", df.head(), "\n")
print("Shape of the dataset (rows, columns):", df.shape, "\n")
print("Column names:", df.columns.tolist(), "\n")
print("Summary statistics:\n", df.describe(), "\n")

# Step 4: Data Cleaning and Preprocessing
df.drop_duplicates(inplace=True)  # Remove duplicate rows
df["Price"] = df["Price"].astype(float)  # Ensure 'Price' is in float format

# Rename columns for clarity
df.rename(
    columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"},
    inplace=True,
)

# Step 5: Data Analysis
# Count the number of books per author
author_counts = df["Author"].value_counts()
print("Top authors by book count:\n", author_counts, "\n")

# Calculate average rating by genre
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print("Average rating by genre:\n", avg_rating_by_genre, "\n")

# Step 6: Export Results
author_counts.head(10).to_csv("top_authors.csv", index=True)

print("Top 10 authors saved to 'top_authors.csv'.")
