import sys
from factories import get_factory
from client import LoginForm

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <theme>")
        print("Available themes: 'light', 'dark'")
        sys.exit(1)

    theme = sys.argv[1]
    try:
        factory = get_factory(theme)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    form = LoginForm(factory)
    form.render()
    form.simulate_interaction()

if __name__ == "__main__":
    main()
    