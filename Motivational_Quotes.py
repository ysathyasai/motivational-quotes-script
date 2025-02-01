import os  # Import the os module for interacting with the operating system
import random  # Import the random module for generating random numbers
import requests  # Import the requests module for making HTTP requests
import json  # Import the json module for working with JSON data
import time  # Import the time module for time-related functions
import sys  # Import the sys module for interacting with the Python interpreter
from colorama import Fore, Style, init  # Import colorama for colored text output
import re  # Import re for regex operations

# Set the environment variable for UTF-8 encoding
os.environ["PYTHONIOENCODING"] = "utf-8"

# Initialize colorama for colored text
init(autoreset=True)

# Define folder and file paths
HOME = os.path.expanduser("~")  # Get the user's home directory
COMPUTER_FOLDER = os.path.join(HOME, "The_Computer")  # Define the path for "The_Computer" folder
TERMINAL_FOLDER = os.path.join(COMPUTER_FOLDER, "Terminal")  # Define the path for "Terminal" folder
SCRIPT_PATH = os.path.join(TERMINAL_FOLDER, "Motivational_Quotes.py")  # Path for the script
QUOTES_FILE = os.path.join(TERMINAL_FOLDER, "Quotes.txt")  # Path for the quotes file
CACHE_FILE = os.path.join(TERMINAL_FOLDER, "quotes_cache.json")  # Path for the cache file
GITIGNORE_FILE = os.path.join(TERMINAL_FOLDER, ".gitignore")  # Path for the .gitignore file
SETUP_FILE = os.path.join(TERMINAL_FOLDER, "setup.json")  # Path for the setup file

# Detect the shell configuration file based on the operating system
if os.name == 'nt':
    SHELL_CONFIG_PATH = os.path.join(HOME, "_shell_setup.cmd")  # Path for a custom setup file on Windows
elif 'TERMUX_VERSION' in os.environ:
    if os.path.exists(os.path.join(HOME, ".zshrc")):
        SHELL_CONFIG_PATH = os.path.join(HOME, ".zshrc")  # Path for the .zshrc file in Termux
    else:
        SHELL_CONFIG_PATH = os.path.join(HOME, ".bashrc")  # Path for the .bashrc file in Termux
elif os.name == "posix" and "Darwin" in os.uname().sysname:
    SHELL_CONFIG_PATH = os.path.join(HOME, ".zshrc")  # Path for the .zshrc file on macOS
else:
    SHELL_CONFIG_PATH = os.path.join(HOME, ".bashrc")  # Path for the .bashrc file on Linux

# Ensure folders exist and move necessary files if not already present
os.makedirs(TERMINAL_FOLDER, exist_ok=True)  # Create the "Terminal" folder if it doesn't exist

def move_file(src, dst):
    """
    Move a file from src to dst if it exists at src and does not exist at dst.
    """
    if os.path.exists(src) and not os.path.exists(dst):  # Check if the source file exists and destination doesn't
        import shutil  # Import shutil for file operations
        shutil.move(src, dst)  # Move the file

# Move the script, quotes, cache, and .gitignore files to the appropriate directory
move_file(sys.argv[0], SCRIPT_PATH)
move_file("Quotes.txt", QUOTES_FILE)
move_file("quotes_cache.json", CACHE_FILE)
move_file(".gitignore", GITIGNORE_FILE)

