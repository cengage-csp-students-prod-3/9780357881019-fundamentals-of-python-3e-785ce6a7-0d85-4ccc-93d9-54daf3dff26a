import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Load CSV file (replace 'breadprice.csv' with your filename)
    df = pd.read_csv('breadprice.csv')

    # Display raw data (optional)
    print(df.head())

    # Clean data: Convert monthly columns to numeric, coerce errors to NaN
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    for month in months:
        df[month] = pd.to_numeric(df[month], errors='coerce')

    # Fill missing values (NaN) with the row mean or drop them
    df[months] = df[months].fillna(df[months].mean(axis=1))

    # Calculate yearly average price
    df['Yearly Average'] = df[months].mean(axis=1)

    # Plot year vs average price
    plt.figure(figsize=(10,5))
    plt.plot(df['Year'], df['Yearly Average'], marker='o', linestyle='-')
    plt.title('Average Price of Bread by Year')
    plt.xlabel('Year')
    plt.ylabel('Average Price ($)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
