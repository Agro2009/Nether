import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('PREFIX', '!')

# Congress Settings
CONGRESS_SETTINGS = {
    'senate_seats': 100,
    'house_seats': 435,
    'parties': ['Republican', 'Democratic', 'Independent'],
    'term_length_days': 2190,  # Roughly 6 years for senators
}

# Election Settings
ELECTION_SETTINGS = {
    'voting_duration_minutes': 5,
    'minimum_voters': 3,
    'enable_campaigns': True,
}