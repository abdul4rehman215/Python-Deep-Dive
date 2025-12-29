import requests
import json
import argparse
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def fetch_data(api_url):
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error occurred: {req_err}")
    except ValueError:
        logging.error("Invalid JSON response")
    return None

def save_data_to_file(data, file_path):
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        logging.info(f"Data successfully saved to {file_path}")
    except Exception as e:
        logging.error(f"Error saving data: {e}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="CLI Data Processor")
    parser.add_argument("--api_url", required=True, help="API URL to fetch JSON data")
    parser.add_argument("--file_path", required=True, help="Output file path")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    logging.info("Starting CLI Data Processor")

    data = fetch_data(args.api_url)

    if data:
        save_data_to_file(data, args.file_path)
    else:
        logging.error("No data fetched. Exiting.")
