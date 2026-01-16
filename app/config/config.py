import os
from dotenv import load_dotenv
load_dotenv()
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")


KNOWLEDGE_BASE_ID = os.getenv("KNOWLEDGE_BASE_ID")

AVAILABILITY_TABLE = os.getenv("AVAILABILITY_TABLE", "hotelRoomAvailabilityTable")
BOOKING_TABLE = os.getenv("BOOKING_TABLE", "HotelBookings")
