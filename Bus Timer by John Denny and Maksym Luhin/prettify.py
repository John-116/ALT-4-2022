import requests
import json


# Internal Tool for getting prettified JSON output
def main():
    out_name = input("Name for your output file (Without Extension): ")
    domain = input("Input a domain name: ")
    r = requests.get(domain)
    with open(out_name + ".json", "w") as out_file:
        out_file.write(json.dumps(r.json(), indent=4))
    print(f"Output for domain {domain[8:20]}... saved to file {out_name}.json")


if __name__ == "__main__":
    main()
