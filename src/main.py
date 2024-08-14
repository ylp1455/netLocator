import click
from src.logic import get_ip_address

@click.command()
@click.option(
    "--getIPAD",
    help="This print tthe IPV4 Adress of the computer ",
)

def main():
    ip_address = get_ip_address()
    if ip_address:
        print(f"My IP address is: {ip_address}")
    else:
        print("Unable to determine my IP address.")

if __name__ == "__main__":
    main()

