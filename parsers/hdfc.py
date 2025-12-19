import re

def parse_hdfc(text):
    data = {}

    name = re.search(r"Name\s*-\s*:\s*([A-Z\s]+?)\s+Statement", text)
    if name:
        data["cardholder_name"] = name.group(1).strip()

    card = re.search(r"Card No\s*:\s*\d{4}\s*55XX\s*XXXX\s*(\d{4})", text)
    if card:
        data["card_last_4"] = card.group(1)

    statement_date = re.search(r"Statement Date\s*:\s*(\d{2}/\d{2}/\d{4})", text)
    if statement_date:
        data["statement_date"] = statement_date.group(1)

    payment_due = re.search(r"letter to\s*(\d{2}/\d{2}/\d{4})", text)
    if payment_due:
        data["payment_due_date"] = payment_due.group(1)

    amounts = re.search(r"(\d{1,3},\d{3}\.\d{2})\s+(\d{1,3},\d{3}\.\d{2})", text)
    if amounts:
        data["total_amount_due"] = amounts.group(1)
        data["minimum_amount_due"] = amounts.group(2)

    return data
