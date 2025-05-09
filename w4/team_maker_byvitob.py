import random

def create_teams():
    input_type = input("\nDo you want to enter names or numbers? ")

    team_size = int(input("Members in a team: "))

    team_qty = int(input("Total team: "))

    if input_type.lower()[1] == "a":
        # ask names
        names = input("Enter all the names: ").strip().title()
        names = names.split(" ")
    else:
        # ask for a range of numbers
        start, end = map(
            int, input("Enter the range of numbers (start, end): ").split(",")
        )
        names = list(map(str, range(start, end + 1)))
    print("\n")
    # shuffle
    random.shuffle(names)

    # create!
    teams = [names[i : i + team_size] for i in range(0, len(names), team_size)]

    # if there are more teams than specified, distribute the extra members to the first few teams
    if len(teams) > team_qty:
        extra_teams = teams[team_qty:]
        teams = teams[:team_qty]

        # flatten the extra_teams list
        extra_members = [member for team in extra_teams for member in team]

        # distribute the extra members across the teams
        for i, member in enumerate(extra_members):
            teams[i % len(teams)].append(member)

    for i, team in enumerate(teams, 1):
        print(f'Team {i}: {", ".join(team)}')

create_teams()
print("\n")
