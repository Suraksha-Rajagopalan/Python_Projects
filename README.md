# Python_Projects
Here are some of the python projects which I have completed successfully. 

<h2>1. Automate Email Sending</h2>
<h4> 🤔Service Provider </h4>
In that moment we surely realized that sending, receiving and storing Emails requires the use of a Service Provider. Among these the most common are certainly Google Mail, Microsoft Outlook and Apple iTunes.

It is therefore inevitable to talk about the 3 famous protocols that characterise Email Service Providers:

<p>i. SMTP: is the protocol used for sending emails. Its acronym stands for Simple Mail Transfer Protocol. This is what we’re going to use in this article.</p>
<p>ii. IMAP and POP, on the other hand, are the other two popular protocols that are used respectively to read and download Emails from/in our Client.</p>

<h4>  🧠The Flow</h4>
Flow of Algorithm:
<p>i. With Python we will instantiate an encrypted connection (STARTTLS) with our Service Provider.</p>
<p>ii. After receiving our Email, our Service Provider (the Sender Server) will send it through SMTP to the Recipient Service Provider (the Recipient Server).</p>
<p>iii. The Recipient’s Server can be used by the Recipient’s Client to read the Email via IMAP or POP.</p>


