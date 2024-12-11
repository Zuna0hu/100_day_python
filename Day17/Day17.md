# Day 17 Create a Quiz Game




## How to Name a Class

To name a class in Python, it is common to use Pascal Case like `PascalCase`, with the first letters in the words being capitalized.

### Other Naming Methods
It is different from Camel Case like `camelCase`, where only the first word is in lowercase, but every subsequent word has its first letter capitalized.

Also, sometimes we can see vairables seperated by an underscore in Python, like `snake_case`.

## What is Object Initialization

How can I specify all these starting pieces of information when I create my object from the class?

In order to do this, we have to understand something called a constructor, which is a part of the blueprint that allows us to specify what should happen when our object is being constructed.

And this is also known in programming as **initializing an object**. When the object is being initialized, we can set variables or counters to they're starting values. 

In Python, the way that we would create the constructor is by using a special function, which is the `init` function.

For example,

```Python
class Car:
    def __init__(self, seats):
        self.seats = seats
```

The `init` function is going to be called every time you create a new object from this class.

- **Self**: Refers to the actual object that is being created or initialized.
- **Parameters**: Like `seats` in this case. You can add as many parameters as you want. The parameters are gonna be passed in when an object gets constructed from this class.

After `init` function is defined, you have to pass in the required parameters when creating object or else there will be errors appearing.

For example:

`car_1 = Car()` will miss one required argument, `seats`.

### Set Default Values in Init Function

Sometimes in our projects, like creating a new user accounts for apps like instagram, every time a new `User` object is created, the number of followers is always zero at the beginning.

So it seems like a good practice to define a default value of zero for `followers` attribute of the object, saving the number to explicitly assign the value like: 

```Python
user_1 = User()
user_1.followers = 0
```

We can define the default value within `init` like:

```Python
class User:

    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.follower = 0
```

## What is Object Attribute

Attributes are the things that the object will have.

Like for an object of `Car` class, it has attributes like `seats = 5`