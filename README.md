# Custom_tools

## Proxy Checker
The script extracts free proxies from **https://free-proxy-list.net** and verifies their functionality using the **Process** module from the `multiprocessing` library. Each proxy IP is tested by making a request to **http://api.ipify.org**. If a proxy returns a 200 response, it is flagged as "working"; otherwise, it is marked as "non-active." 

To optimize the verification process, the list of proxies is divided into chunks, and these chunks are processed concurrently using `Process`, enabling faster and more efficient validation.
