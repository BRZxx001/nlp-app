import json


class Database:
    # ==========================================================
    # --- ADD USER DATA TO DATABASE ---
    # ==========================================================
    def add_data(self, name, email, password):
        """
        Add a new user (name, email, password) to db.json.
        Returns:
            1 -> Successfully added
            0 -> Email already exists
        """

        # Read existing data from JSON file
        with open('db.json', 'r') as rf:
            database = json.load(rf)

        # Check if email already exists
        if email in database:
            return 0
        else:
            # Add new user data
            database[email] = [name, password]

            # Write updated data back to file
            with open('db.json', 'w') as wf:
                json.dump(database, wf, indent=4)

            return 1

    # ==========================================================
    # --- SEARCH USER (LOGIN VALIDATION) ---
    # ==========================================================
    def search(self, email, password):
        """
        Verify user credentials from db.json.
        Returns:
            1 -> Email and Password match
            0 -> Incorrect credentials or email not found
        """

        # Read data from JSON file
        with open('db.json', 'r') as rf:
            database = json.load(rf)

        # Validate credentials
        if email in database:
            if database[email][1] == password:
                return 1
            else:
                return 0
        else:
            return 0
