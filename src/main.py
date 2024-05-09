from config import init_gemini
from ui import menu_options
from models import chat_model


model = init_gemini()

chat = model.start_chat(history=[])

options = menu_options()

match options:
    case "1":
        chat_model(chat)
