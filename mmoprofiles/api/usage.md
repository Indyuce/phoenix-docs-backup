---
order: 1
---

# 🔧 API Usage

We provide a Maven repository with API builds for all MMO plugins. Add our repository to your repository list:

```xml
<repository>
    <id>phoenix</id>
    <url>https://nexus.phoenixdevt.fr/repository/maven-public/</url>
</repository>
```

Add ProfileAPI as a dependency:

```xml
<dependency>
    <groupId>fr.phoenixdevt</groupId>
    <artifactId>Profile-API</artifactId>
    <version>1.1</version>
    <scope>provided</scope>
    <optional>true</optional>
</dependency>
```