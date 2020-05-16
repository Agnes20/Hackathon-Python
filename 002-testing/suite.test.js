    const split = require('./test02-split.js');                                                  //L-1

    test('Split("user:ape1:ape2:city",\':\' to equals ["user","ape1","ape2","city"] )', ()=>{    //L-3
    // Arrange
    var expected = ["user","ape1","ape2","city"];                                                //L-5

    // Act
    var result = split("user:ape1:ape2:city",':');                                               //L-8
    
    // Assert
    expect(result).toStrictEqual(expected);                                                      //L-11
    });                                                                  //L-12

//chartAt
const charAt = require('./test02-charAt.js');                                      //L-1

    test('CharAt("user:ape1:ape2:city",8)  to equals 1 )', ()=>{                                //L-3
    // Arrange
    var toBe = '1';                                                                             //L-5

    // Act
    var result = charAt("user:ape1:ape2:city", 8);                                              //L-8
    
    // Assert
    expect(result).toEqual(toBe);                                                               //L-11
    });                                                                                         //L-12

const toLowerCase = require('./test02-toLowerCase.js');                                      //L-1

    test('toLowerCase("Hello World") to equals "hello world")', ()=>{                            //L-3
    // Arrange
    var toBe = "hello world";                                                                    //L-5

    // Act
    var result = toLowerCase("Hello World");                                                     //L-8
    
    // Assert
    expect(result).toBe(toBe);                                                                   //L-11
    });                                                                                          //L-12


const toUppercase = require('./test02-toUppercase.js');                                      //L-1

    test('toUppercase("Hello World") to equals "HELLO WORLD")', ()=>{                            //L-3
    // Arrange
    var toBe = "HELLO WORLD";                                                                    //L-5

    // Act
    var result = toUppercase("Hello World");                                                     //L-8
    
    // Assert
    expect(result).toBe(toBe);                                                                   //L-11
    });                                                                                          //L-12

const indexOf = require('./test02-indexOf.js');                                              //L-1

    test('indexOf("Hello World","World") to equals 6)', ()=>{                                    //L-3
    // Arrange
    var toBe = 6;                                                                                //L-5

    // Act
    var result = indexOf("Hello World","World");                                                 //L-8
    
    // Assert
    expect(result).toBe(toBe);                                                                   //L-11
    });                                                                                          //L-12


