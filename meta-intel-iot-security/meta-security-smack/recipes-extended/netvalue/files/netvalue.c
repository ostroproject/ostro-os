/*
 *               Copyright (c) 2012, 2013, Intel Corporation
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions are met:
 *
 *    - Redistributions of source code must retain the above copyright notice,
 *     this list of conditions and the following disclaimer.
 *
 *    - Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *
 *    - Neither the name of Intel Corporation nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 *  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 *  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 *  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
 *  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 *  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 *  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 *  OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 *  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 */
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
