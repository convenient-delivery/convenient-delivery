#Be sure sshpass is installed
USER=root
SERVER=zachsminecraft.us
PASSWORD=feengeuh

sshpass -p $PASSWORD rsync -avz /home/convenient/ $USER@$SERVER:/home/zach/backups 
sshpass -p $PASSWORD rsync -avz /etc/nginx/ $USER@$SERVER:/home/zach/backups/nginx 
sshpass -p $PASSWORD rsync -avz /etc/supervisor/ $USER@$SERVER:/home/zach/backups/supervisor 
