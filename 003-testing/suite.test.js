const toString = require('./test03-toString.js');                                            //L-1

    test('toString(789) to equals "789" )', ()=>{                                                //L-3
    // Arrange
    var expected = "789";                                                                        //L-5

    // Act
    var result = toString(789);                                                                  //L-8
    
    // Assert
    expect(result).toBe(expected);                                                               //L-11
    });                                                                                          //L-12

    const toFixed = require('./test03-toFixed.js');                                            //L-1

    test('toFixed(123456.52,5)  to equals "123456.52000" )', ()=>{                             //L-3
    // Arrang
    var toBe =  "123456.52000";                                                                //L-5

    // Act
    var result = toFixed(123456.52,5);                                                         //L-8
    
    // Assert
    expect(result).toBe(toBe);                                                                 //L-11
    });                                                                                        //L-12

    