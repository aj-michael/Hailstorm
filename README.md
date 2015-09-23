# Hailstorm

This system models a real-time taxi hailing system. In this model, passengers hail taxis with the current timestamp and their latitude and longitude. Passengers can cancel their hail any time before they are picked up. Vehicles can come online whenever and can go offline whenever they are not currently transporting a passenger. Information regarding hails, cancels, vehicles coming on and offline, pickups and dropoffs are input'd to the system by appending to one of three files.

The system consists of two components, a data consumer that watches the input files and an HTTP server the presents an API to query the current state of the data.

## Prereqs

This project has only been tested on Python 2.7 and requires the Twisted framework (`pip install twisted`).

## Input

All input is tab-delimited lines appended to one of three files.

### Hail file

In all of the following examples this file will be `/data/hails`.

The input format to hail a taxi is

```
New hail    <timestamp>    <hail_id>    <latitude>    <longitude>
```

The input format to cancel a previous hail is

```
Cancelled hail    <timestamp>    <hail_id>
```

### Vehicle file

In all of the following examples this file will be `/data/vehicles`.

The input format to bring a vehicle online is

```
Vehicle online    <timestamp>    <vehicle_id>
```

The input format to take a vehicle offline is

```
Vehicle offline    <timestamp>    <vehicle_id>
```

### Ride file

In all of the following examples this file will be `/data/rides`.

The input format to pickup a passenger is

```
Ride pickup    <timestamp>    <ride_id>    <hail_id>    <vehicle_id>
```

The input format to dropoff a passenger is

```
Ride dropoff    <timestamp>    <ride_id>
```

## Generating Data

As much as I love manually echo'ing to append to files, testing Hailstorm with any non-trivial use cases is very cumbersome to do manually. The `./data_generator` directory provides helper scripts for each of the input formats described above. They all support command line arguments to specify file paths and ids. Check the help menus (`-h`) for each as necessary.

## Hailstorm Server

The Hailstorm server can be found at `./server/hailstorm.py`. By default it will run on port 12347. You can change this port and also the log file through command line flags. Check `./server/hailstorm.py -h` if you need help.

## Data Consumer

The data consumer can be found at `./consumer/hailstormconsumer.py`. To run it, you will need to know the file locations of your three input files as well as the hostname and port of the Hailstorm server you will be talking to. Additionally, you can specify a log file if you do not wish for the logs to be displayed to STDOUT. Check `./consumer/hailstormconsumer.py -h` if you need help running it.


## API

Hopefully if you're reading this, you have both the Hailstorm Server and the Data Consumer set up and running. Ideally you've also used some of the Generating Data scripts to simulate a small scenario. Congrats! You are now ready to check out the API. If you don't want to see errors about favicons not being routed correctly, I suggest you use wget instead of Chrome.


To see all hails:

`wget -qO- http://127.0.0.1:12347/hails`

To see hails by status:

`wget -qO- http://127.0.0.1:12347/hails/{waiting,transit,arrived}`

To see all vehicles:

`wget -qO- http://127.0.0.1:12347/vehicles`

To see vechiles by status:

`wget -qO- http://127.0.0.1:12347/vehicles/{offline,available,transit}`

To see the hails in the past hour, broken down by status:

`wget -qO- http://127.0.0.1:12347/status/pasthourhails`

To see the project hails for the next hour:

`wget -qO- http://127.0.0.1:12347/status/projectedhails`

To see the projected wait time for the next hour:

`wget -qO- http://127.0.0.1:12347/status/projectedwait`
