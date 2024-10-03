# Adapter Pattern
The Adapter Pattern is a structural design pattern in software development that allows incompatible interfaces of two systems or objects to work together. The main purpose of the adapter pattern is to "adapt" one interface into another that a client expects, without modifying the original interfaces.

It acts like a bridge between two incompatible interfaces. By using an adapter, you can make an existing class work with others without changing its source code.

## Key Concepts:
- Client: The system or code that expects a certain interface.
- Adapter: The class that implements the expected interface and translates the calls from the client to the adaptee.
- Adaptee: The existing class or system with an incompatible interface that needs to be adapted.

## Example of Adapter Pattern:
Let's say you have an existing application that works with square plugs (client), but you need to integrate it with a new round plug (adaptee). Instead of modifying the existing system or the plug, you use an adapter that allows the square plug to work with the round plug.

## Real-World Example:
You can think of the adapter pattern like a power plug adapter. Different countries have different plug shapes and voltages, but if you travel, you use an adapter to allow your plug (say a European two-pin plug) to fit into a different type of socket (say a US socket).