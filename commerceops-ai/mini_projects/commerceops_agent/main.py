from agent import process_message


def main():

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        print(
            "CommerceOps AI:",
            process_message(user_input)
        )


if __name__ == "__main__":
    main()