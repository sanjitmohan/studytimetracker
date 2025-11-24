import pathlib
import webbrowser

def open_local_html(html_filename="study_tracker.html"):
    # Get the absolute path to the HTML file
    html_path = pathlib.Path(html_filename).absolute()

    if not html_path.exists():
        print(f"Could not find {html_filename} in this folder.")
        return

    # Convert path to file:// URL and open in default browser
    url = html_path.as_uri()
    print(f"Opening {url}")
    webbrowser.open(url)

if __name__ == "__main__":
    open_local_html("study_tracker.html")  # or "index.html" if you renamed it
