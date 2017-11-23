# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
from apple import Apple

def cli():
    try:
        apple = Apple()
        apple.run_cli()
    except (EOFError, KeyboardInterrupt):
        pass
        # haxor.cli.set_return_value(None)


if __name__ == "__main__":
    cli()