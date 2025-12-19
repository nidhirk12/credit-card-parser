# Credit Card Statement Parser

## Overview
This project parses real-world credit card statement PDFs and extracts key billing information.
It is designed to support multiple credit card issuers using a modular and extensible architecture.
The solution works on scanned PDF statements by applying OCR and rule-based text parsing.

## Supported Issuers
- HDFC Bank 
- ICICI Bank
- SBI Card
- Axis Bank
- American Express

## Extracted Fields
- Card Last 4 Digits
- Statement Date
- Payment Due Date
- Total Amount Due
- Minimum Amount Due

## Project Structure
credit-card-parser/
├── main.py
├── statement.pdf
├── README.md
└── parsers/
  ├── base.py
  ├── hdfc.py
  ├── icici.py
  ├── sbi.py
  ├── axis.py
  └── amex.py

## Approach
1. Convert scanned PDF pages to images using `pdf2image` and Poppler
2. Extract text from images using Tesseract OCR
3. Detect the card issuer from extracted text
4. Apply issuer-specific regex-based parsing logic
5. Output structured key-value data
The design allows new issuers to be added easily by creating a new parser file without changing the core logic.

## Technologies Used
- Python
- Tesseract OCR
- pdf2image
- Regular Expressions

## Sample Output
Detected Issuer: HDFC

card_last_4: 3388
statement_date: 23/10/2024
payment_due_date: 12/11/2024
total_amount_due: 83,794.00
minimum_amount_due: 4,240.00





