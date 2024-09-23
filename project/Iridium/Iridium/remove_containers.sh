echo -------------------$$$$$-------------------
echo "Remove docker_containers..."
echo -------------------$$$$$-------------------
docker stop attacker web ser1 ser2 ser3 ser4 ser5

echo -------------------$$$$$-------------------
echo "Remove docker_network"
echo -------------------$$$$$-------------------

docker network rm simulated_network
