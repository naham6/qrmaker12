# QR Code Generator

A simple and elegant QR code generator web application built with Python Flask that can be deployed on Vercel.

## Features

- 🔳 Generate QR codes from any text or URL
- 🎨 Modern, responsive UI with gradient design
- ⚡ Fast and lightweight
- 🚀 Deployed on Vercel

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python api/index.py
```

3. Open your browser and navigate to `http://localhost:5000`

## Deploy to Vercel

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy:
```bash
vercel
```

## Usage

1. Enter any text or URL in the input field
2. Click "Generate QR Code"
3. Your QR code will be displayed instantly
4. Scan the QR code with your mobile device

## Tech Stack

- **Backend**: Python Flask
- **QR Code Generation**: qrcode library with Pillow
- **Deployment**: Vercel
- **Frontend**: HTML/CSS (embedded in template)
