import re
from datetime import datetime

def is_valid_destination(destination):
    """Validates that the destination contains only letters and spaces."""
    return bool(re.match(r'^[A-Za-z ]+$', destination))

def has_overlap(itineraries, start_date, end_date):
    """Checks if a new itinerary overlaps with existing ones."""
    for it in itineraries:
        if it['start_date'] <= end_date and it['end_date'] >= start_date:
            return True
    return False
