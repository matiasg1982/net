# Counter Strike

## Download Counter Strike 1.6
  
  Link descarga juego: 
    >https://www.cybersports.lt/

## Docker command:
  
  ### Parameters:
    
    SERVER_NAME
    START_MONEY
    BUY_TIME
    FRIENDLY_FIRE
    START_MAP
    MAX_PLAYERS
    ADMIN_STEAM
  
  ```
  docker run -d -p 26900:26900/udp -p 27020:27020/udp -p 27015:27015/udp -p 27015:27015 -e MAXPLAYERS=32 -e START_MAP=de_dust2 -e SERVER_NAME="[nombre_servidor]" -e START_MONEY=16000 -e BUY_TIME=0.25 -e FRIENDLY_FIRE=1 -e ADMIN_STEAM=0:1:1234566 --name cs cs16ds/server:latest +log
  ```
