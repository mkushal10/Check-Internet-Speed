import speedtest

test = speedtest.Speedtest()

def download_speed():
    speed = round(test.download() / 1_000_000, 2)
    return str(speed) + "Mbps"

def upload_speed():
    speed = round(test.upload() / 1_00_000, 2)
    return str(speed) + "Mbps"

if __name__ == "__main__":
    print(f"Download Speed: {download_speed()}")
    print(f"Upload Speed: {upload_speed()}")
