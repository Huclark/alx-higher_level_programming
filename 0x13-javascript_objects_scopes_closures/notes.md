# Key Notes

## Dot Notation vs Bracket Notation

Dot Notation is usually preferred over bracket notation because it is more succinct and easier to read. However there are some cases where you have to use square brackets. For example, if an object property name is held in a variable, then you can't use dot notation to access the value, but you can access the value using bracket notation.

In the example below, the `logProperty()` function can use `person[propertyName]` to retrieve the value of the property named in `propertyName`.

```JavaScript
const person = {
  name: ["Bob", "Smith"],
  age: 32,
};

function logProperty(propertyName) {
  console.log(person[propertyName]);
}

logProperty("name");
// ["Bob", "Smith"]
logProperty("age");
// 32
```

One useful aspect of bracket notation is that it can be used to set not only member values dynamically, but member names too. Let's say we wanted users to be able to store custom value types in their people data, by typing the member name and value into two text inputs. We could get those values like this:

```JavaScript
const myDataName = "height";
const myDataValue = "1.75m";
person[myDataName] = myDataValue;
```

Adding a property to an object using the method above isn't possible with dot notation, which can only accept a literal member name, not a variable value pointing to a name.Like this:

```JavaScript
const myDataName = "height";
const myDataValue = "1.75m";
person.myDataName = myDataValue;
```

will not have `height` as the property name.

## Introducing constructors

Using object literals is fine when you only need to create one object, but if you have to create more than one, they're seriously inadequate. We have to write out the same code for every object we create, and if we want to change some properties of the object - like adding a `height` property - then we have to remember to update every object.

The first version of this is just a function:

```JavaScript
function createPerson(name) {
  const obj = {};
  obj.name = name;
  obj.introduceSelf = function () {
    console.log(`Hi! I'm ${this.name}.`);
  };
  return obj;
}
```

This function creates and returns a new object each time we call it. The object will have two members:

- a property `name`
- a method `introduceSelf()`

This function creates and returns a new object each time we call it. The object will have two members:

```JavaScript
const salva = createPerson("Salva");
salva.name;
salva.introduceSelf();
// "Hi! I'm Salva."

const frankie = createPerson("Frankie");
frankie.name;
frankie.introduceSelf();
// "Hi! I'm Frankie."
```

A better way is to use a constructor. A constructor is just a function called using the `new` keyword. When you call a constructor, it will:

- create a new object
- bind `this` to the new object, so you can refer to `this` in your constructor code
- run the code in the constructor
- return the new object

Constructors, just like classes, start with a capital letter. So we could rewrite the our function like this:

```JavaScript
function Person(name) {
  this.name = name;
  this.introduceSelf = function () {
    console.log(`Hi! I'm ${this.name}.`);
  };
}
```

To call `Person()` as a constructor, we use `new` like this:

```JavaScript
const salva = new Person("Salva");
salva.name;
salva.introduceSelf();
// "Hi! I'm Salva."

const frankie = new Person("Frankie");
frankie.name;
frankie.introduceSelf();
// "Hi! I'm Frankie."
```

## Classes and Constructors

You can declare a class using the `class` keyword. Here's a class declaration for our `Person` from the previous article:

```JavaScript
class Person {
  name = '';

  constructor(name) {
    this.name = name;
  }

  introduceSelf() {
    console.log(`Hi! I'm ${this.name}`);
  }
}
```

The `constructor` keyword is in-built used to create a constructor.
Given the class declaration code above, you can create and use a new `Person` instance like this:

```JavaScript
const giles = new Person("Giles");

giles.introduceSelf(); // Hi! I'm Giles
```

If you don't need to do any special initialization, you can omit the constructor, and a default constructor will be generated for you:

```JavaScript
class Animal {
  sleep() {
    console.log("zzzzzzz");
  }
}

const spot = new Animal();

spot.sleep(); // 'zzzzzzz'
```

## Inheritance

Given our `Person` class above, let's define the `Professor` subclass.

```JavaScript
class Professor extends Person {
  teaches = "";

  constructor(name, teaches) {
    super(name);
    this.teaches = teaches;
  }

  introduceSelf() {
    console.log(
      `My name is ${this.name}, and I will be your ${this.teaches} professor.`,
    );
  }

  grade(paper) {
    const grade = Math.floor(Math.random() * (5 - 1) + 1);
    console.log(grade);
  }
}
```

We use the `extends` keyword to say that this class inherits from another class.

The `Professor` class adds a new property `teaches`, so we declare that.

Since we want to set `teaches` when a new `Professor` is created, we define a constructor, which takes the `name` and `teaches` as arguments. The first thing this constructor does is call the superclass constructor using `super()`, passing up the `name` parameter. The superclass constructor takes care of setting `name`. After that, the `Professor` constructor sets the `teaches` property.

With this declaration we can now create and use professors:

```JavaScript
const walsh = new Professor("Walsh", "Psychology");
walsh.introduceSelf(); // 'My name is Walsh, and I will be your Psychology professor'

walsh.grade("my paper"); // some random grade
```
