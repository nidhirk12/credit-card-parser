import re

def parse_amex(text):
    data = {}

    name = re.search(r"Cardmember Name\s*([A-Z\s]+)", text)
    if name:
        data["cardholder_name"] = name.group(1).strip()

    card = re.search(r"Account Ending\s*(\d{4})", text)
    if card:
        data["card_last_4"] = card.group(1)

    statement_date = re.search(r"Statement Closing Date\s*(\w+\s\d{1,2},\s\d{4})", text)
    if statement_date:
        data["statement_date"] = statement_date.group(1)

    payment_due = re.search(r"Payment Due Date\s*(\w+\s\d{1,2},\s\d{4})", text)
    if payment_due:
        data["payment_due_date"] = payment_due.group(1)

    total = re.search(r"New Balance\s*\$([\d,]+\.\d{2})", text)
    if total:
        data["total_amount_due"] = total.group(1)

    minimum = re.search(r"Minimum Payment Due\s*\$([\d,]+\.\d{2})", text)
    if minimum:
        data["minimum_amount_due"] = minimum.group(1)

    return data
