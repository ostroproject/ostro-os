#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <ifaddrs.h>
#include <stdio.h>
#include <string.h>

int main (void)
{
	struct ifaddrs *ifap, *ifa;
    	struct sockaddr_in *saaddr,*samask;
	struct in_addr netid;
    	char addr[INET_ADDRSTRLEN],mask[INET_ADDRSTRLEN];
	int prefix=0;
    	getifaddrs (&ifap);
    	for (ifa = ifap; ifa; ifa = ifa->ifa_next) {
        	if (ifa->ifa_addr->sa_family==AF_INET) {
            		saaddr = (struct sockaddr_in *) ifa->ifa_addr;
            		samask = (struct sockaddr_in *) ifa->ifa_netmask;
			strncpy(addr,inet_ntoa(saaddr->sin_addr),sizeof(addr));
            		strncpy(mask,inet_ntoa(samask->sin_addr),sizeof(mask));
			netid.s_addr=(saaddr->sin_addr.s_addr & samask->sin_addr.s_addr);
			prefix=__builtin_popcount(samask->sin_addr.s_addr);	
            		printf("Interface: %s\tAddress: %s\tMask: %s\tNetwork: %s\tPrefix: /%d\n",
				 ifa->ifa_name,addr,mask,inet_ntoa(netid),prefix);
        	}
    	}

    	freeifaddrs(ifap);
    	return 0;
}
