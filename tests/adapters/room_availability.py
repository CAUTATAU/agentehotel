from dotenv import load_dotenv
load_dotenv()
from app.aws.adapters.booking_adapter import BookingAdapter

adapter = BookingAdapter()

print(adapter.check_availability("2026-01-26"))