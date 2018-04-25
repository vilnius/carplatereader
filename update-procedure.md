# Backend update

```
cd ~/cpr/cpr-server
git pull
npm install  # optional
```
IMPORTANT: Create/Update configuration file `config.js` based on `config.js.template` if it was changed.

Restart the whole service:
```
sudo systemctl restart cpr
```
If there are any errors, you can inspect log messages at `/var/log/messages`.

## Optional

Clean up docker system files:
```
docker system prune -a
```

Rebuild docker image:
```
docker build -t openalpr https://github.com/openalpr/openalpr.git
```

# Frontend update

```
cd ~/cpr/cpr-frontend/
git pull
rm -rf node_modules  # optional
npm install          # optional
npm run build:prod
```
If errors - inspect and update dependencies (e.g. minor version broke things)

# Testing

You can test if system is operational by adding a new image for the script to process.
Find image id by browsing around https://cpr.vilnius.lt then go into `incomming` folder and download it:
```
cd /home/camera/incomming
wget http://localhost:2370/api/images/123456789978645.jpg
# note that we are going directly to uwsgi process socket, bypassing nginx and https
```
You can launch processing immediately by executing command specified in:
```
crontab -l
```
