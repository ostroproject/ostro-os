#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netdb.h>
#include <string.h>

int main(int argc, char* argv[])
{
	int sock,ret;
	struct sockaddr_in server_addr, client_addr;
	socklen_t len;
	char message[5];
	char* label;
	char* attr = "security.SMACK64IPIN";
	int port;

	if(argc != 3)
	{
		perror("Server: Argument missing, please provide port and label for SMACK64IPIN");
		return 2;
	}
	
	port = atoi(argv[1]);
	label = argv[2];

	struct timeval timeout;
	timeout.tv_sec = 15;
	timeout.tv_usec = 0;

	sock = socket(AF_INET,SOCK_DGRAM,0);
	if(sock < 0)
	{
		perror("Server: Socket error");
		return 2;
	}
	

	if(fsetxattr(sock, attr, label, strlen(label), 0) < 0)
	{
		perror("Server: Unable to set attribute ");
		return 2;
	}

	server_addr.sin_family = AF_INET;         
	server_addr.sin_port = htons(port);     
	server_addr.sin_addr.s_addr = INADDR_ANY; 
	bzero(&(server_addr.sin_zero),8); 
	

	if(setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, &timeout, sizeof(timeout)) < 0)
	{
		perror("Server: Set timeout failed\n");
		return 2;
	}

	if(bind(sock, (struct sockaddr*) &server_addr, sizeof(server_addr)) < 0)
	{
		perror("Server: Bind failure");
		return 2;
	}

	len = sizeof(client_addr);
	ret = recvfrom(sock, message, sizeof(message), 0, (struct sockaddr*)&client_addr,
					&len);
	close(sock);
	if(ret < 0)
	{
		perror("Server: Error receiving");
		return 1;

	}
	return 0;
}