# Default quotes (used if Quotes.txt is missing)
DEFAULT_QUOTES = [
    "Code is like humor. When you have to explain it, it’s bad. — Cory House",
    "Talk is cheap. Show me the code. — Linus Torvalds",
    "The best way to predict the future is to create it. — Alan Kay",
    "First, solve the problem. Then, write the code. — John Johnson",
    "Work hard in silence. Let success make the noise.",
    "If debugging is the process of removing bugs, then programming must be the process of putting them in. — Edsger Dijkstra",
    "A good programmer is someone who always looks both ways before crossing a one-way street. — Doug Linder",
    "You might not think that programmers are artists, but programming is an extremely creative profession. — John Romero",
    "Discipline is choosing between what you want now and what you want most. — Abraham Lincoln",
    "Perseverance, secret of all triumphs. — Victor Hugo",
    "Programming isn't about what you know; it's about what you can figure out. — Chris Pine",
    "Coding is today's language of creativity. Every child deserves to be fluent in it. — Reshma Saujani",
    "Opportunities don't happen. You create them. — Chris Grosser",
    "Hard work beats talent when talent doesn’t work hard. — Tim Notke",
    "Stay hungry, stay foolish. — Steve Jobs",
    "Failure is simply the opportunity to begin again, this time more intelligently. — Henry Ford",
    "All progress takes place outside the comfort zone. — Michael John Bobak",
    "Strive for progress, not perfection.",
    "Consistency is what transforms average into excellence.",
    "Code more, worry less!",
    "Great coders are not born. They are self-made through consistent effort.",
    "The only way to learn a new programming language is by writing programs in it. — Dennis Ritchie",
    "The problem is not the problem. The problem is your attitude about the problem. — Captain Jack Sparrow",
    "If you think math is hard, try programming. — Unknown",
    "Don't watch the clock; do what it does. Keep going. — Sam Levenson",
    "The road to success and the road to failure are almost exactly the same. — Colin R. Davis",
    "Success is the sum of small efforts, repeated day in and day out. — Robert Collier",
    "The harder I work, the luckier I get. — Gary Player",
    "Nothing worth having comes easy. — Theodore Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill",
    "The difference between who you are and who you want to be is what you do. — Unknown",
    "The secret of getting ahead is getting started. — Mark Twain",
    "Don't be afraid to give up the good to go for the great. — John D. Rockefeller",
    "Success is walking from failure to failure with no loss of enthusiasm. — Winston Churchill",
    "Keep going. Everything you need will come to you at the perfect time. — Unknown",
]

def initialize_quotes_file():
    """
    Ensure Quotes.txt exists. If not, create it with default quotes.
    """
    if not os.path.exists(QUOTES_FILE):  # Check if the quotes file exists
        with open(QUOTES_FILE, "w", encoding="utf-8") as file:  # Open the file in write mode
            file.write("\n".join(DEFAULT_QUOTES) + "\n")  # Write the default quotes to the file

def load_quotes():
    """
    Load quotes from Quotes.txt. If missing, use built-in quotes.
    """
    initialize_quotes_file()  # Ensure the quotes file exists
    try:
        with open(QUOTES_FILE, "r", encoding="utf-8") as file:  # Open the quotes file in read mode
            return [line.strip() for line in file.readlines() if line.strip()] or DEFAULT_QUOTES  # Read the quotes and return them
    except Exception as e:
        print(f"{Fore.RED}⚠️ Error loading quotes: {e}")  # Print an error message if reading fails
        return DEFAULT_QUOTES  # Return the default quotes if an error occurs

def fetch_quote_from_web():
    """
    Fetch a random motivational quote from the web.
    """
    url = "https://zenquotes.io/api/random"  # URL for fetching a random quote
    try:
        response = requests.get(url)  # Make a GET request to the URL
        if response.status_code == 200:  # Check if the request was successful
            quote_data = response.json()  # Parse the JSON response
            return f"{quote_data[0]['q']} — {quote_data[0]['a']}"  # Format and return the quote
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}⚠️ Error fetching web quote: {e}")  # Print an error message if the request fails
    return None  # Return None if fetching the quote fails

def load_cache():
    """
    Load the cached quotes from the file.
    """
    if os.path.exists(CACHE_FILE):  # Check if the cache file exists
        with open(CACHE_FILE, "r", encoding="utf-8") as file:  # Open the cache file in read mode
            cache_data = json.load(file)  # Load the JSON data from the file
            if time.time() - cache_data["timestamp"] < 86400:  # Check if the cache is still valid (24 hours)
                return cache_data["quotes"]  # Return the cached quotes
    return None  # Return None if the cache is not valid or doesn't exist

def save_cache(quotes):
    """
    Save the quotes to the cache.
    """
    with open(CACHE_FILE, "w", encoding="utf-8") as file:  # Open the cache file in write mode
        json.dump({"timestamp": time.time(), "quotes": quotes}, file)  # Save the quotes with a timestamp

def get_quote():
    """
    Get a random motivational quote (either from file or cached/web).
    """
    cached_quotes = load_cache()  # Load the cached quotes
    if cached_quotes:  # If cached quotes exist
        return random.choice(cached_quotes)  # Return a random cached quote
    else:
        web_quote = fetch_quote_from_web()  # Fetch a quote from the web
        if web_quote:  # If a web quote was fetched successfully
            return web_quote  # Return the web quote
        else:
            quotes = load_quotes()  # Load quotes from the file
            save_cache(quotes)  # Cache the loaded quotes
            return random.choice(quotes)  # Return a random quote from the file

def remove_ansi_codes(text):
    """
    Remove ANSI escape codes from the text.
    """
    ansi_escape = re.compile(
        r'\x1B[@-_][0-?]*[ -/]*[@-~]'
    )
    return ansi_escape.sub('', text)

