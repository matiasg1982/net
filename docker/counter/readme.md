# Counter Strike

## Download Counter Strike 1.6
     
  > https://www.cybersports.lt/

## Docker Github
> https://github.com/JimTouz/counter-strike-docker

## Docker command
  
  ### Parameters
  
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |

| Parameter  | Decription | Default Value |
| --- | --- |
| SERVER_NAME | The server name | Counter-Strike 1.6 Server |
| START_MONEY | The initial money | 800 |
| BUY_TIME | The allowed time to buy items in each round (minutes) | 0.25 |
| FRIENDLY_FIRE | Enable or disable the friendly fire. (off: 0, on: 1) | 1 |
| START_MAP | The initial map | de_dust2 |
| MAXPLAYERS | The maximum number of players | 32 |
| ADMIN_STEAM | TBD - amx mod related | TBD |
  
  ### Maps
  
     cs_assault
     de_dust2
     de_inferno
     de_nuke
     de_train
     de_dust2_2x2
     fy_pool_day
     fy_snow
     awp_india
     aim_map
  
  ### Command 
  
  ```
  docker run -d -p 26900:26900/udp -p 27020:27020/udp -p 27015:27015/udp -p 27015:27015 -e START_MAP=de_dust2 -e SERVER_NAME="[nombre_servidor]" -e START_MONEY=16000 -e BUY_TIME=0.25 -e ADMIN_STEAM=0:1:1234566 --name cs cs16ds/server:latest +log
  ```
