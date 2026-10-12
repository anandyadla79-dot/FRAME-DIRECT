# 🌱 Farm Direct Marketplace

A beginner-friendly agricultural marketplace built with Python, Flask, SQLite, HTML, and CSS. It helps farmers publish their products and lets customers browse listings and contact farmers directly.

## Features

- Add agricultural product listings
- Browse product cards with price, quantity, farmer, and location
- Search by product name, category, or location
- Call a farmer using the contact link
- Delete product listings
- SQLite database with sample listings on first run
- Responsive layout for mobile and desktop
- Input validation and friendly messages

## Tech stack

- **Backend:** Python and Flask
- **Database:** SQLite
- **Frontend:** HTML and CSS
- **Version control:** Git and GitHub

## Project structure

```text
farm_direct_marketplace/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_product.html
│   └── 404.html
└── static/
    └── style.css
```

The SQLite database file is created automatically when the app starts and is excluded from Git.

## Run locally

### 1. Install Python

Install Python 3.10 or newer from https://www.python.org/downloads/. On Windows, select **Add Python to PATH** during setup.

### 2. Download or clone this repository

```bash
git clone https://github.com/YOUR-USERNAME/farm-direct-marketplace.git
cd farm-direct-marketplace
```

Or download the ZIP from GitHub and extract it.

### 3. Create a virtual environment

**Windows (Command Prompt):**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Start the app

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

The first run creates the SQLite database and adds three sample products.

## How to use

1. Open the Marketplace page.
2. Search by product, category, or location.
3. Select **Add Product** to publish a listing.
4. Enter the product details and select **Publish product**.
5. Use **Contact farmer** to open your device's calling app.
6. Delete a listing with **Delete listing**.

## Upload to GitHub

Create a new empty repository on GitHub named `farm-direct-marketplace`. Do not add a README on GitHub if you already have this README locally.

From the project folder, run:

```bash
git init
git add .
git commit -m "Build Farm Direct Marketplace"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/farm-direct-marketplace.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. GitHub may ask you to sign in or authenticate.

## Future improvements

- Farmer and customer registration/login
- Farmer-only editing and deletion permissions
- Product photos and image upload
- Product categories and filters
- Telugu and other local language support
- Order requests and order history
- Farmer Producer Organisation (FPO) accounts
- Admin moderation and product verification
- Deployment to a hosting service

## Important notes

- This is a learning/demo project. It does not process payments or verify farmer identities.
- Sample contact details are fictional placeholders; replace them with test data you control.
- The current delete function is open to all visitors. Add authentication and authorization before deploying publicly.
- Change `app.secret_key` to a strong environment-based secret before deployment.
- Debug mode is enabled for local development only. Do not use it in production.

## License

This project is available under the MIT License. Add a `LICENSE` file if you want to formally publish it under that license.
