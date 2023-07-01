import pandas as pd

# Load the flight delay data into a pandas DataFrame
flight_data = pd.read_csv('flight_delay_data.csv')  # Replace 'flight_delay_data.csv' with the actual file path or API call

# Convert the 'date' column to a datetime object
flight_data['date'] = pd.to_datetime(flight_data['date'])

# Prompt the user to enter a specific day
user_input = input("Enter the date (YYYY-MM-DD): ")
selected_date = pd.to_datetime(user_input)

# Filter the data for the selected date
selected_data = flight_data[flight_data['date'].dt.date == selected_date.date()]

# Group the data by location and count the delays
delay_counts = selected_data['location'].value_counts()

# Get the location with the most delays
most_delayed_location = delay_counts.idxmax()
most_delayed_count = delay_counts.max()

# Print the result
print(f"On {selected_date.date()}, the location with the most delays was {most_delayed_location} with {most_delayed_count} delays.")
