# Create Spotify playlists according to Billboard's Top 100 on a date you want

## Tecnologies and Requirements

+ `python >= 3.11.5`
+ `bash`, `powershell` or some cmd
+ You should have a Spotify account
+ Internet connection

## Setting up your Spotify account authentication

1. Once you has a Spotify account, go to [developer dashboard](https://developer.spotify.com/dashboard) and press on the **Create an app** button.
2. Fill the form as follow:
   1. App name: Billboard To Spotify
   2. App description: (it's up to you)
   3. Redirect URI: `http://example.com`
   4. Select the **Web Playback SDK** checkbox
   5. Agree the conditions
   6. Press **Save** button
3. Then, go to your app **Settings** and be ready to copy some values in the `constants.py`
   1. **Client ID**
   2. **Client secret**
   3. **Redirect URIs**
4. You can obtain your username by copying it from the url when you go to your profile page, e.g. `https://open.spotify.com/user/<username - only copy this part>`

## Usage

Instalation

```cmd
# Clone the repo on your current cwd
git clone git@github.com:hiahir357/billboard-to-spotify

# Go to the repo folder
cd billboard-to-spotify

# Install the requirements
# Windows
pip install -r requirements.txt
# Linux
pip3 install -r requirements.txt
```

Creating a playlist

```cmd
$ python main.py
Which year do you want to travel to? Type de date in this format YYYY-MM-DD -> 2002-08-12
```

The first time you run it, it'll open a window for authorizing your Spotify account to use the app. In that case, you have to agree and wait for a redirection. Copy the whole url from it and paste it in the console. It should be displaying something like this:

`$ Enter the URL you were redirected to: <paste the url here>`

## That's all

I hope you enjoy it 😊
