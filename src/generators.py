trs = [ {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "RUB",
                  "code": "RUB"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }]

def filter_by_currency(transactions: list[dict], currency: str):
        for transaction in transactions:
            t_cur = transaction["operationAmount"]["currency"]["name"]
            if t_cur == currency:
                yield transaction


# print(*filter_by_currency(trs, "RUB"))
# print(*filter_by_currency(trs, "USD"))


def transaction_descriptions(transactions: list[dict]):
    result = []
    for transaction in transactions:
        desc = transaction["description"]
        yield desc
#print(*transaction_descriptions(trs))



def card_number_generator(start: int, end: int) -> str:
    for number in range(start, end + 1):
        e = str(number).zfill(16)
        yield f'{e[:4]} {e[4:8]} {e[8:12]} {e[12:]}'


for card_number in card_number_generator(3, 40):
    print(card_number)


