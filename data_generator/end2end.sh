#!/usr/bin/env bash
> /data/hails
> /data/vehicles
> /data/rides

./new_hail.py --hail_id hail1
./new_hail.py --hail_id hail2
./new_hail.py --hail_id hail3
./vehicle_online.py --vehicle_id vehicle1
./vehicle_online.py --vehicle_id vehicle2
./vehicle_online.py --vehicle_id vehicle3

sleep 1

./pickup.py --hail_id hail2 --vehicle_id vehicle1 --ride_id ride1
./cancel_hail.py --hail_id hail1

sleep 1

./dropoff.py --ride_id ride1
