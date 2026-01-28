### Day 5 – Security, Testing & Production Readiness

### Topics
- Password hashing and authentication security
- CORS, CSRF, SQL Injection, XSS basics
- Centralized error handling- Logging levels and structured logs
- Unit and integration testing
- Dev vs Staging vs Production environments
- Docker basics
- CI/CD overview
- Health checks and monitoring basics

### Project Structure
```project/
 ├── routes
 ├── controllers
 ├── services
 ├── models
 ├── config
 ├── tests
 ├── .env
```

## Pending
- Background jobs and async tasks
- Connect backend to database
- Build one CRUD API




### Password Hashing 
When a user creates an account and sets a password, the system applies a hashing algorithm to convert the plaintext password into a hash. This hash is stored in the database, not the plaintext password. When the user attempts to log in, the system hashes the entered password and compares it with the stored hash. If they match, the user is authenticated.

*However, this also means that two identical passwords will produce the same hash, which could be exploited if not mitigated by techniques like salting passwords.*

Mostly used Hashing algo - SHA-256, bcrypt, Argon2 etc

#### Difference between Hashing and Encryption

**Hashing**
 - One-way Function: Password hashing is a one-way process, meaning once data is hashed, it cannot be reverted to its original form.
 - Fixed Output Length: Regardless of the input size, a hashing algorithm produces a fixed-length string. For instance, * **SHA-256** always generates a 256-bit message digest*, ensuring uniformity in storage and comparison.
 - Primary Use Case: Hashing is primarily used for verifying data integrity and securely storing sensitive information like passwords. When a password is hashed and stored, subsequent password attempts are hashed and compared against the stored hash for verification.

**Encryption**
- Two-way Function: Encryption involves converting plaintext data into ciphertext using an encryption key. The original data can be recovered by decrypting the ciphertext with the appropriate decryption key. This two-way functionality is crucial for protecting data that needs to be accessed and read later.
 - Variable Output Length: The length of the encrypted data (ciphertext) can vary based on the encryption algorithm and the length of the input data. This means encrypted data may not have a consistent size.
 - Primary Use Case: Encryption is used for protecting data in transit and at rest, ensuring that only authorized parties with the correct key can access the original information. Common use cases include secure communication channels (like HTTPS) and encrypted file storage.
In summary, password hashing is used for secure, irreversible storage of data like passwords, while encryption is used for reversible protection of data that needs to be read or accessed later.

#### *Bcrypt is a password hashing function that applies a modified version of the Blowfish cipher*

Bcrypt works as follows:
 - It takes a plaintext password and a random value called a "salt" as input.
 - It uses a modified, computationally expensive key setup algorithm for the Blowfish cipher, known as "Eksblowfish" (expensive key schedule Blowfish).
 - It repeatedly applies the Blowfish function a number of rounds, determined by an adjustable "work factor" or "cost factor".
 - The final output is a unique, fixed-length hash that includes the cost, the salt, and the result of the repeated encryption process embedded within it. 

#### salt is not kept secreat in mordern system
 While the salt (unique per user) is public, some security architectures use a **pepper**. A pepper is a secret, system-wide key that is added to the password hashing process but is not stored in the database. The pepper is typically kept in a separate configuration file or a secure key management system. 



### CORS
Cross-Origin Resource Sharing (CORS) is a browser security mechanism that controls how a web application running on one origin (domain, protocol, or port) can request resources from a different origin. By default, browsers block such cross-origin requests to prevent unauthorized access to sensitive data. CORS provides a controlled way to enable intentional sharing of resources with trusted third-party domains through specific HTTP headers.


**Unit testing and intregration testing**
Unit testing involves testing individual code components in isolation using mocked dependencies, while integration testing verifies the interactions and data flow between multiple components using real or simulated dependencies

### development, staging and production enviroment
https://www.servermania.com/kb/articles/production-development-staging


