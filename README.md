# ShopImpact

A friendly Streamlit app to log purchases, estimate CO₂ impact, earn eco-badges, and reflect mindfully.

## Quick local run
1. Open PowerShell and cd into the project folder:

```powershell
cd "C:\Users\dwijv\OneDrive\Desktop\Python SA 1"
```

2. (Optional) Activate virtual environment:

```powershell
& "C:/Users/dwijv/OneDrive/Desktop/Python SA 1/.venv/Scripts/Activate.ps1"
```

3. Install dependencies (if not already):

```powershell
"C:/Users/dwijv/OneDrive/Desktop/Python SA 1/.venv/Scripts/python.exe" -m pip install -r requirements.txt
```

4. Run the app:

```powershell
streamlit run ShopImpact.py
```


## Deploy to GitHub and Streamlit Community Cloud
Follow these steps to publish your app to Streamlit Community Cloud.

1. Initialize Git and commit your code (if you haven't):

```powershell
git init
git add .
git commit -m "Initial commit: ShopImpact Streamlit app"
```

2. Create a new repository on GitHub (via web). Then link and push:

```powershell
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```

3. Deploy on Streamlit Community Cloud:
- Go to https://share.streamlit.io and sign in with GitHub.
- Click **New app** → select your repository → set **Main file path** to `ShopImpact.py` and branch `main` → Deploy.

4. App will build using `requirements.txt`. When finished, Streamlit provides a live URL you can share.


## Notes about data persistence
- The app writes `data/purchases.csv` locally. On Streamlit Community Cloud, the filesystem is ephemeral: files saved at runtime may be lost after redeploy or container restart.
- For persistent storage consider:
  - Google Sheets (via API), Airtable, or Supabase (recommended for simple apps).
  - A small cloud database (Supabase or Postgres) for production.


## Extra tips
- If deployment fails due to package versions, pin versions in `requirements.txt`, e.g. `streamlit==1.22.0`.
- To enable automated deploys, enable auto-deploy from the Streamlit app settings (it redeploys on `main` pushes).