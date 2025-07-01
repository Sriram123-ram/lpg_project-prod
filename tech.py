from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from supabase import create_client, Client
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
from src.controllers.user_controller import router as user_router
app = FastAPI()
app.include_router(user_router)
# templates = Jinja2Templates(directory="templates")

# app.mount("/static", StaticFiles(directory="static"), name="static")
# supabase_url = "https://dmrmooovmshrxfjlmpgg.supabase.co"
# supabase_api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRtcm1vb292bXNocnhmamxtcGdnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk5Njc5MDUsImV4cCI6MjA2NTU0MzkwNX0.3m5dYlHWN8xolLEnWhbAnud0R0QslykMIl-FHsR54XM"

# # Create Supabase client
# database: Client = create_client(supabase_url, supabase_api_key)

# @app.get("/", response_class=HTMLResponse)
# def home(request:Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# @app.get("/all-data")
# def get_all_data():
#     users = database.table('users_table').select("*").execute().data
#     posts = database.table('posts_table').select("*").execute().data
#     tones = database.table('tones_table').select("*").execute().data
#     hashtags = database.table('hashtags').select("*").execute().data
#     preferences = database.table('preferences').select("*").execute().data

#     return {
#         "users_table": users,
#         "posts_table": posts,
#         "tones_table": tones,
#         "hashtags": hashtags,
#         "preferences": preferences
#     }



