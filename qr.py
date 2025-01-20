import qrcode

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Create a QR code
img = qrcode.make('This is a test QR code!')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as a PNG file
img.save('qrcode.png')