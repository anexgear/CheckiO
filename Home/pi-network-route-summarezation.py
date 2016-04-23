# Input: A list of strings containing the IP addresses
# Output: A string containing the summary route, represented as an IP address, 
#followed by a slash and the subnet. 

def checkio(data):
    allAdresBin = []
    mask = 0
    for adress in data:
        binAdres = ""
    	for part in adress.split("."):
			binAdres += (bin(int(part)).replace("0b", "")).zfill(8)
        allAdresBin.append(binAdres)
    
    allAdresBin.sort()
    listMaxAdres = []
    listMinAdres = []
    
    for char in allAdresBin[0]:
        listMinAdres.append(char)
    
    for char in allAdresBin[-1]:
        listMaxAdres.append(char)
    IP = ""
    for num in range(len(listMinAdres)):
        if listMaxAdres[num] == listMinAdres[num]:
            mask += 1
            IP += listMinAdres[num]
        else:
            break
    IP = IP.ljust(32, "0")
    return "{}.{}.{}.{}/{}".format(first:(int(IP[:8], 2)), (int(IP[8:16], 2)), (int(IP[16:24], 2)), (int(IP[24:], 2)), mask )
   
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"
