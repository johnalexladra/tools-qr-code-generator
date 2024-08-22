import qrcode
import os

def get_data():
    file_path = 'data.txt'
    
    # Check if the file exists and read from it
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            data = file.read().strip()
        if data:
            return data
    
    # If file doesn't exist or is empty, prompt user for input
    print("File 'data.txt' not found or is empty.")
    data = input("Enter the data to encode in the QR code: ")
    return data

# Get the data for the QR code
data = get_data()

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
