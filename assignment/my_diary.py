entries = []
# password = input("enter your password: ")


def create_entry():
    date, title = input("date: "), input("title: ")

    key = ["date", "title", "body"]
    value = [date, title, input(f"{date}\n {title}\n\nDear diary,\n")]
    entry = dict(zip(key, value))
    return entry


def diary(passwords):

    if passwords == "code":
        to_continue = input("'y' to continue and 'n' to stop [y / n]").lower()

        while to_continue == 'y':
            entries.append(create_entry())
            to_continue = input("'y' to continue and 'n' to stop [y / n]").lower()
        return entries

    print(diary())
