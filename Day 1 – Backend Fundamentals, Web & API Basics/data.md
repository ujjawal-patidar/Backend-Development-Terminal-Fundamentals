**Frontend Development**

-> UI

-> Responsiveness

-> interactivity

-> cross browser Compatibility

Technologies -> react, angular, HTML, CSS, JS, tailwind etc







**A 1-tier architecture in web architecture is the simplest model where the presentation (UI), business logic, and data layers all reside on a** 


**A 2-tier architecture** 

A 2-tier architecture in web design involves two main layers: the Client Tier (Presentation Layer), handling user interface, and the Data Tier (Database), storing data, with direct communication between them



2-Tier: Client <-> Database (Simpler, less scalable).

3-Tier: Client <-> Application Server <-> Database (Adds a middle layer for business logic, better scalability and separation of concerns). 




**How the web works: DNS → HTTP → Response**
1. Enter a URL
2. user input \& Browser Cache  check
3. **DNS Resolver (ISP Server) :** ISP uses DNS resolver to convert the URL into the IP address for this it checks it in its cache
4. Root Server Query : points the resolver to the correct top - level - domain
5. TLD (Top level domain) server : (like .com server) which then direct it to ANS
6. Authoritative Name Server : names to IP it has all the records it will provide
7. Response and Caching: The resolver receives the IP caches it for your future use and sends it back to your computer.
8. Now browser uses this IP for the request from server


**DNS->TCP->TLS->HTTPS :** 

The sequence **DNS->TCP->TLS->HTTPS** describes the layers of network protocols for secure web browsing: first, DNS (Domain Name System) finds the website's IP address, then TCP (Transmission Control Protocol) establishes a reliable connection, followed by TLS (Transport Layer Security) encrypting that connection (like an encrypted TCP/IP session), and finally HTTPS (HTTP over TLS) sends encrypted application data (web content) securely over that encrypted link, securing your interaction with websites. 

When you type a URL, your browser first uses DNS to find the IP, then establishes a TCP connection. Next, TLS is layered on top to encrypt that connection, and finally, HTTPS (HTTP over TLS) uses this secure tunnel to exchange web page content. 







**HTTP METHODS**

HTTPS methods are the standard HTTP request verbs (like GET, POST, PUT, DELETE, PATCH) used to communicate with web servers, with HTTPS adding a layer of encryption (TLS/SSL) for secure communication, but the methods themselves define the action (read, create, update, delete) on a resource, working the same way as regular HTTP but securely. 

**Key methods include** 

GET (retrieve data), 

POST (send data to create/update), 

PUT (replace resource), 

PATCH (partially update),

DELETE (remove resource). 





**STATUS CODE :** 

Informational responses (100 – 199)

Successful responses (200 – 299)

Redirection messages (300 – 399)

Client error responses (400 – 499)

Server error responses (500 – 599)





##### **API versioning**

is the process of managing and tracking changes to an API to ensure that new features, bug fixes, and performance improvements can be introduced without breaking existing client applications. It is a critical practice for maintaining compatibility, providing a stable experience for consumers, and allowing the API to evolve over time. 



Use Semantic Versioning (SemVer): Employ a MAJOR.MINOR.PATCH format to clearly communicate the scope of changes (major for breaking changes, minor for new features, patch for bug fixes).









**todo:**

fetch("https://jsonplaceholder.typicode.com/posts").then((res)=>{console.log(res); return res.json()}).then((data)=>{console.log(data)});




**in progress :** 

python - code understanding

ci/cd

deploynment

Cloudes aws, AZURE, GCP 

vertex AI

langchain and langgraph RAG

DATA bricks

