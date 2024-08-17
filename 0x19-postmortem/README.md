![creative_2024-08-17_1723916839](https://github.com/user-attachments/assets/fb01930d-73cd-49a2-ab47-6dfefb3b0464)
# Postmortem: Outage of the Job Recommender System on August 17, 2024.

## Issue Summary
Duration: August 15, 2024, 10:00 AM - 12:30 PM (UTC)
Impact: The Job Recommender System experienced a complete outage, rendering the service inaccessible to 100% of users. Users attempting to access the platform were met with a "503 Service Unavailable" error, preventing them from receiving job recommendations or interacting with the dashboard.
Root Cause: The root cause of the outage was a misconfiguration in the Nginx server, leading to a memory leak and subsequent server crash.

## Timeline
10:00 AM: Issue detected via monitoring alert indicating high memory usage on the server.
10:05 AM: The on-call engineer noticed that the Nginx server was unresponsive and escalated the issue to the DevOps team.
10:10 AM: Initial assumption was that the issue was related to a recent deployment. The deployment was rolled back, but the issue persisted.
10:30 AM: Investigations into the application logs showed no errors, leading to misleading paths suggesting database connectivity issues.
11:00 AM: After further inspection, it was discovered that the Nginx server was consuming an abnormal amount of memory, pointing to a potential memory leak.
11:15 AM: The issue was escalated to the System Administration team to inspect the server configuration.
11:45 AM: The root cause was identified as a misconfiguration in the Nginx server’s worker processes, which was causing the memory leak.
12:00 PM: The Nginx configuration was corrected, and the server was restarted.
12:15 PM: Monitoring confirmed the server was stable, and all services were back online.
12:30 PM: The issue was fully resolved, and the incident was closed.

## Root Cause and Resolution
Root Cause: The Nginx server was configured with an excessive number of worker processes (8), which led to a memory leak as each process consumed more memory than the server could handle. This configuration was set during a previous update to optimize performance but was not tested thoroughly under peak loads. As traffic increased, the memory usage escalated, eventually causing the server to crash.
Resolution: The Nginx configuration was revised to reduce the number of worker processes to 4, a number more appropriate for the server’s available memory. Additionally, a memory limit was imposed on each process to prevent similar issues in the future. After making these changes, the server was restarted, and monitoring tools confirmed that the system was stable and operating within normal parameters.

## Corrective and Preventative Measures
### Improvements:
Testing Configuration Changes: Implement a more rigorous testing procedure for server configurations, especially those related to performance optimization. This will include stress-testing the server under peak traffic conditions to identify potential issues before they impact production.
Enhanced Monitoring: Expand monitoring to include alerts for memory usage specific to each Nginx worker process. This will enable earlier detection of potential memory leaks.
Documentation and Review: Update the server configuration documentation to reflect the optimal settings and ensure these are reviewed by multiple teams before deployment.
### Tasks:
Patch Nginx Server: Apply the revised Nginx configuration across all servers in the production environment.
Add Memory Monitoring: Implement monitoring for individual Nginx worker processes and set up automated alerts.
Conduct Load Testing: Schedule regular load testing sessions to ensure the server can handle peak traffic without issues.
Review Deployment Process: Review and update the deployment process to include thorough testing of server configurations.
Team Training: Provide training to the DevOps and System Administration teams on best practices for server configuration and performance monitoring.
