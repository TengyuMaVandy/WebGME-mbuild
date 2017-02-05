set webgme_dir=E:\Users\TengyuMa\WebGME\WebGME-mbuild
cd /D %webgme_dir%
start cmd /c "cd /D E:\Users\TengyuMa\WebGME\WebGME-mbuild & npm start"
start cmd /c "start chrome "http://localhost:8888""
mongod --dbpath db