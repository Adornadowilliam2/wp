import qrcode

# Data to encode
data = "https://github.com/Adornadowilliam2?tab=repositories"

# Create an instance of QRCode class
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Thickness of the border
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save("qrcode.png")

# Optionally, show the image
img.show()
