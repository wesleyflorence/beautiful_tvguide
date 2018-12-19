# beautiful_tvguide
using beautiful soup and selenium to get tv schedule.

### Design
Script is run on 15 minute intervals on a remote server using the crontab.
Tv schedual updates the Firebase Realtime database which provides data for the WibbleWobble app.

### Requires ServiceAccountsKey.json
To run this you need a service accounts Key in same directory.
You can generate this key for your firebase project [here.](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk)

### Crontab
```
PATH=/home/wes/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
*/15 * * * * echo $(date) >> /home/wes/WibbleWobble/beautiful_tvguide/bash_cron_log.txt
*/15 * * * * /home/wes/WibbleWobble/beautiful_tvguide/tvguide.py >> /home/wes/WibbleWobble/beautiful_tvguide/bash_cron_log.txt
```
