# thread to run code in the background
import threading
import time

from DataFetcherManager import DataFetcherManager


class DataPoller:
    # 5 minutes
    def __init__(self, interval=300):
        self.fetcher = DataFetcherManager()
        self.interval = interval
        self.running = False

    def start(self):
        self.running = True

        def loop():
            # run while the app is running
            #paused for 5 minutes between 2 calls
            while self.running:
                try:
                    self.fetcher.fetch_all()  # Refresh system data
                except Exception as e:
                    print(f"Error polling data: {e}")
                time.sleep(self.interval)

        # run the loop
        threading.Thread(target=loop, daemon=True).start()

    def stop(self):
        self.running = False
