# Manage Recruitment - Python Program

## Overview
Manage Recruitment is a simple command-line application designed to assist recruiters in managing candidate information efficiently. The program provides essential features such as viewing, adding, updating, and deleting candidates, as well as managing recruitment budgets.

## Features
- **View Candidate 👀**: Displays a summary of all candidates and allows users to view details of a selected candidate.
- **Add Candidate ➕**: Adds a new candidate to the system while checking for duplicate entries.
- **Update Candidate 💫**: Updates details of an existing candidate.
- **Delete Candidate 🧹**: Removes a candidate from the system after confirmation.
- **Budget Manager 💰**: Helps in managing recruitment budgets.
- **Exit Program 👋**: Closes the application with a farewell message.

## Prerequisites
Before running the program, ensure you have the following installed:
- **Python 3.x**
- **Required Libraries:** Install dependencies using the command below:

  ```bash
  pip install pyfiglet tabulate
  ```

## How to Run
To execute the program, run the following command in the terminal:

```bash
python main.py
```

## Usage
1. When the program starts, it displays a welcome message.
2. Choose an option from the main menu by entering a number (1-6).
3. Follow the on-screen prompts to perform actions related to candidates or budget management.
4. Exit the program using option **6**.

## Code Sneak Peek
```python
# Main menu
def main():
    welcome_message = pyfiglet.figlet_format("Manage Recruitment")
    print(welcome_message)

    while True:
        menu_options = [
            ["1", "View Candidate 👀 "],
            ["2", "Add Candidate ➕ "],
            ["3", "Update Candidate 💫 "],
            ["4", "Delete Candidate 🧹 "],
            ["5", "Budget Manager 💰 "],
            ["6", "Exit Program 👋 "]
        ]
        print(tabulate(menu_options, headers=["Option", "Description"], colalign=['center', 'left'], tablefmt="rounded_grid"))

        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            view_candidate_details(candidates)
        elif choice == "2":
            create_candidate(candidates, budget_data)  # Pass budget_data here
        elif choice == "3":
            update_candidate(candidates)
        elif choice == "4":
            delete_candidate(candidates)
        elif choice == "5":
            budget_manager(budget_data)
        elif choice == "6":
            print("\n")
            big_message = pyfiglet.figlet_format("Goodbye!")
            print(big_message)
            break
        else:
            print(" ❌ Invalid option. Please try again.")

# Call the main function
main()
```

## Contribution
If you'd like to contribute, feel free to submit a pull request or suggest improvements.

## License
This project is open-source and free to use under the MIT License.

