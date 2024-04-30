models = []


def up():
    for model in models:
        print(f'🛠️\tCreating a table for {model.table_name}...')
        model.up()

    print('✅\tMigration is complete', end='\n\n')


def down():
    for model in reversed(models):
        print(f'🗑️\tDeleting a table with {model.table_name}...')
        model.down()

    print('✅\tRollback is complete', end='\n\n')


def reset():
    down()
    up()


def playground(function):
    def playground_function_wrapper(*args, **kwargs):
        reset()
        function(*args, **kwargs)
        down()

    return playground_function_wrapper
