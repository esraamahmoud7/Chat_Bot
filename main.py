from dotenv import load_dotenv
from Constants import API_KEY, OrgTOKEN,SeekerTOKEN
from DataFetcherManager import DataFetcherManager
from DataPoller import DataPoller
from GeminiChatbot import GeminiChatbot
from TextFormatter import TextFormatter
import threading
import time

load_dotenv()

def run_chat():
    print("Bot: Hello! How can I help you today on the HireNy platform?\n")


    bot = GeminiChatbot(api_key=API_KEY, Token=SeekerTOKEN)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye!")
            break

        try:
            reply = bot.get_response(user_input)
            formatted = TextFormatter.clean(reply)
            print("Bot:", formatted)
        except Exception as e:
            print(" Error:", e)


if __name__ == "__main__":
    try:
        # Initial fetch (synchronous, blocks until data is loaded)
        manager = DataFetcherManager()
        manager.fetch_all()  # Ensure services, jobs, courses etc. are preloaded


        # Start chat
        run_chat()

        poller = DataPoller()


        # Delay poller start AFTER chatbot begins (e.g., 5 minutes = 300 seconds)
        def delayed_start():
            time.sleep(300)  # 5 minutes
            poller.start()


        threading.Thread(target=delayed_start, daemon=True).start()
        # fetch the data



    except KeyboardInterrupt:
        # Stop poller gracefully if needed
        try:
            poller.stop()
        except:
            pass

    except Exception as e:
        print(f"Unexpected error: {e}")

    finally:
        print("Goodbye!")
