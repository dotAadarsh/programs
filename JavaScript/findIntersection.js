// https://coderbyte.com/editor/Find%20Intersection:JavaScript
// https://dev.to/coderbyte/a-common-coding-interview-question-461f

function FindIntersection(strArr) { 
    const inBothStrings = []
    const arr1 = strArr[0].split(', ')
    const arr2 = strArr[1].split(', ')
    arr1.forEach(elementArr1 => {
      const numArr1 = parseInt(elementArr1)
      arr2.forEach(elementArr2 =>{
        const numArr2 = parseInt(elementArr2)
        if(numArr1 === numArr2) {
          inBothStrings.push(numArr1)
        }
      })
    })
    return inBothStrings.join(','); 
  
  }
     
  // keep this function call here 
  console.log(FindIntersection(readline()));