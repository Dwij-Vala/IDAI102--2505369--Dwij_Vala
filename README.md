# ShopImpact 🌱

A Streamlit web app for tracking purchases, estimating CO₂ impact, and promoting eco-friendly shopping habits.

## Features

- 📝 Log purchases with price and category
- 🌍 Real-time CO₂ impact estimation
- 📊 Monthly impact dashboard
- 🏅 Earn eco-badges for sustainable choices
- 💭 Mindful reflection prompts
- 🌱 Eco-friendly shopping tips

## Quick Start

1. Install Python requirements:
```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:
```bash
streamlit run ShopImpact.py
```

## Deployment

The app is deployed on Streamlit Cloud and can be accessed at:
https://idai102-2505369--dwijvala-shopimpactapp.streamlit.app/

- 💚 Get personalized eco-friendly suggestions

- 🎨 Dark mode and accessibility options2. (Optional) Activate virtual environment:



## Local Development```powershell

& "C:/Users/dwijv/OneDrive/Desktop/Python SA 1/.venv/Scripts/Activate.ps1"

1. Clone the repository:```

```bash

git clone https://github.com/Dwij-Vala/IDAI102-2505369--Dwij_Vala.git3. Install dependencies (if not already):

cd IDAI102-2505369--Dwij_Vala

``````powershell

"C:/Users/dwijv/OneDrive/Desktop/Python SA 1/.venv/Scripts/python.exe" -m pip install -r requirements.txt

2. Create and activate a virtual environment:```

```bash

python -m venv .venv4. Run the app:

.venv\Scripts\activate  # Windows

source .venv/bin/activate  # Linux/Mac```powershell

```streamlit run ShopImpact.py

```

3. Install dependencies:

```bash

pip install -r requirements.txt## Deploy to GitHub and Streamlit Community Cloud

```Follow these steps to publish your app to Streamlit Community Cloud.



4. Run the app:1. Initialize Git and commit your code (if you haven't):

```bash

streamlit run ShopImpact.py```powershell

```git init

git add .

The app will open in your default browser at http://localhost:8501git commit -m "Initial commit: ShopImpact Streamlit app"

```

## Deploying to Streamlit Cloud

2. Create a new repository on GitHub (via web). Then link and push:

1. Fork/push this repository to your GitHub account

2. Sign up for [Streamlit Cloud](https://streamlit.io/cloud)```powershell

3. Create New App → select this repositorygit remote add origin https://github.com/<your-username>/<repo-name>.git

4. Main file path: `ShopImpact.py`git branch -M main

git push -u origin main

## Data Storage```



The app uses local CSV storage (`data/purchases.csv`) for development. For production, consider using:3. Deploy on Streamlit Community Cloud:

- Supabase- Go to https://share.streamlit.io and sign in with GitHub.

- Google Sheets- Click **New app** → select your repository → set **Main file path** to `ShopImpact.py` and branch `main` → Deploy.

- Other cloud database

4. App will build using `requirements.txt`. When finished, Streamlit provides a live URL you can share.

## Contributing



Feel free to open issues and pull requests!## Notes about data persistence
- The app writes `data/purchases.csv` locally. On Streamlit Community Cloud, the filesystem is ephemeral: files saved at runtime may be lost after redeploy or container restart.
- For persistent storage consider:
  - Google Sheets (via API), Airtable, or Supabase (recommended for simple apps).
  - A small cloud database (Supabase or Postgres) for production.


## Extra tips
- If deployment fails due to package versions, pin versions in `requirements.txt`, e.g. `streamlit==1.22.0`.
- To enable automated deploys, enable auto-deploy from the Streamlit app settings (it redeploys on `main` pushes).
=======
# IDAI102--2505369--Dwij_Vala
>>>>>>> eec12a6c448af8c8dc15bb73bbc4a894355b9708
