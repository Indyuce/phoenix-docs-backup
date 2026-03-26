---
order: 1
---

# 📦 Maven

## Repository

We provide a Maven repository with API builds for all MMO plugins. Add our repository to your repository list:

```xml
<repository>
    <id>phoenix</id>
    <url>https://nexus.phoenixdevt.fr/repository/maven-public/</url>
</repository>
```

## Dependency

Include the following dependency in your Maven `pom.xml`

```xml
<dependency>
    <groupId>net.Indyuce</groupId>
    <artifactId>MMOInventory-API</artifactId>
    <version>2.0-SNAPSHOT</version>
    <scope>provided</scope>
</dependency>
```
