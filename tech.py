from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from supabase import create_client, Client
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Supabase credentials
supabase_url = "https://dmrmooovmshrxfjlmpgg.supabase.co"
supabase_api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRtcm1vb292bXNocnhmamxtcGdnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk5Njc5MDUsImV4cCI6MjA2NTU0MzkwNX0.3m5dYlHWN8xolLEnWhbAnud0R0QslykMIl-FHsR54XM"

# Create Supabase client
database: Client = create_client(supabase_url, supabase_api_key)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
<html>
 
<head>
    <title>LinkedIn Post Generator</title>
</head>
 
<body>
    <h2>LinkedIn Post Generator</h2>
    <p>
        Default code has been
        loaded into the Editor.
    </p>
</body>
</html>
"""

@app.get("/all-data")
def get_all_data():
    users = database.table('users_table').select("*").execute().data
    posts = database.table('posts_table').select("*").execute().data
    tones = database.table('tones_table').select("*").execute().data
    hashtags = database.table('hashtags').select("*").execute().data
    preferences = database.table('preferences').select("*").execute().data

    return {
        "users_table": users,
        "posts_table": posts,
        "tones_table": tones,
        "hashtags": hashtags,
        "preferences": preferences
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
