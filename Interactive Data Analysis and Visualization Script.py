import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data(file_path):
    try:
        # Load the data into a Pandas DataFrame
        df = pd.read_csv(file_path)

        # Display the original data
        print("Original Data:")
        print(df)

        # Data Cleaning Steps
        # Example: Removing rows with missing values
        df = df.dropna()

        # Example: Removing duplicates
        df = df.drop_duplicates()

        # Example: Convert date columns to datetime format
        df['Date'] = pd.to_datetime(df['Date'])

        # Additional cleaning steps can be added based on your specific dataset

        # Display the cleaned data
        print("\nCleaned Data:")
        print(df)

        # Save the cleaned data to a new CSV file
        cleaned_file_path = 'cleaned_data.csv'
        df.to_csv(cleaned_file_path, index=False)
        print(f"\nCleaned data saved to '{cleaned_file_path}'.")

        return df
    except Exception as e:
        print(f"Error: {e}")
        return None

def plot_data(df, plot_type):
    try:
        # Choose the type of plot based on user input
        if plot_type == 'line':
            sns.lineplot(x='Date', y='Value', data=df)
            plt.title('Line Plot')
        elif plot_type == 'bar':
            sns.barplot(x='Date', y='Value', data=df)
            plt.title('Bar Plot')
        elif plot_type == 'scatter':
            sns.scatterplot(x='Date', y='Value', data=df)
            plt.title('Scatter Plot')
        elif plot_type == 'box':
            sns.boxplot(x='Date', y='Value', data=df)
            plt.title('Boxplot')
        elif plot_type == 'hist':
            sns.histplot(df['Value'], bins=10, kde=True)
            plt.title('Histogram')
        else:
            print(f"Invalid plot type: {plot_type}")
            return

        # Show the plot
        plt.show()
    except Exception as e:
        print(f"Error plotting data: {e}")

if __name__ == "__main__":
    # Get the file path from the user
    data_file_path = input("Enter the file path: ")

    # Load and clean the data
    cleaned_data = load_and_clean_data(data_file_path)

    # If data cleaning is successful, allow the user to plot graphs until they choose to exit
    if cleaned_data is not None:
        while True:
            plot_type = input("Enter the type of plot (line/bar/scatter/box/hist), or type 'exit' to quit: ").lower()

            if plot_type == 'exit':
                print("Exiting the program.")
                break

            plot_data(cleaned_data, plot_type)