const car = {
    name: "vato",
    lastname: "imnaishvili",
    age: 17,
    ageplus: function() {
        this.age+=1
    }
  };
  function Person(name, age, gender) {
    this.name = name;
    this.age = age;
    this.gender = gender;
  }

  const person1 = new Person("imnaishvili", 17, "male");
  function Car(brand, model, year, color, horsePower) {
    this.brand = brand;
    this.model = model;
    this.year = year;
    this.color = color;
    this.horsePower = horsePower;
  
    this.horsePowerplus = function() {
      this.horsePower += 100;}
}