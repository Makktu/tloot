from textual.app import App
from textual.widgets import Static, Label


class HelloApp(App):
    CSS_PATH = "stopwatch.tcss"

    def compose(self):
        yield Static("[bold lightgreen]Welcome, adventurer.")


if __name__ == "__main__":
    app = HelloApp()
    app.run()