# Webpage Monitor with Page Fetch API

This Python script uses the Page Fetch API to monitor a webpage for changes. It's perfect for tracking updates on a news website, changes in the content of a blog post, or any modifications on a webpage that doesn't provide an API for accessing its content.

## Prerequisites

To run this script, you need the following:

- Python 3.6 or higher
- A RapidAPI account
- Your RapidAPI key and host for the Page Fetch API

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/DaddyApi/website-change-monitoring.git
    ```
2. Navigate to the cloned directory:
    ```
    cd website-change-monitoring
    ```
3. Install the required Python modules:
    ```
    pip install requests
    ```

## Usage

1. Open `monitor.py` in your favorite text editor.
2. Replace `<your-api-host>` and `<your-api-key>` with your RapidAPI host and key for the Page Fetch API.
3. Replace `https://example.com` with the URL of the webpage you want to monitor.
4. Save your changes and close the text editor.
5. Run the script:
    ```
    python monitor.py
    ```

## How it Works

The script fetches the webpage content every 60 seconds and compares the SHA256 hash of the content with the hash of the previously fetched content. If the hashes don't match, the script prints a message indicating that a change was detected.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.
