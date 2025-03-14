def load_emails() -> dict[str, str]:
    emails = {}
    try:
        with open("mail_input.txt", "r") as file:
            for line in file:
                # print(line)
                temp_list = line.strip().replace(" ", "").split(",")
                # print(temp_list)
                print(type(temp_list))
                emails[temp_list[0]] = temp_list[1]
    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return emails

def process_emails(emails: dict[str, str]) -> set[str]:
    return set(emails.values())

if __name__ == "__main__":
    emails = load_emails()
    print(f" Available emails: {str(emails)}")
    students = process_emails(emails)
    print(f" Available emails: {str(students)}")
