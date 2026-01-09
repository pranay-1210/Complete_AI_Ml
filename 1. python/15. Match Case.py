color = input("Enter a color: ")

match color:
    case "red":
        print("Stop.")
    case "green":
        print("Go.")
    case _:            # Default Case
        print("Wait.")