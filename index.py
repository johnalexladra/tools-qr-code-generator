import qrcode

# Prompt user for data
data = input("Enter the data to encode in the QR code: ")

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controls the error correction used for the QR Code
    box_size=10,  # Controls how many pixels each box of the QR code is
    border=4,  # Controls how many boxes thick the border should be
)

# Add data to the QR code object
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'")
