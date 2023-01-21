import backend


USER_OPTIONS = """
What do you wanna do?
type: r -> retreive password:
type: c -> create password:
type: d -> delete password:

OPTION: """


option = input(USER_OPTIONS).lower()

if option == 'c':
    backend.create()
elif option == 'r':
    print(backend.retreive())
elif option == 'd':
    print(backend.delete())

