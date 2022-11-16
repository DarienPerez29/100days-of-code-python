def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "No valid values"
    return f"{f_name} {l_name}".title()

if __name__ == "__main__":
    print(format_name("", "PÉREZ"))