# Concepts
****

#### Infrastructure as a Code

**What is it?**
IAAS means to create and manage IT infrastructure using configuration files. 

**Why would I want it?**
Earlier creating and managing IT infrasturture used to be a manual process, wherein physically servers were setup and configured. Manual process used to be error prone and used to take lot of time and effort. Best part is we can also do versioning.

Few Advantages:-
- cost saving
- increases speed
- Less error prone therefore reducing risks
- Easy to manage
- Can be versioned
- Easy to rollback.
- Easy to delete

**Are there any alternatives ?**

IAAS Tools:-
-   Terraform
-   Cloudformation
-   ARM Templates

Even Ansible, puppet & chef which are most common configuration management tools also has the capability to spin up infrastructure. Plus we can also use AWS SDK with any supported programming language to create infrastructure.

#### Observability 

It's the capability of a person to understand the system and knowing what is wrong or what could go wrong proactively where ever possible.

**What do we want to observe?**
- metrics
- logs
- distributed tracing

**What kind of challenges do you see in a distributed environment? and How can we solve them?**
- microservices need to find each other on network -> rpc frameworks, network proxies and service meshes.
- Need an advanced orchestration platform -> Kubernetes, DockerSwarm
- Complexity increases.-> through tracing, logging and monitoring.

#### Security

**What are the first three things that you check, to limit the risk of a breach?**

- **Trusted Advisor** -> It helps us identify security issues around multiple AWS services, not only security but also advises us other factors like:- performance, costs and service limits.
- **Guard Duty** -> warns us about unprotected port and IAM user related permissions.
- **Inspector** -> Access security risk via pre written security rule packages by AWS and provides recommendation to resolve as per severity levels. 



