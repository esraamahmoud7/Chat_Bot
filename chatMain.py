# guided_chatbot_console.py
import Constants
import Sys_Data
from Constants import OrgTOKEN, SeekerTOKEN
from DataFetcherManager import DataFetcherManager
from DataPoller import DataPoller
from chatBot import ChatFlowManager
import threading
import time

def run_console_chat():
    # user_token = input("Enter you Token ").strip()
    # Constants.TOKEN = user_token
    user_id = "user1"

    # start the chat
    flow = ChatFlowManager(data=Sys_Data.Data,token=Constants.OrgTOKEN)
    # TOKEN is the user id
    flow.reset(Constants.OrgTOKEN)


    print("Bot: Hello! Welcome to HireNy assistant.\n")

    # First prompt only once
    # to print the options
    prompt = flow.get_prompt(user_id)

    while True:
        # Print current prompt
        print(f"Bot: {prompt['message']}")
        # print the options
        for i, option in enumerate(prompt['options'], start=1):
            if option == 'Available Services' and flow.TOKEN != OrgTOKEN:
                continue
            if option == 'Explore courses' and flow.TOKEN != SeekerTOKEN:
                continue
            print(f"  {i}. {option}")
        print()

        # User input
        user_input = input("You: ").strip()

        # exist state
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\nBot: Goodbye! ")
            break

        # Convert numeric input to an actual option
        if user_input.isdigit():
            # the option list start from 0
            idx = int(user_input) - 1
            # ensure that user entered the right choice range
            if 0 <= idx < len(prompt['options']):
                # what the user chose from the menu
                user_input = prompt['options'][idx]
            else:
                print("Invalid option number. Try again.\n")
                continue

        # Get a response and use it as the next prompt
        prompt = flow.handle_input(user_id, user_input)


if __name__ == "__main__":
    try:
        # Initial fetch (synchronous, blocks until data is loaded)
        manager = DataFetcherManager()
        manager.fetch_all()  # Ensure services, jobs, courses etc. are preloaded

        # Start chatbot
        run_console_chat()
        poller = DataPoller()


        # Delay poller start AFTER chatbot begins (e.g., 5 minutes = 300 seconds)
        def delayed_start():
            time.sleep(300)  # 5 minutes
            poller.start()

        threading.Thread(target=delayed_start, daemon=True).start()

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
