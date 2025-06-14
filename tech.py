from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/",response_class=HTMLResponse)
def home():
    return """
      <!DOCTYPE html>
        <html>

        <head>
            <title>𝐋𝐈𝐍𝐊𝐄𝐃𝐈𝐍 𝐏𝐎𝐒𝐓 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐎𝐑</title>
        </head>

        <body>
            <h2>Welcome To 𝐋𝐈𝐍𝐊𝐄𝐃𝐈𝐍 𝐏𝐎𝐒𝐓 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐎𝐑</h2>
            <p>
                Generate Your digital posts in just 5 mins!
            </p>
        </body>

        </html>
    """