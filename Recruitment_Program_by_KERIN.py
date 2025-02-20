from tabulate import tabulate
import pyfiglet

## Candidate-realted functions
# ADD NEW CANDIDATE
def collect_candidate_data(): #input new candidate
    name = input("\nEnter candidate name: ").title()
    while not name:
        print(" ⚠️ Name cannot be empty.")
        name = input("\nEnter candidate name: ").title()

    phone = input("\nEnter candidate phone number: ")
    while not phone.isdigit():
        print(" ⚠️ Phone number must be numbers.")
        phone = input("\nEnter candidate phone number: ")

    email = input("\nEnter candidate email: ").capitalize()
    while not email:
        print(" ⚠️ Email cannot be empty.")
        email = input("\nEnter candidate email: ").capitalize()

    position = input("\nEnter position applied for: ").title()
    while not position:
        print(" ⚠️ Position cannot be empty.")
        position = input("\nEnter position applied for: ").title()

    level = input("\nEnter position level: ").title()
    while not level:
        print(" ⚠️ Level cannot be empty.")
        level = input("\nEnter position level: ").title()

    salary_expectation = input("\nEnter salary expectation: ")
    while not salary_expectation.isdigit():
        print(" ⚠️ Salary expectation must be a number.")
        salary_expectation = input("\nEnter salary expectation: ")
    salary_expectation=int(salary_expectation)
    salary_expectation=f'Rp. {salary_expectation:,}'

    status = input("\nEnter application status (e.g., Applied, Interviewed, Offered, Rejected): ").capitalize()
    valid_statuses = ["Applied", "Interviewed", "Offered", "Rejected"]
    while status not in valid_statuses:
        print(" ⚠️ Invalid status. Please choose from: (Applied, Interviewed, Offered, Rejected).")
        status = input("\nEnter application status (e.g., Applied, Interviewed, Offered, Rejected): ").capitalize()

    notes = input("\nEnter notes (optional): ").capitalize()

    return {
        "name": name,
        "phone": phone,
        "email": email,
        "position": position,
        "level": level,
        "salary_expectation": salary_expectation,
        "status": status,
        "notes": notes
    }

def check_for_duplicates(candidates, name, position): #check for duplicates

    for candidate in candidates:
        if candidate["name"].title() == name.title() and candidate["position"].title() == position.title():
            print(" ⚠️ Data already exists")
            return True
    return False

def confirm_data(candidate_data): #confirm data input (correct or not)
    candidate_data_list = [[
        candidate_data["name"],
        candidate_data["phone"],
        candidate_data["email"],
        candidate_data["position"],
        candidate_data["level"],
        candidate_data["salary_expectation"],
        candidate_data["status"],
        candidate_data["notes"]
    ]]
    headers = ["Name", "Phone Number", "Email", "Position", "Level", "Salary Expectation", "Status", "Notes"]
    print("\nPlease review the entered data:")
    print(tabulate(candidate_data_list, headers=headers, colalign=['left', 'left', 'left', 'left', 'center', 'center', 'center', 'left'], tablefmt="grid"))

    while True:
        confirmation = input("\nDoes the data you just input already correct? (yes/no): ").strip().lower()
        if confirmation == 'yes':
            return True
        elif confirmation == 'no':
            return False
        else:
            print(" ❌ Invalid input. Please enter 'yes' or 'no'.")

def handle_re_input(candidates, name, position): #confirmation reinput (reinput or not)
    while True:
        retry_choice = input("\nDo you want to re-input the data? (yes/no): ").strip().lower()
        if retry_choice == 'yes':
            print("\nRe-entering candidate information...")
            return True
        elif retry_choice == 'no':
            print("\n❌ Add candidate cancelled. ⬅️ Returning to Add Candidate menu . . .")
            return False
        else:
            print(" ❌ Invalid input. Please enter 'yes' or 'no'.")

def add_new_candidate(candidates): #adding new candidate to the list / append to candidate data
    while True:
        candidate_data = collect_candidate_data()

        # check for duplicates
        if check_for_duplicates(candidates, candidate_data["name"], candidate_data["position"]):
            return False  # stay in the submenu

        # confirm data and add if correct
        if confirm_data(candidate_data):
            candidates.append(candidate_data)
            print(" ✅ Candidate added successfully.")
            return False  # stay in the submenu
        else:
            # ask if want to re-input the data or not
            if not handle_re_input(candidates, candidate_data["name"], candidate_data["position"]):
                return False  # stay in the submenu

