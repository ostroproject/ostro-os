#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netdb.h>
#include <string.h>

int main(int argc, char* argv[])
{
	char* message = "hello";
	int sock, ret;
	struct sockaddr_in server_addr;
	struct hostent*  host = gethostbyname("localhost");
	char* label;
	char* attr = "security.SMACK64IPOUT";
	int port;
	if (argc != 3)
	{
		perror("Client: Argument missing, please provide port and  label for SMACK64IPOUT");
		return 2;
	}

	port = atoi(argv[1]);
	label = argv[2];
	sock = socket(AF_INET, SOCK_DGRAM,0);
	if(sock < 0)
	{
		perror("Client: Socket failure");
		return 2;
	}
	

	if(fsetxattr(sock, attr, label, strlen(label),0) < 0)
	{
		perror("Client: Unable to set attribute ");
		return 2;
	}


	server_addr.sin_family = AF_INET;
	server_addr.sin_port = htons(port);
	bcopy((char*) host->h_addr, (char*) &server_addr.sin_addr.s_addr,host->h_length);
	bzero(&(server_addr.sin_zero),8);
	
	ret = sendto(sock, message, strlen(message),0,(const struct sockaddr*)&server_addr,
			sizeof(struct sockaddr_in));

	close(sock);
	if(ret < 0)
	{
		perror("Client: Error sending message\n");
		return 1;
	}
	
	return 0;
}

