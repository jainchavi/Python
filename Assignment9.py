#NAME: CHAVI JAIN
#BATCH: 3
#JECRC UNIVERSITY



import re
import threading

def validate_pass(password):

    valid = True
    errors = []

    if len(password)<8:
        valid = False
        errors.append("Password should be of 8 characters atleast.")

    if not re.search(r'[A-Z]', password):
        valid = False
        errors.append("Password does not contain uppercase letter.")

    if not re.search(r'[a-z]', password):
        valid = False
        errors.append("Password does not contain lowercase letter.")

    if not re.search(r'\d', password):
        valid = False
        errors.append("Password does not contain numbers.")

    if not re.search(r'[!@#$%^&*()\,.?":{}|<>]',password):
        valid = False
        errors.append("Password does not contain special characters.")

    return (valid, errors)

valid_pass = []
invalid_pass = []
results_lock = threading.Lock()

def pass_validator(password):
    try:
        valid,errors = validate_pass(password)

        with results_lock:
            if valid:
                valid_pass.append(password)
                print(f"Valid Password: {password}")

            else:
                error_msg = f"Invalid Password: {password} | Errors: {','.join(errors)}"
                invalid_pass.append(error_msg)
                print(error_msg)


                with open("Invalid_password.log","a") as log_file:
                    log_file.write(f"error_msg")
    
    except Exception as e:
        print(f"Error validationg password '{password}' : {str(e)}")


def main():
    try:
        pass_input = input("Enter passwords:")
        passwords = pass_input.strip().split()

        if not passwords:
            print("No password provided.")
            return
        

        threads = []
        for password in passwords:
            thread = threading.Thread(target = pass_validator, args=(password,))
            threads.append(thread)
            thread.start()


        for thread in threads:
            thread.join()

        try:
            with open("valid_password.txt", "w") as f:
                for password in valid_pass:
                    f.write(f"{password}")
        except Exception as e:
            print("Error saving valid password: {str(e)}")

        print("Password Validation Complete!")

    except Exception as e:
        print(f"Error Occurred: {str(e)}")

if __name__ == "__main__":
    main()