def return_to_main_menu(): # return to main menu
    print(" \n ⬅️  Returning to the main menu . . .")
    return True # return to main menu

def create_candidate(candidates, budget_data): #submenu 'add candidate'
    print("Creating candidate...")
    while True:
        print('''
 ========================================    
 |       'Add Candidate' Submenu:       |
 ========================================    
        ''')
        menu_data = [["1", "Add New Candidate"], ["2", "Back to main menu"]]
        print(tabulate(menu_data, headers=["Option", "Action"], colalign=['center','left'], tablefmt="rounded_outline"))
        
        submenu_choice = input("Please choose an option (1 or 2): ").strip()
        
        if submenu_choice == "1":
            # adding a new candidate
            while True:
                candidate_data = collect_candidate_data()

                # Check for duplicates
                if check_for_duplicates(candidates, candidate_data["name"], candidate_data["position"]):
                    return False  # Stay in the submenu if duplicate

                # Confirm data and add if correct
                if confirm_data(candidate_data):
                    # Check if position and level match the budget
                    position_matched = False  # Track if a match is found

                    for budget in budget_data:
                        if (candidate_data["position"].title() == budget["Position"].title() and
                                candidate_data["level"].title() == budget["Level"].title()):
                            position_matched = True

                            try:
                                # Ensure `budget["Budget"]` is converted to an integer if it's a string
                                if isinstance(budget["Budget"], str):
                                    budget_amount = int(budget["Budget"].replace('Rp. ', '').replace(',', ''))
                                else:
                                    budget_amount = budget["Budget"]

                                # Convert candidate salary expectation
                                salary_int = int(candidate_data["salary_expectation"].replace('Rp. ', '').replace(',', ''))

                                # Compare salary with the budget
                                if salary_int > budget_amount:
                                    print(f" ⚠️ Warning: The salary expectation of {candidate_data['salary_expectation']} exceeds the budget of {budget['Budget']} for {candidate_data['position']} position at {candidate_data['level']} level.")
                                else:
                                    print(f" ✅ Salary expectation of {candidate_data['salary_expectation']} is within the budget for {candidate_data['position']} position at {candidate_data['level']} level.")
                                break  # Exit loop after find a match
                            except ValueError:
                                print("Error: Invalid format for budget or salary expectation. Please check the data.")
                                break  # Exit loop krna invalid data

                    # Feedback if no matching position and level found
                    if not position_matched:
                        print(f" ⚠️ No budget found for {candidate_data['position']} position at {candidate_data['level']} level.")

                    # Add the candidate to the list
                    candidates.append(candidate_data)
                    print(f" ✅ Candidate {candidate_data['name']} added successfully.")
                    break  # exit the loop after adding candidate successfully
                else:
                    # ask if they want to re-input the data or exit
                    if not handle_re_input(candidates, candidate_data["name"], candidate_data["position"]):
                        break  # Exit loop and return to the submenu

        elif submenu_choice == "2":
            # Return to the main menu
            print(" \n ⬅️  Returning to the main menu . . .")
            break  # Exit the submenu and return to the main menu

        else:
            print(" ❌ Invalid input. Please enter '1' or '2'.")


# VIEW CANDIDATE
def view_candidate_details(candidates): #submenu for view candidate
    if not candidates:
        print(" ⚠️ No candidates available.")
        return

    while True:
        print('''
 =========================================  
 |        View Candidates' submenu:      |
 ========================================= ''')
        menu_options = [
            ["1", "View all candidates"],
            ["2", "View candidates by position"],
            ["3", "View candidates by status"],
            ["4", "Back to main menu ⬅️ "]
        ]

        print("\n" + tabulate(menu_options, headers=["Option", "Action"], colalign=['center','left'],tablefmt="rounded_outline"))
        choice = input("Please choose an option (1-4): ").strip()

        if choice == "1":
            view_all_candidates(candidates)
        elif choice == "2":
            view_candidates_by_position(candidates)
        elif choice == "3":
            view_candidates_by_status(candidates)
        elif choice == "4":
            print(" \n ⬅️  Returning to the main menu . . .")
            break
        else:
            print(" ❌ Invalid input. Please choose a number (1-4).")

