from dotenv import load_dotenv
load_dotenv()
from app.aws.adapters.booking_adapter import BookingAdapter
adapter = BookingAdapter()

print(adapter.create_booking("2026-01-25", "John Doe", "seaView", 3))