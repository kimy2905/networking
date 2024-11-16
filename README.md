# Overview

{This project is a simple chat application designed to enhance my skills as a software engineer by applying networking concepts and exploring client-server communication. The goal was to develop a program that allows multiple clients to connect to a central server, exchange messages, and perform specific requests.}

{The application uses the client-server model to establish communication. Users can join the chat by running the client program, register with a username, and send messages to others. The server handles multiple clients simultaneously, ensuring reliable message delivery.

}

{The purpose of writing this software is to deepen my understanding of network communication and socket programming while building a practical application. By creating a chat application, I aimed to explore how computers interact over a network, implement reliable data exchange, and handle concurrent connections. This project also allowed me to practice key software engineering principles, such as modular code design, multithreading, and real-time communication.

}

[Software Demo Video](https://youtu.be/NgTEjbRv1Ec)

# Network Communication

{
- Architecture: Client-Server Model
- Protocol: TCP (Transmission Control Protocol) for reliable message delivery.
- Port: The server listens on port 7001.

Message Format:
- User Registration: USER|{username}
- Send Message: MSG|{message}
- List Users: DIR

Server Responses:
- USER_OK: Acknowledges username registration.
- MSG_OK: Confirms message delivery.
- Users logged in: {user1, user2, ...}: Lists active users.
}

# Development Environment

{
- Code Editor: Visual Studio Code
- Debugging: Terminal and logging for error tracking
- Testing: Multiple terminal instances on a local machine
}

{
- Programming Language: Python
- socket: For network communication
- threading: To handle multiple clients concurrently
}

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Pyhton Server Libraries](https://docs.python.org/3.6/library/socketserver.html)
* [Python Socket Libraries](https://docs.python.org/3.6/library/socket.html)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Add a Graphical User Interface (GUI) for a more user-friendly experience.
* Create a persistent chat history stored on the server.
* Add encryption for secure message transmission.