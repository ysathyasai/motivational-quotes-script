# Motivational Quotes Script

This project is a Python script that displays a motivational quote each time a new terminal session opens. It also provides functionality to manually show quotes, add new quotes, and view a help menu. The script is integrated into the `.bashrc` file to ensure it runs automatically and allows for custom commands.

## Features

- **Automatic Quote Display**: Displays a motivational quote each time a new terminal session opens.
- **Manual Quote Display**: Commands to manually display a quote.
- **Add New Quotes**: Functionality to add new quotes to the list.
- **Help Menu**: A help menu that provides information on available commands.
- **Web Quote Fetching**: Fetches a random motivational quote from a web API.
- **Quote Caching**: Caches quotes to reduce the number of API requests.
- **Colorful Output**: Uses `colorama` to display colorful text in the terminal.

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library
- `colorama` library

You can install the required libraries using pip:

```sh
pip install requests colorama
```
## Installation

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/ysathyasai/motivational-quotes-script.git
    ```

2. **Navigate to the Directory**:

    ```sh
    cd motivational-quotes-script
    ```

3. After getting into the directory, install the requirements from the `requirements.txt`:

    ```sh
    pip install -r requirements.txt
    ```

4. **Move the Script and Necessary Files**:

    The script automatically moves itself and other necessary files to `~/The_Computer/Terminal` directory. Ensure you have `Quotes.txt`, `quotes_cache.json`, and `.gitignore` in the same directory as the script initially.

5. **Run the Script**:

    Run the script once to set up everything:

    ```sh
    python3 Motivational_Quotes.py
    ```

6. After executing the program, to delete the `motivational-quotes-script` folder:

    ```sh
    rm -rf motivational-quotes-script
    ```


### .bashrc Integration

The script updates your `.bashrc` file to run itself each time a new terminal session opens and to add custom commands. The following functions are added to `.bashrc`:

- `motivate`
- `motivational`
- `q`
- `quote`
- `Help_quote`
- `addtoquotes`

### Usage

#### Displaying a Quote

The script automatically displays a quote each time a new terminal session opens. You can also manually display a quote using the following commands:

```sh
motivate
motivation
q
quote
```
#### Adding a New Quote

To add a new quote, use the `addtoquotes` command followed by the quote in quotes:

```sh
addtoquotes "Your new motivational quote here."
```
#### Viewing the Help Menu

To view the help menu, use the `Help_quote` command:

```sh
Help_quote
```
## Main Functions

- **`initialize_quotes_file()`**: Ensures the `Quotes.txt` file exists. If not, it creates the file with a set of default quotes.
- **`load_quotes()`**: Loads quotes from the `Quotes.txt` file. If the file is missing, it uses the default quotes.
- **`fetch_quote_from_web()`**: Fetches a random motivational quote from a web API.
- **`load_cache()`**: Loads the cached quotes from the `quotes_cache.json` file.
- **`save_cache()`**: Saves quotes to the cache with a timestamp.
- **`get_quote()`**: Gets a random motivational quote, either from the cache, the web, or the `Quotes.txt` file.
- **`type_effect()`**: Displays text with a typewriter effect.
- **`display_quote()`**: Displays a motivational quote.
- **`show_help()`**: Displays the help menu with information on available commands.
- **`add_quote()`**: Adds a new quote to the `Quotes.txt` file.
- **`add_to_bashrc()`**: Adds the script and custom functions to the `.bashrc` file to ensure the script runs automatically and allows for custom commands.
- **`check_if_setup_done()`**: Checks if the setup has been completed by looking for the `setup.json` file. If not, it shows the help menu and creates the `setup.json` file.

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.

## Contributions

Any improvements, contributions, or ideas are always welcome! Feel free to open an issue or submit a pull request. For any questions or inquiries, please contact [ysathyasai.dev@gmail.com](mailto:ysathyasai.dev@gmail.com).