def type_effect(text, delay=0.03):
    """
    Display text with a typewriter effect.
    """
    clean_text = remove_ansi_codes(text)  # Remove ANSI escape codes from the text
    for char in clean_text:  # Iterate through each character in the text
        sys.stdout.write(char)  # Write the character to stdout
        sys.stdout.flush()  # Flush the stdout buffer
        time.sleep(delay)  # Sleep for a short delay
    sys.stdout.flush()  # Ensure all characters are written to stdout

def display_quote():
    """
    Display a quote.
    """
    print(Fore.YELLOW + "\n💡 Work Motivation 💡\n" + Style.RESET_ALL)  # Print the header
    type_effect(Fore.BLUE + get_quote() + Style.RESET_ALL + "\n")  # Display the quote with a typewriter effect in blue
    print("\n")

def show_help():
    """
    Display the help menu.
    """
    print(Fore.GREEN + "\n📖 Motivational Quotes - Help Menu 📖\n" + Style.RESET_ALL)  # Print the help menu header
    print(Fore.YELLOW + "💡 Every time you open a new terminal, a motivational quote is displayed.\n" + Style.RESET_ALL)  # Explain the main functionality
    print(Fore.CYAN + "👉 **Commands:**" + Style.RESET_ALL)  # Print the commands header
    print(Fore.CYAN + "   - `motivate`, `motivational`, `q`, `quote` → Show a new quote manually." + Style.RESET_ALL)  # Explain the command to show a new quote
    print(Fore.CYAN + "   - `Help_quote` → Show this help menu." + Style.RESET_ALL)  # Explain the command to show the help menu
    print(Fore.CYAN + "   - `addtoquotes(\"your quote here\")` → Add a new quote to Quotes.txt." + Style.RESET_ALL)  # Explain the command to add a new quote
    print(Fore.YELLOW + "\n⚡ All quotes are stored in: ~/The_Computer/Terminal/Quotes.txt\n" + Style.RESET_ALL)  # Print the location of the quotes file

def add_quote(quote):
    """
    Add a new quote to Quotes.txt.
    """
    initialize_quotes_file()  # Ensure the quotes file exists
    escaped_quote = quote.replace('"', '\\"')  # Escape double quotes in the quote
    with open(QUOTES_FILE, "a", encoding="utf-8") as file:  # Open the quotes file in append mode
        file.write(escaped_quote.strip() + "\n")  # Write the new quote to the file
    print("\n✅ Quote added successfully!\n")  # Print a success message

def add_to_shell_config():
    """
    Ensure this script runs automatically when a new terminal opens and handles commands.
    """
    shell_config_entry = f'\n# Run motivation script\npython3 "{SCRIPT_PATH}" display_quote\n'
    function_definitions = f'''
# Functions to handle commands for Motivational Quotes
function motivate() {{ python3 "{SCRIPT_PATH}" display_quote; }}
function motivational() {{ python3 "{SCRIPT_PATH}" display_quote; }}
function q() {{ python3 "{SCRIPT_PATH}" display_quote; }}
function quote() {{ python3 "{SCRIPT_PATH}" display_quote; }}
function Help_quote() {{ python3 "{SCRIPT_PATH}" show_help; }}
function addtoquotes() {{ python3 "{SCRIPT_PATH}" add_quote "$1"; }}
'''
    with open(SHELL_CONFIG_PATH, "r+", encoding="utf-8") as shell_config:
        content = shell_config.read()
        if shell_config_entry not in content:
            shell_config.write(shell_config_entry)
            shell_config.write(function_definitions)

def check_if_setup_done():
    """
    Check if the user has completed the setup before displaying the help menu.
    """
    if not os.path.exists(SETUP_FILE):  # Check if the setup file exists
        show_help()  # Show the help menu
        with open(SETUP_FILE, "w", encoding="utf-8") as f:  # Open the setup file in write mode
            json.dump({"help_shown": True}, f)  # Write to the setup file to mark setup as done

# Main program logic
if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == "display_quote":  # Check if no arguments or "display_quote" is passed
        display_quote()  # Display a quote
    elif sys.argv[1] == "show_help":  # Check if "show_help" is passed
        show_help()  # Show the help menu
    elif sys.argv[1] == "add_quote" and len(sys.argv) > 2:  # Check if "add_quote" is passed with a quote
        add_quote(sys.argv[2])  # Add the new quote
    else:
        print(f"{Fore.RED}⚠️ Unknown command or missing arguments." + Style.RESET_ALL)  # Print an error message

    # Ensure the script is added to the shell configuration file
    add_to_shell_config()
    check_if_setup_done()