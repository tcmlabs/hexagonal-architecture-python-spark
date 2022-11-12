# TCM Labs' Python/Spark data engineering white project

This is a Python/Spark white project in which we highlight how to craft a highly maintainable data project which can run both locally, on any developer machine, and remotely on any Spark cluster (including Databricks clusters). This also works with Pandas.

Especially, if you're using Notebooks in production and are unhappy about the quality of the output data, you'll find valuable insights here.

## What problems does this white project intend to solve?

This project is here to help you if you struggle with some of these problems:

- poor data quality
- lack of testing
- costly maintainance
- slow iteration speed
- difficult collaboration
- deployment to production fear
- etc.

This project shows how battle-tested software engineering architecture known to be highly effective in backend or frontend environments can also be applied to data projects, using Spark and/or Pandas.

## Architecture, tests, feedback loop, code quality and environments

Let's zoom into 6 very specific problems that your data engineering project may have:

### Problem #1: "We don't know where and what the business rules are"

This is a **software architecture** problem.

- Quickly find such business rules and modify them
- Allow business/non-software engineer people to read and possible contribute to the project in very isolated places

### Problem #2: "We don't know if the code/business rules behave as expected"

This is a **testing** problem.

How do we solve this?

This repository shows how to write thorough Spark unit tests:

- Ensure business use cases behaves as expected: given a known input, we should determnistically return the same output
- Prevent any regression, so that all previously working feature don't break when new features or bug fixes are merged

### Problem #3: "We're slow to iterate, developing a new feature or fixing a bug takes age"

This is a **feedback loop** problem.

How do we solve this?

- Allow developers get a very fast local feedback loop by allowing them to run tests locally in less than a minute
- Allow continuous integration (CI), by preventing non-functioning code to be merged into `main` branch

### Problem #4: "We always spend a lot of time understanding what the code does, and people complain it's cryptic and hard to decypher"

This is a **code quality** problem.

How do we solve this? We automate the boring yet very important stuffs with tools such as:

- `black` handles code formatting
- `flake8` handles linting
- `Python Type Hints` handles static type checking

### Problem #5: "We had a bug in production because the installed library version didn't match what we're using in development"

This is a **server/machine provisioning** problem.

How do we solve this?

- We make it next to impossible to deploy an application in production without the appropriate dependencies and expected exact versions
- We also allow all developers to work with the same dependency trees, on their machine.

How? We use the following tools:

- `poetry` for managing Python dependencies
- `pyenv` for managing Python binaries

That could work with `pip` + `virtualenv` or `conda`

### Problem #6: "We have duplicated code everywhere, and updating all of this takes age"

This is a **software engineering** problem.

How do we solve this?

- We make domain code explicit in domain services
- We make orchestration logic, ie. what do to sequentially or in parallel, explicit in application services

Code is data, and duplicated data tend to go out of sync. Duplicated code will lead to inconsistent code which will lead to inconsistent results.

## Highlighted software engineering concepts

This repository uses the following **software engineering** concepts:

- [Hexagonal architecture (= ports and adapter)](https://alistair.cockburn.us/hexagonal-architecture); you may be familiar with [Clean architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- Inversion of Control (IoC) and Dependency Injection mecanisms (DI)
- Dependency Inversion Principle (DIP)

We also borrow useful concepts from **Domain-Driven Design (DDD)**, especially:

- Repository pattern
- Application services
- Domain services

Also, we use Domain-Specific Languages (DSLs) ideas to hide the Spark/Pandas implementations details, and focus on the _what_ rather than the _how_. This part is not mandatory.

## Maintainers

Provided to you by [TCM Labs](https://www.tcmlabs.fr/), an expert IT Consulting firm based in Paris, France.

We believe that there's absolutely no difference between data, backend and frontend engineering.

Lead maintainer:

- Jean-Baptiste Musso // jeanbaptiste (at) tcmlabs.fr

## Contributing

Feel free to open issues and pull requests. Contributions are welcomed.
