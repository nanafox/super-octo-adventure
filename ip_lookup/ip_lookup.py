import requests
import ipaddress


def build_lookup_address(ip_address=None, format='json'):
    base_url = 'https://ipapi.co'
    
    if ip_address is not None:
        return f'{base_url}/{ip_address}/{format}'
    

def ip_lookup(url):
    
    """
    :params url: received from the build_lookup_address function
    :action: looks up the requested data
    :returns: API response based on the URL receieved
    """
    requests.get()

if __name__ == '__main__':
    ip = input('Hostname / IP Address: ')
    format = input('Preferred format: ')
    
    
    
# TODO: Ask for hostname or IP Address.
# TODO: Confirm the validity of IP Addresses (use the ipaddress library)
# TODO: 