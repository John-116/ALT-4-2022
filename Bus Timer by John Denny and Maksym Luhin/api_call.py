# ALT 4 API Call and Process
# 01|12|2022 by John Denny
from datetime import datetime
import requests
import serial
import time

time_format = "%H%M"

# Assign Bus Stop ID Values
id_for_409 = "8460B525641"
id_for_404_newcastle = "8460B5225701"
id_for_404_oranmore = "8460B5231801"

# Configure Microbit Serial Port
baud_for_mb = 115200
mb_409 = serial.Serial(port="COM12", baudrate=baud_for_mb)  # Green one
mb_404_oranmore = serial.Serial(port="COM11", baudrate=baud_for_mb)  # Blue  one
mb_404_newcastle = serial.Serial(port="COM7", baudrate=baud_for_mb)  # Yellow one


def getArrivalTime(query, bus_name):
    # Make Request and Convert to json
    r_in_json = requests.get(
        f"https://galway-bus.apis.ie/api/gstoptimes/bystopid/{query}/{current_date}"
    ).json()

    for i in range(len(r_in_json["results"][0]["g_stop_times"])):
        arrival_i = r_in_json["results"][0]["g_stop_times"][i]["arrival_time"].replace(
            ":", ""
        )[:4]
        arrival_previous = r_in_json["results"][0]["g_stop_times"][i - 1][
            "arrival_time"
        ].replace(":", "")[:4]

        if (arrival_previous < current_time) and (arrival_i > current_time):

            time_dif_seconds = (
                datetime.strptime(arrival_i, time_format)
                - datetime.strptime(current_time, time_format)
            ).total_seconds()
            time_difference = int((time_dif_seconds // 60))

            print(
                f"The Next {bus_name} bus arrives at {arrival_i} that is in {time_difference} mins"
            )
            return time_difference


def main():
    time_409 = str(getArrivalTime(id_for_409, "409"))
    time_404_oranmore = str(getArrivalTime(id_for_404_oranmore, "404 Oranmore"))
    time_404_newcastle = str(getArrivalTime(id_for_404_newcastle, "404 Newcastle"))

    mb_409.write((time_409 + "\n").encode("utf-8"))
    mb_404_oranmore.write((time_404_oranmore + "\n").encode("utf-8"))
    mb_404_newcastle.write((time_404_newcastle + "\n").encode("utf-8"))


if __name__ == "__main__":
    while True:
        # Get Current Date and Time for API Querys
        current_date = datetime.today().strftime("%Y%m%d")
        current_time = datetime.today().strftime("%H%M")
        main()
        time.sleep(20)
