# Phoenix Plugin Documentation

Plugin documentation is implemented using [VitePress](https://vitepress.dev). This wonderful Vue-based framework allows to generate static websites from Markdown files.

This website is hosted on the [PhoenixDevt website](https://docs.phoenixdevt.fr) and is continously deployed using [TeamCity](https://teamcity.phoenixdevt.fr) whenever changes are pushed to the `main` branch.

## Development

Install dependencies
```sh
npm install
```

Run the development server, it will be running at http://localhost:5173
```sh
npm run docs:dev
```

## Build Website

The static site will be built in the `.vitepress/dist` folder. It can be built using the following command
```sh
npm run docs:build
```

Building the website will reveal dead links and references to non-existing images. This is useful for checking the validity of the documentation before pushing changes to the `main` branch. TeamCity will fail the build if such errors are detected.

## File Systems & Casing

When working on a Windows machine, keep in mind that the Windows file system is case insensitive, while most deployment targets (Linux based) are case sensitive. The TeamCity agent that builds the website is running on a Linux based system, so file name casing issues could show up even if the server builds locally on Windows.

For file names, follow the `lowercase-kebab-case` convention to avoid problems with file name casing. You can use the Python script `scripts/check_file_casing.py` to check for files that feature uppercase characters in their file names.
