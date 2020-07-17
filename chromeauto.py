import webbrowser as web

def chromeauto():
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    URLS = (
            "stackoverflow.com",
            "github.com/princep2727",
            "youtube.com",
            "google.com",
            "gmail.com"
    )
    for url in URLS:
        print("opening:"+ url)
        web.get(chrome_path).open(url)

chromeauto()