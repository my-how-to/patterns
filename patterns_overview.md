# 🧩 Patterns Overview

This document lists all **23 classic Design Patterns** as described by the *Gang of Four (GoF)*, grouped by category.
Each entry includes a short, one-line description for quick reference.

---

## 🏗️ Creational Patterns

| Pattern              | Description                                                                     |
| -------------------- | ------------------------------------------------------------------------------- |
| **Factory Method**   | Creates objects without specifying the exact class to instantiate.              |
| **Abstract Factory** | Produces families of related objects without specifying their concrete classes. |
| **Builder**          | Separates the construction of a complex object from its representation.         |
| **Prototype**        | Creates new objects by copying existing ones (cloning).                         |
| **Singleton**        | Ensures a class has only one instance and provides a global access point.       |

---

## 🧱 Structural Patterns

| Pattern       | Description                                                                               |
| ------------- | ----------------------------------------------------------------------------------------- |
| **Adapter**   | Bridges incompatible interfaces so that classes can work together.                        |
| **Bridge**    | Separates an object’s abstraction from its implementation so they can vary independently. |
| **Composite** | Composes objects into tree structures to represent part-whole hierarchies.                |
| **Decorator** | Dynamically adds or modifies functionality of an object at runtime.                       |
| **Facade**    | Provides a simplified interface to a larger body of code.                                 |
| **Flyweight** | Reduces memory usage by sharing common data between similar objects.                      |
| **Proxy**     | Controls access to another object, often adding additional behavior.                      |

---

## 🔁 Behavioral Patterns

| Pattern                     | Description                                                                               |
| --------------------------- | ----------------------------------------------------------------------------------------- |
| **Chain of Responsibility** | Passes requests along a chain of handlers until one processes it.                         |
| **Command**                 | Encapsulates a request as an object, allowing parameterization and queuing of operations. |
| **Interpreter**             | Defines a grammar and interpreter for a language or symbolic expressions.                 |
| **Iterator**                | Provides a way to access elements of a collection without exposing its structure.         |
| **Mediator**                | Defines an object that coordinates communication between multiple objects.                |
| **Memento**                 | Captures and restores an object’s internal state without exposing details.                |
| **Observer**                | Allows objects to subscribe and react to events or state changes in another object.       |
| **State**                   | Allows an object to alter its behavior when its internal state changes.                   |
| **Strategy**                | Defines a family of algorithms and makes them interchangeable at runtime.                 |
| **Template Method**         | Defines the skeleton of an algorithm, letting subclasses override certain steps.          |
| **Visitor**                 | Separates an algorithm from the objects it operates on for easier extension.              |

---

## 📚 Notes

Each pattern includes:

* A **Before Version** showing the old manual or repetitive approach.
* A **Pattern Version** showing the improved structured solution.
* Consistent **comments**, **example output**, and a short **history** in each file.

> This overview serves as a reference and progress checklist as the repository expands to include all 23 patterns.
