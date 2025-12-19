import re

def parse_sbi(text):
    data = {}

    name = re.search(r"Name\s*:\s*([A-Z\s]+)", text)
    if name:
        data["cardholder_name"] = name.group(1).strip()

    card = re.search(r"XXXX\s*XXXX\s*XXXX\s*(\d{4})", text)
    if card:
        data["card_last_4"] = card.group(1)

    statement_date = re.search(r"Statement Date\s*:\s*(\d{2}/\d{2}/\d{4})", text)
    if statement_date:
        data["statement_date"] = statement_date.group(1)

    payment_due = re.search(r"Payment Due Date\s*:\s*(\d{2}/\d{2}/\d{4})", text)
    if payment_due:
        data["payment_due_date"] = payment_due.group(1)

    total = re.search(r"Total Amount Due\s*₹?\s*([\d,]+\.\d{2})", text)
    if total:
        data["total_amount_due"] = total.group(1)

    minimum = re.search(r"Minimum Amount Due\s*₹?\s*([\d,]+\.\d{2})", text)
    if minimum:
        data["minimum_amount_due"] = minimum.group(1)

    return data
