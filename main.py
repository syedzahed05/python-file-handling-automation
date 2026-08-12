# Python File Management & Automation System
# Alfido Tech - Python Developer Internship
# Task 1: File Handling & Automation


def write_txt_file():
    """Create and write data to a TXT file."""

    try:
        with open("input/students.txt", "w") as file:
            file.write("Name: Zahed\n")
            file.write("Course: B.Tech\n")
            file.write("Branch: EEE\n")

        print("\nTXT file created and data written successfully.")

    except Exception as error:
        print(f"\nError while writing the TXT file: {error}")


def read_txt_file():
    """Read and display data from a TXT file."""

    try:
        with open("input/students.txt", "r") as file:
            data = file.read()

        print("\nStudent Information:")
        print(data)

    except FileNotFoundError:
        print("\nError: TXT file not found.")
    except Exception as error:
        print(f"\nError while reading the TXT file: {error}")


def append_txt_file():
    """Append additional data to the TXT file."""

    try:
        with open("input/students.txt", "a") as file:
            file.write("Internship: Alfido Tech\n")

        print("\nData appended to TXT file successfully.")

    except FileNotFoundError:
        print("\nError: TXT file not found.")
    except Exception as error:
        print(f"\nError while appending to the TXT file: {error}")


def create_csv_file():
    """Create a CSV file and write student records."""

    import csv

    try:
        with open("input/students.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["Name", "Age", "Course"])
            writer.writerow(["Zahed", "21", "B.Tech"])
            writer.writerow(["Afroz", "21", "B.Tech"])

        print("\nCSV file created successfully.")

    except Exception as error:
        print(f"\nError while creating CSV file: {error}")


def read_csv_file():
    """Read and display student records from the CSV file."""

    import csv

    try:
        with open("input/students.csv", "r", newline="") as file:
            reader = csv.reader(file)

            print("\nStudent Records:")

            for row in reader:
                print(" | ".join(row))

    except FileNotFoundError:
        print("\nError: CSV file not found.")
    except Exception as error:
        print(f"\nError while reading CSV file: {error}")
def rename_file():
    """Rename the students TXT file."""

    import os

    try:
        old_name = "input/students.txt"
        new_name = "input/student_records.txt"

        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            print("\nTXT file renamed successfully.")
        else:
            print("\nError: File to rename was not found.")

    except Exception as error:
        print(f"\nError while renaming file: {error}")


def move_file():
    """Move the renamed TXT file to the managed_files folder."""

    import os
    import shutil

    try:
        source = "input/student_records.txt"
        destination = "managed_files/student_records.txt"

        if os.path.exists(source):
            shutil.move(source, destination)
            print("\nTXT file moved successfully.")
        else:
            print("\nError: File to move was not found.")

    except Exception as error:
        print(f"\nError while moving file: {error}")


def delete_file():
    """Delete the TXT file from the managed_files folder."""

    import os

    try:
        file_path = "managed_files/student_records.txt"

        if os.path.exists(file_path):
            os.remove(file_path)
            print("\nTXT file deleted successfully.")
        else:
            print("\nError: File to delete was not found.")

    except Exception as error:
        print(f"\nError while deleting file: {error}")
def main():
    while True:
        print("\n" + "=" * 45)
        print("   PYTHON FILE MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1. Write TXT file")
        print("2. Read TXT file")
        print("3. Append TXT file")
        print("4. Create CSV file")
        print("5. Read CSV file")
        print("6. Rename TXT file")
        print("7. Move TXT file")
        print("8. Delete TXT file")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            write_txt_file()

        elif choice == "2":
            read_txt_file()

        elif choice == "3":
            append_txt_file()

        elif choice == "4":
            create_csv_file()

        elif choice == "5":
            read_csv_file()

        elif choice == "6":
            rename_file()

        elif choice == "7":
            move_file()

        elif choice == "8":
            delete_file()

        elif choice == "9":
            print("\nThank you for using the system.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()