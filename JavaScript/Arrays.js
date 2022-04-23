var myArray = [1,2,3,4,5]
console.log(myArray[0])

var theSameArr = new Array(1,2,3,4,5)
console.log(theSameArr[4])

var newArr = []
newArr[3] = "Hello"
console.log(newArr)

var myEleArr = ["string", 10, {}]
console.log(myEleArr[0])


// Manipulating arrays
// Pushing and popping

var myStack = [];
myStack.push(1);
myStack.push(2);
myStack.push(3);
console.log(myStack)

console.log(myStack.pop())
console.log(myStack)

// Queues using shifting and unshifting

var myQueue = [];
myQueue.push(1);
myQueue.push(2);
myQueue.push(3);

console.log(myQueue.shift()) // Remove the variables of the array in the exact order they were inserted in
console.log(myQueue.shift())

console.log(myQueue)
 
myQueue.unshift(0) //insert a variable at the beginning of an arra
console.log(myQueue)

// Splicing

var myArray = [1,2,3,4,5,6,7,8,9,10];
var splice = myArray.splice(3,6);

console.log(splice)
console.log(myArray)