import requests
import json
import argparse


class Webhook:
    """
        replace url/data with your webhook url/data 
    """

    def __init__(self, url):
        self.webhook_url = url
        self.embed = {
            "description": "Just testing out this webhook",
            "title": "donkurayami",
        }
        self.data = {
            "YEA": "MAN",
            "donkurayami": "online",
            "Testing": "webhook",
            "embeds": [
                self.embed
            ],
        }

    """
        sends webhook request to your service
    """

    def send_webhook(self):
        request = requests.post(self.webhook_url, json=self.data)
        request.raise_for_status()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='Your webhook url')
    args = parser.parse_args()
    discord_webhook = Webhook(args.url)
    discord_webhook.send_webhook()