def view_all_candidates(candidates): #view all candidates
    print("\nAll Candidates:")
    display_candidates(candidates)

def view_candidates_by_position(candidates): # to filter candidate based on positions
    position = input("\nEnter the position to filter by: ").title()
    filtered_candidates = []

    # Iterate through each candidate in the list
    for candidate in candidates:
        if candidate["position"].title() == position:  # Compare position directly
            filtered_candidates.append(candidate)  # Add candidate to filtered list

    if filtered_candidates:
        display_candidates(filtered_candidates)
    else:
        print(" ⚠️ No candidates found for the given position.")

def view_candidates_by_status(candidates): # to filter candidate based on status
    status = input("\nEnter the status to filter by (Applied, Interviewed, Offered, Rejected): ").capitalize()
    filtered_candidates = []

    # Iterate through each candidate and access the attributes without dictionary indexing
    for candidate in candidates:
        if "status" in candidate and candidate["status"].capitalize() == status:
            filtered_candidates.append(candidate)

    if filtered_candidates:
        display_candidates(filtered_candidates)
    else:
        print(" ⚠️ No candidates found for the given status.")

def display_candidates(candidates): #to see list of candidates
    headers = ["No", "Name", "Position", "Level", "Status"]
    table_data = []

    # Iterate over the candidates directly
    for i in range(len(candidates)):
        candidate = candidates[i]
        table_data.append([i + 1, candidate["name"], candidate["position"], candidate["level"], candidate["status"]])

    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

    candidate_no = input("\nEnter candidate number to view details or press Enter to return: ")
    if candidate_no.isdigit():
        candidate_no = int(candidate_no)
        if 1 <= candidate_no <= len(candidates):
            display_candidate_details(candidates[candidate_no - 1]) #what we input -1 , untuk match index
        else:
            print(" ❌ Candidate not found.")
    else:
        print(" \n ⬅️  Returning to the main menu . . .")

def display_candidate_details(candidate): #to see the choosen candidates for details
    details = [
        ["Name", candidate["name"]],
        ["Phone Number", candidate["phone"]],
        ["Email", candidate["email"]],
        ["Position", candidate["position"]],
        ["Level", candidate["level"]],
        ["Salary Expectation", candidate["salary_expectation"]],
        ["Status", candidate["status"]],
        ["Notes", candidate["notes"]],
    ]
    print('''\n
    ==================================  
    |        Candidate Details       |
    ================================== ''')
    print(tabulate(details, headers=["Field", "Value"], colalign=['left', 'left'], tablefmt="fancy_grid"))


# UPDATE CANDIDATE
def confirm_data():  #confirm if the data is correct
    while True:
        confirmation = input("\nDoes the data you just input already correct? (yes/no): ").strip().lower()
        if confirmation == 'yes':
            return True
        elif confirmation == 'no':
            return False
        else:
            print(" ❌ Invalid input. Please enter 'yes' or 'no'.")

def handle_re_input():  # ask if want re-input the data
    while True:
        retry_choice = input("\nDo you want to re-input the data? (yes/no): ").strip().lower()
        if retry_choice == 'yes':
            print("\nRe-entering candidate information...")
            return True
        elif retry_choice == 'no':
            print("\n❌ Update cancelled. ⬅️ Returning to Update Candidate menu . . .")
            return False
        else:
            print(" ❌ Invalid input. Please enter 'yes' or 'no'.")

