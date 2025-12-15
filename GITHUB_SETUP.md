# GitHub Setup and Push Instructions

Follow these steps to push your code to GitHub and build the installer.

## Step 1: Create a GitHub Repository

1. Go to https://github.com and sign in (or create an account)
2. Click the **+** icon in the top right → **New repository**
3. Name it (e.g., `ebook-screenshot-tool`)
4. Choose **Public** or **Private**
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click **Create repository**

## Step 2: Connect Your Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these:

### If you haven't pushed yet (first time):

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

Replace:
- `YOUR_USERNAME` with your GitHub username
- `YOUR_REPO_NAME` with your repository name

### Example:
```bash
git remote add origin https://github.com/johndoe/ebook-screenshot-tool.git
git branch -M main
git push -u origin main
```

## Step 3: Push Your Code

Run the push command. You'll be prompted for your GitHub credentials:
- **Username**: Your GitHub username
- **Password**: Use a Personal Access Token (not your regular password)

### Creating a Personal Access Token:

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click **Generate new token (classic)**
3. Give it a name (e.g., "Ebook Tool")
4. Select scopes: Check **repo** (full control of private repositories)
5. Click **Generate token**
6. **Copy the token immediately** (you won't see it again)
7. Use this token as your password when pushing

## Step 4: Trigger the Installer Build

Once your code is pushed:

1. Go to your GitHub repository
2. Click the **Actions** tab
3. You should see "Build Windows Installer" workflow
4. Click on it
5. Click **Run workflow** → **Run workflow** (green button)
6. Wait for it to complete (usually 2-3 minutes)

## Step 5: Download the Installer

1. In the Actions tab, click on the completed workflow run
2. Scroll down to **Artifacts**
3. Click **EbookScreenshotTool_Setup** to download
4. The installer file will be a ZIP - extract it to get the `.exe` file

## Alternative: Create a Release

For easier distribution:

1. Go to your repository → **Releases** → **Create a new release**
2. Choose a tag (e.g., `v1.0.0`)
3. Add release title and description
4. The workflow will automatically attach the installer to the release
5. Click **Publish release**

## Quick Command Reference

```bash
# Check current remote
git remote -v

# Add remote (if not already added)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main

# For future updates
git add .
git commit -m "Your commit message"
git push
```

## Troubleshooting

### "Remote origin already exists"
If you already have a remote, update it:
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

### "Authentication failed"
- Make sure you're using a Personal Access Token, not your password
- Check that the token has `repo` scope

### "Workflow not running"
- Make sure the `.github/workflows/build-installer.yml` file is in your repository
- Check that you've pushed the code to GitHub
- Go to Actions tab and manually trigger the workflow

