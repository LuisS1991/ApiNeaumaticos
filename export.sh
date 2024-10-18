API_URL=https://apineumaticos-production.up.railway.app reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
chmod -R 777 ./public 


#win 10
#$env:API_URL="https://apineumaticos-production.up.railway.app"
#reflex export --frontend-only