def update_candidate(candidates):  # submenu and display
    # Submenu for the update option
    while True:
        submenu_options = [
            ["1", "Update candidate"],
            ["2", "Back to main menu ⬅️ "]
        ]
        print(''' 
 ===========================================    
 |       'Update Candidate' submenu:       | 
 ===========================================''')
        print(tabulate(submenu_options, headers=["Option", "Action"], colalign=['center', 'left'], tablefmt="rounded_outline"))

        choice = input("Please choose an option (1 or 2): ")

        if choice == '1':
            if not candidates:
                print(" ⚠️ No candidates available to update.")
                continue  # return to the submenu

            # display candidate
            headers = ["No", "Name", "Position", "Status"]
            rows = []
            for i in range(len(candidates)):  # Manual indexing
                candidate = candidates[i]
                rows.append([i + 1, candidate["name"], candidate["position"], candidate["status"]])

            print(''' 
 =================================      
 |        Candidates List        |
 =================================''')
            print(tabulate(rows, headers=headers, colalign=['center', 'left', 'center', 'center'], tablefmt="fancy_grid"))

            while True:
                candidate_no = input("\nEnter the candidate number to update or press Enter to return: ")
                if candidate_no == "": 
                    print(" ⬅️  Returning to the Update Candidate submenu...")
                    break
                try:
                    candidate_no = int(candidate_no)
                    if 1 <= candidate_no <= len(candidates):
                        candidate = candidates[candidate_no - 1]
                        break  
                    else:
                        print(" ❌ Invalid number. Please choose a valid candidate number.")
                except ValueError:
                    print(" ❌ Invalid input. Please enter a valid candidate number or press Enter to return.")

            if candidate_no == "":  
                continue  # Go back submenu

            while True: 
                name = input(f"\nEnter Name [{candidate['name']}]: ") or candidate['name']
                position = input(f"\nEnter Position [{candidate['position']}]: ") or candidate['position']
                level = input(f"\nEnter Level [{candidate['level']}]: ") or candidate['level']

                # Phone number (must be numeric)
                while True:
                    phone = input(f"\nEnter Phone Number [{candidate['phone']}]: ") or candidate['phone']
                    if phone.isdigit():
                        break
                    else:
                        print(" ❌ Phone number must be numbers.")

                email = input(f"\nEnter Email [{candidate['email']}]: ") or candidate['email']

                # salary
                while True:
                    salary_expectation_input = input(f"\nEnter Salary Expectation [{candidate['salary_expectation']}]: ")
                    if salary_expectation_input == "":
                        salary_expectation = candidate['salary_expectation']  # Keep old value
                        break
                    elif salary_expectation_input.isdigit() and int(salary_expectation_input) >= 0:
                        salary_expectation = int(salary_expectation_input)
                        break
                    else:
                        print(" ❌ Salary Expectation must be digits.")

                valid_statuses = ["Applied", "Interviewed", "Offered", "Rejected"]
                while True:
                    status_input = input(f"\nEnter Status [{candidate['status']}]: ") or candidate['status']
                    status = status_input.capitalize()
                    if status in valid_statuses:
                        break  # Exit loop 
                    else:
                        print(" ⚠️ Invalid status. Please choose from: (Applied, Interviewed, Offered, Rejected).")

                notes = input(f"\nEnter Notes [{candidate['notes']}]: ") or candidate['notes']

                # Display
                candidate_data = [
                    ["Name", name],
                    ["Position", position],
                    ["Level", level],
                    ["Phone", phone],
                    ["Email", email],
                    ["Salary Expectation", salary_expectation],
                    ["Status", status],
                    ["Notes", notes]
                ]
                print("\nReview the entered data:")
                print(tabulate(candidate_data, headers=["Field", "Value"], colalign=['left', 'left'], tablefmt="grid"))

                # Ask for confirmation
                if confirm_data(): 
                    candidate["name"] = name
                    candidate["position"] = position
                    candidate["level"] = level
                    candidate["phone"] = phone
                    candidate["email"] = email
                    candidate["salary_expectation"] = salary_expectation
                    candidate["status"] = status
                    candidate["notes"] = notes

                    print(f"✅ Candidate '{name}' has been updated successfully!")
                    break  

                else:  
                    if not handle_re_input(): 
                        break 

        elif choice == '2':  # main menu
            print("\n  ⬅️  Returning to main menu...")
            break  

        else:
            print(" ❌ Invalid input. Please enter '1' or '2'.")


