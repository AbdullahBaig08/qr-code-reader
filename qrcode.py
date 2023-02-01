import cv2
from pyzbar import pyzbar

# Read the image file
image = cv2.imread("qr_code.jpg")

# Detect the QR code in the image
barcodes = pyzbar.decode(image)

# Iterate over the detected barcodes
for barcode in barcodes:
    # Extract the QR code data as a string
    qr_code_data = barcode.data.decode("utf-8")

    # Print the QR code data
    print("QR Code data:", qr_code_data)
