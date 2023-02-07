def main():
    print("Welcome to email splitter")
    user_email = input("Please enter your email address: ")

    (username, domain) = user_email.split("@")
    (domain, extension) = domain.split(".")

    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"Extension: {extension}")


main()