# DELETE CANDIDATE / ALL
def delete_candidate(candidates):
    if not candidates:
        print(" ⚠️ No candidates available to delete.")
        return

    while True:
        submenu_options = [
            ["1", "Delete a specific candidate"],
            ["2", "Delete all candidates"],
            ["3", "Back to main menu ⬅️ "]
        ]
        print('''
 ==============================================  
 |        'Delete Candidates' Submenu:        |
 ==============================================''')
        print(tabulate(submenu_options, headers=["Option", "Action"], colalign=["center", "left"], tablefmt="rounded_outline"))

        choice = input("Please choose an option (1-3): ").strip()

        if choice == "1":  # Deleting a specific candidate
            while True: 
                if not candidates:
                    print(" ⚠️ No candidates available to delete.")
                    break

                headers = ["No", "Name", "Position", "Level", "Status"]
                rows = []
                for index in range(len(candidates)):
                    candidate = candidates[index]
                    rows.append([
                        index + 1,  # Manual numbering
                        candidate["name"],
                        candidate["position"],
                        candidate["level"],
                        candidate["status"]
                    ])

                print('''
 =================================  
 |        Candidates List        |
 =================================  
 ''')
                print(tabulate(rows, headers=headers, colalign=['center', 'left', 'left', 'left', 'center'], tablefmt="fancy_grid"))

                candidate_no_input = input("Enter the candidate number to delete: ")

                if candidate_no_input.isdigit():
                    candidate_no = int(candidate_no_input)
                    if 1 <= candidate_no <= len(candidates):
                        candidate = candidates[candidate_no - 1]

                        details = [
                            ["Name", candidate["name"]],
                            ["Phone Number", candidate["phone"] if "phone" in candidate else "Not available"],
                            ["Email", candidate["email"] if "email" in candidate else "Not available"],
                            ["Position", candidate["position"]],
                            ["Level", candidate["level"]],
                            ["Salary Expectation", candidate["salary_expectation"] if "salary_expectation" in candidate else "Not available"],
                            ["Status", candidate["status"]],
                            ["Notes", candidate["notes"] if "notes" in candidate else "None"],
                        ]
                        print(tabulate(details, headers=["Field", "Value"], colalign=['left', 'left'], tablefmt="fancy_grid"))

                        while True:
                            confirmation = input("\nAre you sure you want to delete this candidate? (yes/no): ").strip().lower()
                            if confirmation == "yes":
                                del candidates[candidate_no - 1]
                                print(" ✅ Candidate deleted successfully.")
                                break
                            elif confirmation == "no":
                                print(" ❌ Deletion cancelled. ⬅️  Returning to delete menu . . .")
                                break
                            else:
                                print(" ❌ Invalid input. Please enter 'yes' or 'no'.")
                        break
                    else:
                        print(" ❌ Invalid number. Please choose a valid candidate number.")
                else:
                    print(" ❌ Invalid input. Please enter a valid candidate number.")

        elif choice == "2":  # Deleting all candidates
            while True:
                if not candidates:
                    print(" ⚠️ No candidates available to delete.")
                    break

                headers = ["No", "Name", "Position", "Level", "Status"]
                rows = []
                for index in range(len(candidates)):
                    candidate = candidates[index]
                    rows.append([
                        index + 1,  # Manual numbering
                        candidate["name"],
                        candidate["position"],
                        candidate["level"],
                        candidate["status"]
                    ])

                print('''
 =================================  
 |        Candidates List        |
 =================================  
 ''')
                print(tabulate(rows, headers=headers, colalign=['center', 'left', 'left', 'left', 'center'], tablefmt="fancy_grid"))

                confirmation = input("Are you sure you want to delete all candidates? (yes/no): ").strip().lower()
                if confirmation == "yes":
                    candidates.clear()
                    print(" ✅ All candidates deleted successfully.")
                    break
                elif confirmation == "no":
                    print(" ❌ Deletion cancelled. ⬅️  Returning to delete menu . . .")
                    break
                else:
                    print(" ❌ Invalid input. Please enter 'yes' or 'no'.")

        elif choice == "3": # Returning 
            print("\n ⬅️ Returning to main menu . . .")
            break

        else:
            print("❌ Invalid input. Please choose a number (1-3). ")  


