while True:
        print("Options: [a]User Path [b]Main Path: ")
        choice = str(input("Choices :"))

        if choice == 'a':
                import userprovider
                break

        elif choice == 'b':
            import main
            break

        else:
            print("Invalid Input! ")