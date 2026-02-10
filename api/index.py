from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.form.get('data', '')
    
    if not data:
        return render_template('index.html', error='Please enter some text')
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to base64 for embedding in HTML
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    
    return render_template('index.html', qr_code=img_base64, input_data=data)

if __name__ == '__main__':
    import os
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')
