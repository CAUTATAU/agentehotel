from app.aws.dynamo_client import get_dynamodb_client
from app.config.config import AVAILABILITY_TABLE
from app.config.config import BOOKING_TABLE
import uuid


class BookingAdapter:
    def __init__(self):
        self.dynamodb = get_dynamodb_client()
        self.availability_table = AVAILABILITY_TABLE
        self.booking_table = BOOKING_TABLE

    """def format_date(self, date_str: str) -> str:
        if "/" in date_str:
            year, month, day = date_str.split("/")
            return f"{day}-{month}-{year}"
        return date_str"""

    def check_availability(self, date: str) -> dict:
        #formatted_date = self.format_date(date)
        response = self.dynamodb.get_item(
            TableName=self.availability_table,
            Key={"date": {"S": date}}
        )
        item = response.get('Item')
        return {
            "date": item['date']['S'],
            "seaView": item['seaView']['N'],
            "gardenView": item['gardenView']['N']
        }
    

    def create_booking(self, date: str, name: str, room_type: str, number_of_nights: int) -> dict:
        room_field = "seaView" if room_type == "seaView" else "gardenView"
        booking_id = str(uuid.uuid4())
        try:
            #Atualizar quantidade de reservas disponiveis
            self.dynamodb.update_item(
                TableName=self.availability_table,
                Key={"date": {"S": date}},
                UpdateExpression=f"SET {room_field} = {room_field} - :one",
                ConditionExpression=f"{room_field} > :zero",
                ExpressionAttributeValues={":one": {"N": "1"}, ":zero": {"N": "0"}}
            )
            #Criar a reserva
            self.dynamodb.put_item(
                TableName=self.booking_table,
                Item={
                    "bookingId": {"S": booking_id},
                    "date": {"S": date},
                    "name": {"S": name},
                    "roomType": {"S": room_type},
                    "numberOfNights": {"N": str(number_of_nights)}
                }
            )
            return {
                "success": True,
                "bookingId": booking_id,
                "message": f"Reserva criada com sucesso para {name} em {date} no quarto {room_type} por {number_of_nights} noites."
            }
        except Exception as e:
            if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
                return {
                    "success": False,
                    "message": f"Nenhum quarto {room_type} disponível para a data {date}."
                }
            raise