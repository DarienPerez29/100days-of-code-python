def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "No valid values"
    return f"{f_name} {l_name}".title()

if __name__ == "__main__":
    print(format_name("", "PÉREZ"))