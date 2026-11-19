from textual.app import App
from textual.widgets import Static, Label, Footer, Digits

class HelloApp(App):
    CSS_PATH = "styled.tcss"
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self):
        yield Static("This is one thing")
        yield Static("This is using an id", id="static_id")
        yield Static("First class", classes="static_class1")
        yield Static("Second class", classes="static_class2")
        yield Digits(1234)
        yield Footer()


    def on_key(self, event):
        match event.key:
            case "escape":
                self.exit()

    # remember: uv run textual run --dev main.py

if __name__ == "__main__":
    app = HelloApp()
    app.run()