#Budget-related functions
# ADD BUDGET
def add_budget(budgets):
    while True:  # Budget position
        while True:
            budget_position = input("\nEnter budget position: ").title()
            if not budget_position.isalpha():
                print(" ⚠️ Input is invalid, Please try again.")
            else:
                break

        while True:  # Budget level
            budget_level = input("\nEnter budget level position: ").capitalize()
            if not budget_level.isalpha():
                print(" ⚠️ Input is invalid, Please try again.")
            else:
                break

        while True:  # Budget amount
            the_budget = input("\nEnter the budget: ")
            if not the_budget.isdigit():  # numeric
                if not the_budget:
                    print(" ⚠️ Budget cannot be empty.")
                else:
                    print(" ⚠️ Budget must be digits.")
            else:
                the_budget = int(the_budget)
                the_budget = f'Rp. {the_budget:,}'
                break  # Break after valid input 

        # Display for review
        budget_data = [
            ["Position", budget_position],
            ["Level", budget_level],
            ["Budget", the_budget],
        ]

        print("\nNew data:")
        print(tabulate(budget_data, headers=["Field", "Value"], colalign=['left', 'left'], tablefmt="grid"))

        # append the data
        budgets.append({
            "Position": budget_position,
            "Level": budget_level,
            "Budget": the_budget,
        })
        print(f" ✅ Budget for {budget_position} position and {budget_level} level added successfully.")
        return  # Return to menu


# VIEW BUDGET
def view_budget(budgets):
    if not budgets:
        print(" ⚠️ No budget data available.")
        return

    # function to retrieve for sorting
    def get_position(budget):
        return budget['Position'].title()

    # sorting alphabetically 
    budgets_sorted = sorted(budgets, key=get_position)

    # format rupiah and ','
    for budget in budgets_sorted:
        if isinstance(budget["Budget"], str):  # If Budget is a string, remove 'Rp.' and commas, then reformat
            budget_amount = int(budget["Budget"].replace('Rp. ', '').replace(',', ''))
        else:  # If Budget is already an integer, use it directly
            budget_amount = budget["Budget"]
        
        budget["Budget"] = f'Rp. {budget_amount:,}'  # formatting

    print('''
 ========================         
 |      Budget List     |          
 ========================''')
    print(tabulate(budgets_sorted, headers="keys", tablefmt="rounded_grid", showindex=False))


# DELETE BUDGET
def delete_budget(budgets):
    if not budgets:
        print(" ⚠️ No budget available to delete.")
        return

    print('''
 ========================         
 |      Budget List     |          
 ========================''')
    budget_data = [
        [f"{i + 1}", budgets[i]['Position'], budgets[i]['Level'], budgets[i]['Budget']]
        for i in range(len(budgets))
    ]
    print(tabulate(budget_data, headers=["No.", "Position", "Level", "Budget"], tablefmt="rounded_grid"))

    while True:  # Select budget to delete
        budget_no_input = input("\nEnter the budget number to delete or press Enter to return: ")
        
        if not budget_no_input:  # If Enter is pressed without any input
            print(" ⬅️ Returning to delete budget sub-menu.")
            return  # Exit and return 

        try:
            budget_no = int(budget_no_input)
            if 1 <= budget_no <= len(budgets):
                selected_budget = budgets[budget_no - 1]
                budgets.pop(budget_no - 1)  # Delete the selected budget
                print(f" ✅ Budget for {selected_budget['Position']} position and {selected_budget['Level']} level deleted successfully.")
                break  # Exit loop after deletion
            else:
                print(" ❌ Invalid number. Please choose a valid number.")
        except ValueError:
            print(" ❌ Invalid input. Please enter a valid number.")

# MENU BUDGET
def budget_manager(budgets):
    while True:
        options = [
            ["1", "View Budget"],
            ["2", "Add Budget"],
            ["3", "Delete Budget"],
            ["4", "Back to main menu ⬅️ "],
        ]
        print(''' 
 ======================================  
 |        'Budget Manager' Menu       |
 ======================================
        ''')
        print(tabulate(options, headers=["Option", "Description"], colalign=['center', 'left'], tablefmt="rounded_outline"))

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            view_budget(budgets)
        elif choice == "2":
            add_budget(budgets)
        elif choice == "3":
            delete_budget(budgets)
        elif choice == "4":
            print("Exiting Budget Manager...")
            break
        else:
            print(" ❌ Invalid input. Please select a valid option.")

