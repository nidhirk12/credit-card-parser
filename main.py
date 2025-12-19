from parsers.hdfc import parse_hdfc
from parsers.icici import parse_icici
from parsers.sbi import parse_sbi
from parsers.axis import parse_axis
from parsers.amex import parse_amex


from pdf2image import convert_from_path
import pytesseract

# tell python where tesseract is
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_scanned_pdf(pdf_path):
    text = ""
    images = convert_from_path(
        pdf_path,
        poppler_path=r"C:\poppler-25.12.0\Library\bin"
    )
    for img in images:
        text += pytesseract.image_to_string(img)
    return text

def detect_issuer(text):
    text_upper = text.upper()

    if "HDFC" in text_upper:
        return "HDFC"
    elif "ICICI" in text_upper:
        return "ICICI"
    elif "STATE BANK OF INDIA" in text_upper or "SBI" in text_upper:
        return "SBI"
    elif "AXIS" in text_upper:
        return "AXIS"
    elif "AMERICAN EXPRESS" in text_upper or "AMEX" in text_upper:
        return "AMEX"
    else:
        return "UNKNOWN"


text = extract_text_from_scanned_pdf("statement.pdf")
print("TEXT LENGTH:", len(text))
print(text[:2000])

issuer = detect_issuer(text)
print("\nDetected Issuer:", issuer)

print("\n--- PARSED DATA ---")

if issuer == "HDFC":
    parsed = parse_hdfc(text)
elif issuer == "ICICI":
    parsed = parse_icici(text)
elif issuer == "SBI":
    parsed = parse_sbi(text)
elif issuer == "AXIS":
    parsed = parse_axis(text)
elif issuer == "AMEX":
    parsed = parse_amex(text)
else:
    parsed = {}

if not parsed:
    print("No parser available for this statement.")
else:
    for k, v in parsed.items():
        print(f"{k}: {v}")

