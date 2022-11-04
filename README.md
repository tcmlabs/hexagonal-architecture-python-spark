# TCM Labs' Python/Spark data engineering white project

This is a Python/Spark white project in which we highlight how to craft a highly maintainable data project which can run both locally, on any developer machine, and remotely on any Spark cluster (including Databricks clusters).

## What problems does it solve?

This project is here to help you if you struggle with data quality, maintainance, testing, collaboration.

### Problem #1: Understand where and what the business rules are (architecture)

- Quickly find such business rules and modify them
- Allow business/non-software engineer people to read and possible contribute to the project in very isolated places

### Problem #2: Ensure code/business rules behave as expected (testing)

This repository shows how to write thorough Spark unit tests:

- Ensure business use cases behaves as expected: given a known input, we should determnistically return the same output
- Prevent any regression, so that all previously working feature don't break when new features or bug fixes are merged

### Problem #3: Ensure very-fast development pace with increased feedback loop

- Allow developers get a very fast local feedback loop by allowing them to run tests locally in less than a minute
- Allow continuous integration (CI), by preventing non-functioning code to be merged into `main` branch

### Problem #4: Code quality

We automate the boring yet very important stuffs:

- formatting with `black`
- linting with `flake8`
- typecheck with Python Type Hints

### Problem #5: Determinism of environemtn from local development up to production cluster

We make it next to impossible to deploy an application in production withouth the appropaita dependencies

- we also do that so that any developers work on the same.

How?

poetry : python dependencies
pyenv: python binaries

Why not pip + virtualenv or conda?
-> That could work, too.

### Software architecture

This project shows that generic software engineering architecture known to be highly effective in backend or frontend environments can also be applied to data projects.

## Highlighted software engineering concepts

This repository uses the following software engineering concepts:

- [Hexagonal architecture (= ports and adapter)](https://alistair.cockburn.us/hexagonal-architecture); you may be familiar with [Clean architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- Inversion of Control (IoC) and Dependency Injection mecanisms (DI)
- Dependency Inversion Principle (DIP)

We also borrow useful tools from Domain-Driven Design (DDD), especially:

- Repository pattern
- Application services
- Domain services

## Maintainers

Provided to you by [TCM Labs](https://www.tcmlabs.fr/), an expert IT Consulting firm based in Paris, France.

Lead maintainer:

- Jean-Baptiste Musso

## Contributing

Feel free to open issues and pull requests