# Call to main
# Dummy data candidates
# candidates = []
candidates = [
    {
        "name": "Alice Johnson",
        "phone": "088235325523",
        "email": "alice.johnson@example.com",
        "position": "Software Engineer",
        "level": "Staff",
        "salary_expectation": "Rp. 25,000,000",
        "status": "Applied",
        "notes": "Strong coding skills"
    },
    {
        "name": "Bob Smith",
        "phone": "084324315156",
        "email": "bob.smith@example.com",
        "position": "Software Engineer",
        "level": "Supervisor",
        "salary_expectation": "Rp. 15,000,000",
        "status": "Interviewed",
        "notes": "Good team player"
    },
    {
        "name": "Catherine Lee",
        "phone": "08436643432",
        "email": "catherine.lee@example.com",
        "position": "Data Scientist",
        "level": "Staff",
        "salary_expectation": "Rp. 9,500,000",
        "status": "Offered",
        "notes": "Excellent analytical skills"
    },
    {
        "name": "David Kim",
        "phone": "081234567890",
        "email": "david.kim@example.com",
        "position": "Software Engineer",
        "level": "Manager",
        "salary_expectation": "Rp. 30,000,000",
        "status": "Applied",
        "notes": "Leadership experience"
    },
    {
        "name": "Eva White",
        "phone": "083012345678",
        "email": "eva.white@example.com",
        "position": "Sales",
        "level": "Manager",
        "salary_expectation": "Rp. 18,000,000",
        "status": "Interviewed",
        "notes": "Creative and detail-oriented"
    },
    {
        "name": "Frank Black",
        "phone": "082123456789",
        "email": "frank.black@example.com",
        "position": "Data Scientist",
        "level": "Staff",
        "salary_expectation": "Rp. 8,000,000",
        "status": "Rejected",
        "notes": "Experienced in cloud technologies"
    },
    {
        "name": "Grace Chen",
        "phone": "089876543210",
        "email": "grace.chen@example.com",
        "position": "Human Resources",
        "level": "Supervisor",
        "salary_expectation": "Rp. 22,000,000",
        "status": "Applied",
        "notes": "Strong project management skills"
    },
    {
        "name": "Henry Zhang",
        "phone": "085123498765",
        "email": "henry.zhang@example.com",
        "position": "Marketing",
        "level": "Staff",
        "salary_expectation": "Rp. 8,500,000",
        "status": "Rejected",
        "notes": "Quick learner, eager to grow"
    },
    {
        "name": "Ivy Lee",
        "phone": "087654321987",
        "email": "ivy.lee@example.com",
        "position": "Data Scientist",
        "level": "Supervisor",
        "salary_expectation": "Rp. 18,000,000",
        "status": "Offered",
        "notes": "Proficient in machine learning"
    }
]

# Dummy data budgets
# budget_data = []
budget_data = [
    {"Position": "Software Engineer", "Level": "Staff", "Budget": 7000000},
    {"Position": "Software Engineer", "Level": "Supervisor", "Budget": 15000000},
    {"Position": "Software Engineer", "Level": "Manager", "Budget": 22000000},
    {"Position": "Data Scientist", "Level": "Staff", "Budget": 7000000},
    {"Position": "Data Scientist", "Level": "Supervisor", "Budget": 17000000},
    {"Position": "Data Scientist", "Level": "Manager", "Budget": 22000000},
    {"Position": "Human Resources", "Level": "Staff", "Budget": 7500000},
    {"Position": "Human Resources", "Level": "Supervisor", "Budget": 10000000},
    {"Position": "Human Resources", "Level": "Manager", "Budget": 18000000},
    {"Position": "Sales", "Level": "Staff", "Budget": 5000000},
    {"Position": "Sales", "Level": "Supervisor", "Budget": 8500000},
    {"Position": "Sales", "Level": "Manager", "Budget": 9000000},
    {"Position": "Secretary", "Level": "Staff", "Budget": 12000000},
    {"Position": "Marketing", "Level": "Staff", "Budget": 7000000}
]

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
        
        print('''
 =========================
 |       Main Menu       |
 =========================
        ''')
        
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
