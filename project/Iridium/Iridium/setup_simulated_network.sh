echo -------------------$$$$$-------------------
echo "Create docker_network"
echo -------------------$$$$$-------------------
docker network create simulated_network

echo -------------------$$$$$-------------------
echo "Create target servers"
echo -------------------$$$$$-------------------

docker run -dit --rm --name ser1 --network simulated_network --user root target-server:1.0.0
docker run -dit --rm --name ser2 --network simulated_network --user root target-server:1.0.0
docker run -dit --rm --name ser3 --network simulated_network --user root target-server:1.0.0
docker run -dit --rm --name ser4 --network simulated_network --user root target-server:1.0.0
docker run -dit --rm --name ser5 --network simulated_network --user root target-server:1.0.0

echo -------------------$$$$$------------------------------------------
echo "Start ssh and ftp services on target servers"
echo -------------------$$$$$------------------------------------------

temp=$(docker exec -it ser1 rc-service sshd start)
temp=$(docker exec -it ser1 rc-service vsftpd start)
temp=$(docker exec -it ser1 rc-service crond start)

temp=$(docker exec -it ser2 rc-service sshd start)
temp=$(docker exec -it ser2 rc-service crond start)

temp=$(docker exec -it ser3 rc-service vsftpd start)
temp=$(docker exec -it ser3 rc-service crond start)

temp=$(docker exec -it ser4 rc-service vsftpd start)
temp=$(docker exec -it ser4 rc-service crond start)

temp=$(docker exec -it ser5 rc-service sshd start)
temp=$(docker exec -it ser5 rc-service vsftpd start)
temp=$(docker exec -it ser5 rc-service crond start)

echo ----------------------------------
echo "Create web server"
echo ----------------------------------
docker run -dit --rm --name web --network simulated_network --user root -p 8000:8000 web-server:1.0.0

echo ----------------------------------
echo "Create attack machine"
echo ----------------------------------
docker run -it --rm --name attacker --network simulated_network --user root attacker-machine:1.0.0
