# Ref: https://archive.ics.uci.edu/api/datasets/list
# Ref: https://archive.ics.uci.edu/api/dataset?id=45
# Prereq: pip install requests, pip install ucimlrepo
# from ucimlrepo import list_available_datasets
# # check which datasets can be imported
# list_available_datasets()

import requests

# Function to dynamically fetch and save datasets
def fetch_and_save_dataset(data_id, base_url, save_directory):
    """
    Fetches a dataset from the given data ID and saves it to a specified directory.

    :param data_id: The dataset ID from the UCI ML repository.
    :param base_url: Base URL of the UCI ML repository.
    :param save_directory: Local directory to save the downloaded dataset.
    """
    # Construct the URL dynamically using the data_id
    url = f"{base_url}{data_id}/data.csv"

    # Construct the local file path dynamically
    local_file_path = f"{save_directory}/data{data_id}_UCI.csv"

    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Write the content to a local file
        with open(local_file_path, "wb") as file:
            file.write(response.content)

        print(f"File saved successfully to {local_file_path}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# Parameters
base_url = "https://archive.ics.uci.edu/static/public/"
save_directory = "/Users/z5601757/Documents/AriaResearch/Project/Generative AI based Health Management Application/data"

# Change this to the dataset ID you want to fetch
data_id = 145  # Example: Statlog (Heart)

# Fetch and save the dataset
fetch_and_save_dataset(data_id, base_url, save_directory)
