# Low Level System Design

## class Diagrams
    - Identify differnt Entities
    - Identify attributes and method with respect to entities
    - Identify relationships like association, dependencies, inheritence
## Apply solid principles
    - Single responsibility -> a class should have only single reason to change
    - Open/close -> open for extention but close for edit
    - Liskov substitution -> subclass can be substituted with parent class
    - Interface segragation -> a client should not forced to implement interface if it doesn't uses it
    - Dependency Inversion -> High level module should not depend on low level module - both should depend on abstration

## Identify which patterns to use

 ### Creational Pattern
    - Singleton pattern
    - Factory pattern
    - Abstract Factory
    - Builder pattern
    - Prototype pattern

 ### Structural Patterns
    - Adaptor Pattern
    - Decorator Pattern
    - Facade Pattern
    - Proxy Pattern
    - Composite

 ### Behaviour Patterns
    - Observer Pattern
    - Strategy Pattern
    - Command Pattern
    - Chain of Responsibility Pattern
    - State Pattern

 ### Concurrency Pattern
    - Producer-Consumer Pattern
    - Thread Pool Pattern
    - Future Pattern
    - Locking Pattern

 ### Caching Pattern
    - Cache aside Pattern
    - Write Through Cache Pattern
    - Read Through Cache Pattern
    
 ### Error Handling Pattern
    - Retry Pattern
    - Circuit Breaker Pattern
    - Fallback Pattern

 ### Data Management Pattern
    - Repository Pattern
    - Active Record Pattern
