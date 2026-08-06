text = """
Customers may return products within 30 days.
Refunds are processed in 5 business days.
Shipping fees are non-refundable.
Holiday purchases receive extended returns.
"""

chunks = text.split("\n")

for chunk in chunks:
    print(chunk)

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

size = 5
overlap = 2

chunks = []

for i in range(0, len(text), size - overlap):
    chunks.append(text[i:i+size])

print(chunks)

text = "CommerceOps AI allows employees to work remotely two days per week. Refund requests must be submitted within 30 days. Refunds are processed within five business days. Shipping fees are not refundable."

chunks = text.split(".")

for chunk in chunks:
    print(chunk)

size = 20
overlap = 5

chunks = []

for i in range(0,len(text), size - overlap):
    chunks.append(text[i:i+size])

print(chunks)